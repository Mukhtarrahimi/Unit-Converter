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
