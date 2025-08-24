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
