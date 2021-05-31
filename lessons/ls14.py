"""Named constants and f-strings."""

INTEREST_RATE: float = 0.009
# constant that isn't changing - global variable

def compound(current_balance: float) -> float:
    print(f"The interest rate is {INTEREST_RATE}")
    return current_balance + (current_balance * INTEREST_RATE)


compound(10.0)