
import math
import random

# 1. Number of buses needed
passengers = 129
bus_capacity = 25

buses = math.ceil(passengers / bus_capacity)
print(buses)


# 2. Convert seconds into hours, minutes and seconds
total_seconds = 7384

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, minutes, seconds)


# 3. Simplify a fraction using math.gcd
def simplify(n, d):
    gcd = math.gcd(n, d)
    return (n // gcd, d // gcd)

print(simplify(36, 84))


# 4. Calculate tower height
dist = 120
angle = 60

height = dist * math.tan(math.radians(angle))
print(round(height, 2))


# 5. Roll a die 5 times
random.seed(31)

rolls = []

for i in range(5):
    rolls.append(random.randint(1, 6))

print(rolls, sum(rolls))


# 6. Shuffle deck and choose random option
deck = list(range(1, 9))

random.shuffle(deck)
print(deck)
