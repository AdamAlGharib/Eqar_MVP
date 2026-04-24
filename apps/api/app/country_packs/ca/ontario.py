from app.country_packs.base import CountryPack

ONTARIO_PACK = CountryPack(
    key="CA-ON",
    country_code="CA",
    region_code="ON",
    display_name="Canada - Ontario",
    currency_code="CAD",
    tool_names=("mortgage_payment", "ontario_land_transfer_tax"),
)

