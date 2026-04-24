from app.country_packs.base import CountryPack
from app.country_packs.ca import CANADA_PACKS

_PACKS = {pack.key: pack for pack in CANADA_PACKS}


class UnsupportedCountryPackError(ValueError):
    """Raised when no deterministic country pack exists for a request."""


def get_country_pack(country_code: str, region_code: str | None = None) -> CountryPack:
    normalized_country = country_code.upper()
    normalized_region = (region_code or "").upper()
    key = f"{normalized_country}-{normalized_region}" if normalized_region else normalized_country

    if key in _PACKS:
        return _PACKS[key]

    fallback_key = f"{normalized_country}-ON" if normalized_country == "CA" else normalized_country
    if fallback_key in _PACKS:
        return _PACKS[fallback_key]

    raise UnsupportedCountryPackError(f"Unsupported country pack: {country_code}/{region_code or '*'}")


__all__ = ["CountryPack", "UnsupportedCountryPackError", "get_country_pack"]
