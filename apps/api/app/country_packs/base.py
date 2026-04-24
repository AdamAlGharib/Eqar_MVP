from dataclasses import dataclass


@dataclass(frozen=True)
class CountryPack:
    key: str
    country_code: str
    region_code: str
    display_name: str
    currency_code: str
    tool_names: tuple[str, ...]

