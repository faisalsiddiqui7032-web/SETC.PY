
# Calculate late fee
def late_fee(days):
    return days * 5


# Check whether fee is waived
def is_waived(amount):
    return amount <= 100
