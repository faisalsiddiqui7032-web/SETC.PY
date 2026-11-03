
# Method 1: Import whole module
import unitconv

# Method 2: Import specific names
from unitconv import c_to_f, KM_PER_MILE

# Method 3: Import with alias
import unitconv as uc


# 1. Whole module
print(unitconv.km_to_miles(42.195))


# 2. Specific names
print(c_to_f(37), KM_PER_MILE)


# 3. Alias
print(uc.c_to_f(-40), uc.km_to_miles(10))


# 4. Public names using dir()
public_names = [
    name for name in dir(unitconv)
    if not name.startswith("_")
]

print(public_names)


# 5. Module name and main file name
print(unitconv.__name__)
print(__name__)


# Comment: The main guard runs only when unitconv.py is executed directly,
# not when it is imported into another file.
