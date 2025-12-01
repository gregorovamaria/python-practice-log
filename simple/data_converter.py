"""
Data Converter
Converts:
- Fahrenheit to Celsius and vice versa
- miles to kilometers
- one currency to another
and prints the results to terminal.
"""

from typing import Iterable, Callable, List, Tuple

Conversion = Callable[[float], float]

_CONVERSIONS: dict[tuple[str, str], Conversion] = {
    ("c", "f"): lambda c: c * 9 / 5 + 32,
    ("f", "c"): lambda f: (f - 32) * 5 / 9,
    ("mi", "km"): lambda m: m * 1.60934,
    ("km", "mi"): lambda km: km / 1.60934,
    ("usd", "eur"): lambda x: x * 0.86,
    ("eur", "usd"): lambda x: x * 1.16,
}


def _normalize_unit(unit: str) -> str:
    """Normalize user inputs and map them to short units"""

    u = unit.strip().lower()

    if u in ("c", "celsius"):
        return "c"
    if u in ("f", "fahrenheit"):
        return "f"
    if u in ("km", "kilometer", "kilometers"):
        return "km"
    if u in ("mi", "mile", "miles"):
        return "mi"
    if u in ("usd", "eur"):
        return u
    raise ValueError(f"Unsupported unit: {unit!r}")


def convert(
    values: Iterable[float], from_unit: str, to_unit: str
) -> Tuple[List[float], List[float]]:
    """
    Convert an iterable of values from one unit to another and
    return (original_values, converted_values) rounded to 2 decimals.
    """
    src = list(values)
    if not src:
        raise ValueError("values must not be empty")

    src_u = _normalize_unit(from_unit)
    dst_u = _normalize_unit(to_unit)

    try:
        fn = _CONVERSIONS[(src_u, dst_u)]
    except KeyError:
        raise ValueError(
            f"No conversion defined from {from_unit} to {to_unit}"
        ) from None

    converted = [round(fn(v), 2) for v in src]
    return src, converted


def main() -> None:
    """Convert source data target data vice versa and print results to terminal."""
    fahrenheit = [32, 50, 77, 100, 212]
    celsius = [-30, 0, 10, 22, 32]
    miles = [10, 20, 30, 40]
    kms = [4, 8, 12, 20, 32]
    usd = [10, 30, 60, 100]
    eur = [20, 40, 80, 120]

    fahrenheit_to_celsius = convert(fahrenheit, "fahrenheit", "celsius")
    celsius_to_fahrenheit = convert(celsius, "celsius", "F")
    miles_to_km = convert(miles, "miles", "km")
    km_to_miles = convert(kms, "km", "mi")
    usd_to_eur = convert(usd, "usd", "eur")
    eur_to_usd = convert(eur, "EUR  ", "USD")

    print("----- TEMPERATURE CONVERTER -----")
    print(
        f"Temperatures in fahrenheit (original): {fahrenheit_to_celsius[0]}\
            \nTemperatures in celsius (converted):{fahrenheit_to_celsius[1]}"
    )
    print(
        f"Temperatures in celsius (original):{celsius_to_fahrenheit[0]}\
            \nTemperatures in fahrenheit (converted): {celsius_to_fahrenheit[1]}"
    )

    print("----- DISTANCE CONVERTER -----")
    print(
        f"Distance in miles (original):{miles_to_km[0]}\
            \nDistance in kilometers (converted): {miles_to_km[1]}"
    )
    print(
        f"Distance in kilometers (original):{km_to_miles[0]}\
            \nDistance in miles (converted): {km_to_miles[1]}"
    )

    print("----- CURRENCY CONVERTER -----")
    print(
        f"Currency in USD (original):{usd_to_eur[0]}\
            \nCurrency in EUR (converted): {usd_to_eur[1]}"
    )
    print(
        f"Currency in EUR (original):{eur_to_usd[0]}\
            \nCurrency in USD (converted): {eur_to_usd[1]}"
    )


if __name__ == "__main__":
    main()
