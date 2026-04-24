from collections.abc import Callable, Mapping
from dataclasses import asdict, dataclass
from decimal import Decimal
from inspect import isawaitable
from typing import Any

from app.tools.calculators import mortgage_payment, ontario_land_transfer_tax

ToolHandler = Callable[[Mapping[str, Any]], dict[str, Any]]


@dataclass(frozen=True)
class ToolDefinition:
    name: str
    description: str
    input_schema: dict[str, Any]
    handler: ToolHandler


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolDefinition] = {}

    def register(self, tool: ToolDefinition) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def get(self, name: str) -> ToolDefinition:
        try:
            return self._tools[name]
        except KeyError as exc:
            raise KeyError(f"Unknown tool: {name}") from exc

    def list_tools(self) -> list[ToolDefinition]:
        return list(self._tools.values())

    async def execute(self, name: str, arguments: Mapping[str, Any]) -> dict[str, Any]:
        result = self.get(name).handler(arguments)
        if isawaitable(result):
            result = await result
        return result


def build_default_tool_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(
        ToolDefinition(
            name="mortgage_payment",
            description="Calculate a Canadian mortgage payment and total interest.",
            input_schema={
                "type": "object",
                "additionalProperties": False,
                "required": [
                    "principal",
                    "annual_interest_rate_percent",
                    "amortization_years",
                ],
                "properties": {
                    "principal": {"type": "number", "exclusiveMinimum": 0},
                    "annual_interest_rate_percent": {"type": "number", "minimum": 0},
                    "amortization_years": {"type": "integer", "minimum": 1},
                    "payments_per_year": {"type": "integer", "minimum": 1, "default": 12},
                    "compounding_periods_per_year": {
                        "type": "integer",
                        "minimum": 1,
                        "default": 2,
                    },
                },
            },
            handler=_mortgage_payment_tool,
        )
    )
    registry.register(
        ToolDefinition(
            name="ontario_land_transfer_tax",
            description="Calculate Ontario provincial land transfer tax.",
            input_schema={
                "type": "object",
                "additionalProperties": False,
                "required": ["purchase_price"],
                "properties": {
                    "purchase_price": {"type": "number", "exclusiveMinimum": 0},
                    "first_time_home_buyer": {"type": "boolean", "default": False},
                    "single_family_residence": {"type": "boolean", "default": True},
                },
            },
            handler=_ontario_land_transfer_tax_tool,
        )
    )
    return registry


def _mortgage_payment_tool(arguments: Mapping[str, Any]) -> dict[str, Any]:
    result = mortgage_payment(
        principal=arguments["principal"],
        annual_interest_rate_percent=arguments["annual_interest_rate_percent"],
        amortization_years=int(arguments["amortization_years"]),
        payments_per_year=int(arguments.get("payments_per_year", 12)),
        compounding_periods_per_year=int(arguments.get("compounding_periods_per_year", 2)),
    )
    return _json_safe(asdict(result))


def _ontario_land_transfer_tax_tool(arguments: Mapping[str, Any]) -> dict[str, Any]:
    result = ontario_land_transfer_tax(
        purchase_price=arguments["purchase_price"],
        first_time_home_buyer=bool(arguments.get("first_time_home_buyer", False)),
        single_family_residence=bool(arguments.get("single_family_residence", True)),
    )
    return _json_safe(asdict(result))


def _json_safe(value: Any) -> Any:
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, tuple | list):
        return [_json_safe(item) for item in value]
    if isinstance(value, dict):
        return {key: _json_safe(item) for key, item in value.items()}
    return value

