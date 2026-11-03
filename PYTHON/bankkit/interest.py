
# Simple Interest
def simple_interest(p, r, t):
    return p * r * t / 100


# Compound Interest
def compound(p, r, t):
    amount = p * (1 + r / 100) ** t
    return round(amount, 2)
