import sys

LENGTH_FACTORS = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,  # mile
    "yd": 0.9144,  # yard
    "ft": 0.3048,  # foot
    "in": 0.0254,  # inch
}

WEIGHT_FACTORS = {
    "kg": 1.0,
    "g": 0.001,
    "mg": 1e-6,
    "lb": 0.45359237,  # pound
    "oz": 0.028349523125,  # ounce
    "ton": 1000.0,  # metric ton
}

VOLUME_FACTORS = {
    "l": 1.0,  # liter
    "ml": 0.001,
    "m3": 1000.0,  # cubic meter
    "cm3": 0.001,  # cubic centimeter == milliliter
    "cup": 0.2365882365,  # US cup
    "pt": 0.473176473,  # pint
    "qt": 0.946352946,  # quart
    "gal": 3.785411784,  # gallon (US)
}

SPEED_FACTORS = {
    "m/s": 1.0,
    "km/h": 1000.0 / 3600.0,  # 0.277777...
    "mph": 0.44704,  # miles per hour
    "knot": 0.5144444444444445,
}

AREA_FACTORS = {
    "m2": 1.0,
    "km2": 1e6,
    "cm2": 0.0001,
    "mm2": 1e-6,
    "acre": 4046.8564224,
    "hectare": 10000.0,
}

CATEGORIES = {
    "length": LENGTH_FACTORS,
    "weight": WEIGHT_FACTORS,
    "volume": VOLUME_FACTORS,
    "speed": SPEED_FACTORS,
    "area": AREA_FACTORS,
}


def convert_linear(value: float, from_unit: str, to_unit: str, factors: dict) -> float:

    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Invalid unit for conversion.")
    value_in_base = value * factors[from_unit] 
    result = value_in_base / factors[to_unit]  
    return result


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
  
    from_u = from_unit.upper()
    to_u = to_unit.upper()
    valid = {"C", "F", "K"}
    if from_u not in valid or to_u not in valid:
        raise ValueError("Invalid temperature unit.")

    if from_u == "C":
        c = value
    elif from_u == "F":
        c = (value - 32) * 5.0/9.0
    elif from_u == "K":
        c = value - 273.15

    if to_u == "C":
        return c
    elif to_u == "F":
        return c * 9.0/5.0 + 32
    elif to_u == "K":
        return c + 273.15