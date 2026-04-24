from dataclasses import dataclass, field
from typing import Literal, Protocol


@dataclass(frozen=True)
class LLMMessage:
    role: Literal["system", "user", "assistant", "tool"]
    content: str


@dataclass(frozen=True)
class LLMTool:
    name: str
    description: str
    input_schema: dict[str, object]


@dataclass(frozen=True)
class LLMCompletion:
    content: str
    tool_calls: tuple[dict[str, object], ...] = field(default_factory=tuple)


class LLMProviderError(Exception):
    """Base class for LLM provider failures."""


class LLMProviderNotConfigured(LLMProviderError):
    """Raised when a provider cannot run because required settings are missing."""


class LLMProviderNotImplemented(LLMProviderError):
    """Raised by scaffolded providers before live network calls are implemented."""


class LLMProvider(Protocol):
    name: str

    async def complete(
        self,
        messages: list[LLMMessage],
        tools: list[LLMTool],
        metadata: dict[str, str],
    ) -> LLMCompletion:
        """Return an assistant completion for the supplied message history."""
