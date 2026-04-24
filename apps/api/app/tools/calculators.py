from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from typing import TypeAlias

NumberInput: TypeAlias = Decimal | int | float | str

CENT = Decimal("0.01")


@dataclass(frozen=True)
class MortgagePaymentResult:
    principal: Decimal
    annual_interest_rate_percent: Decimal
    amortization_years: int
    payments_per_year: int
    compounding_periods_per_year: int
    periodic_interest_rate: Decimal
    payment: Decimal
    total_paid: Decimal
    total_interest: Decimal


@dataclass(frozen=True)
class LandTransferTaxBracket:
    lower_bound: Decimal
    upper_bound: Decimal | None
    rate: Decimal
    taxable_amount: Decimal
    tax: Decimal


@dataclass(frozen=True)
class LandTransferTaxResult:
    purchase_price: Decimal
    provincial_tax: Decimal
    first_time_home_buyer_rebate: Decimal
    total_tax: Decimal
    brackets: tuple[LandTransferTaxBracket, ...]


def mortgage_payment(
    principal: NumberInput,
    annual_interest_rate_percent: NumberInput,
    amortization_years: int,
    *,
    payments_per_year: int = 12,
    compounding_periods_per_year: int = 2,
) -> MortgagePaymentResult:
    """Calculate a periodic mortgage payment.

    The default compounding is semi-annual, matching the Canadian mortgage convention.
    """

    principal_decimal = _positive_money(principal, "principal")
    annual_rate = _non_negative_decimal(
        annual_interest_rate_percent, "annual_interest_rate_percent"
    )

    if amortization_years <= 0:
        raise ValueError("amortization_years must be greater than 0.")
    if payments_per_year <= 0:
        raise ValueError("payments_per_year must be greater than 0.")
    if compounding_periods_per_year <= 0:
        raise ValueError("compounding_periods_per_year must be greater than 0.")

    number_of_payments = amortization_years * payments_per_year

    if annual_rate == 0:
        periodic_rate = Decimal("0")
        raw_payment = principal_decimal / Decimal(number_of_payments)
    else:
        periodic_rate = _periodic_interest_rate(
            annual_rate,
            payments_per_year=payments_per_year,
            compounding_periods_per_year=compounding_periods_per_year,
        )
        raw_payment = principal_decimal * periodic_rate / (
            Decimal("1") - (Decimal("1") + periodic_rate) ** Decimal(-number_of_payments)
        )

    payment = _to_cents(raw_payment)
    total_paid = _to_cents(payment * Decimal(number_of_payments))
    total_interest = _to_cents(total_paid - principal_decimal)

    return MortgagePaymentResult(
        principal=_to_cents(principal_decimal),
        annual_interest_rate_percent=annual_rate,
        amortization_years=amortization_years,
        payments_per_year=payments_per_year,
        compounding_periods_per_year=compounding_periods_per_year,
        periodic_interest_rate=periodic_rate,
        payment=payment,
        total_paid=total_paid,
        total_interest=total_interest,
    )


def ontario_land_transfer_tax(
    purchase_price: NumberInput,
    *,
    first_time_home_buyer: bool = False,
    single_family_residence: bool = True,
) -> LandTransferTaxResult:
    """Calculate Ontario provincial land transfer tax.

    The first-time home buyer rebate is capped at $4,000 and cannot exceed the tax owed.
    """

    price = _positive_money(purchase_price, "purchase_price")
    brackets = _ontario_brackets(single_family_residence=single_family_residence)
    charges: list[LandTransferTaxBracket] = []
    provincial_tax = Decimal("0")

    for lower_bound, upper_bound, rate in brackets:
        if price <= lower_bound:
            continue

        bracket_ceiling = price if upper_bound is None else min(price, upper_bound)
        taxable_amount = bracket_ceiling - lower_bound
        tax = _to_cents(taxable_amount * rate)
        provincial_tax += tax

        charges.append(
            LandTransferTaxBracket(
                lower_bound=_to_cents(lower_bound),
                upper_bound=_to_cents(upper_bound) if upper_bound is not None else None,
                rate=rate,
                taxable_amount=_to_cents(taxable_amount),
                tax=tax,
            )
        )

    provincial_tax = _to_cents(provincial_tax)
    rebate = Decimal("0")
    if first_time_home_buyer:
        rebate = min(provincial_tax, Decimal("4000.00"))

    return LandTransferTaxResult(
        purchase_price=_to_cents(price),
        provincial_tax=provincial_tax,
        first_time_home_buyer_rebate=_to_cents(rebate),
        total_tax=_to_cents(provincial_tax - rebate),
        brackets=tuple(charges),
    )


def _periodic_interest_rate(
    annual_rate_percent: Decimal,
    *,
    payments_per_year: int,
    compounding_periods_per_year: int,
) -> Decimal:
    annual_rate = annual_rate_percent / Decimal("100")
    base = Decimal("1") + (annual_rate / Decimal(compounding_periods_per_year))
    exponent = Decimal(compounding_periods_per_year) / Decimal(payments_per_year)

    with localcontext() as context:
        context.prec = 34
        return (base.ln() * exponent).exp() - Decimal("1")


def _ontario_brackets(
    *, single_family_residence: bool
) -> tuple[tuple[Decimal, Decimal | None, Decimal], ...]:
    terminal_rate = Decimal("0.025") if single_family_residence else Decimal("0.02")

    return (
        (Decimal("0"), Decimal("55000"), Decimal("0.005")),
        (Decimal("55000"), Decimal("250000"), Decimal("0.01")),
        (Decimal("250000"), Decimal("400000"), Decimal("0.015")),
        (Decimal("400000"), Decimal("2000000"), Decimal("0.02")),
        (Decimal("2000000"), None, terminal_rate),
    )


def _positive_money(value: NumberInput, name: str) -> Decimal:
    decimal_value = _decimal(value, name)
    if decimal_value <= 0:
        raise ValueError(f"{name} must be greater than 0.")
    return decimal_value


def _non_negative_decimal(value: NumberInput, name: str) -> Decimal:
    decimal_value = _decimal(value, name)
    if decimal_value < 0:
        raise ValueError(f"{name} must be greater than or equal to 0.")
    return decimal_value


def _decimal(value: NumberInput, name: str) -> Decimal:
    try:
        decimal_value = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"{name} must be a valid number.") from exc

    if not decimal_value.is_finite():
        raise ValueError(f"{name} must be finite.")

    return decimal_value


def _to_cents(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)

