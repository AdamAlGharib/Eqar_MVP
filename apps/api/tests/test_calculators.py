from decimal import Decimal

import pytest

from app.tools.calculators import mortgage_payment, ontario_land_transfer_tax


def test_mortgage_payment_uses_canadian_semi_annual_compounding_by_default() -> None:
    result = mortgage_payment(
        principal=500_000,
        annual_interest_rate_percent=5,
        amortization_years=25,
    )

    assert result.payment == Decimal("2908.02")
    assert result.total_paid == Decimal("872406.00")
    assert result.total_interest == Decimal("372406.00")
    assert result.payments_per_year == 12
    assert result.compounding_periods_per_year == 2


def test_mortgage_payment_handles_zero_interest() -> None:
    result = mortgage_payment(
        principal=120_000,
        annual_interest_rate_percent=0,
        amortization_years=10,
    )

    assert result.payment == Decimal("1000.00")
    assert result.total_interest == Decimal("0.00")


def test_mortgage_payment_rejects_invalid_values() -> None:
    with pytest.raises(ValueError):
        mortgage_payment(principal=0, annual_interest_rate_percent=5, amortization_years=25)

    with pytest.raises(ValueError):
        mortgage_payment(principal=500_000, annual_interest_rate_percent=-1, amortization_years=25)

    with pytest.raises(ValueError):
        mortgage_payment(principal=500_000, annual_interest_rate_percent=5, amortization_years=0)


def test_ontario_land_transfer_tax_for_mid_market_purchase() -> None:
    result = ontario_land_transfer_tax(500_000)

    assert result.provincial_tax == Decimal("6475.00")
    assert result.first_time_home_buyer_rebate == Decimal("0.00")
    assert result.total_tax == Decimal("6475.00")
    assert len(result.brackets) == 4


def test_ontario_land_transfer_tax_applies_first_time_buyer_rebate_cap() -> None:
    result = ontario_land_transfer_tax(500_000, first_time_home_buyer=True)

    assert result.provincial_tax == Decimal("6475.00")
    assert result.first_time_home_buyer_rebate == Decimal("4000.00")
    assert result.total_tax == Decimal("2475.00")


def test_ontario_land_transfer_tax_single_family_surtax_over_two_million() -> None:
    result = ontario_land_transfer_tax(3_000_000)

    assert result.provincial_tax == Decimal("61475.00")
    assert result.total_tax == Decimal("61475.00")


def test_ontario_land_transfer_tax_rejects_invalid_price() -> None:
    with pytest.raises(ValueError):
        ontario_land_transfer_tax(0)

