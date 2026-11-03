
import uuid
import time
from datetime import datetime, timezone


# 1. Generate UUID5 for names
names = ['Kavita', 'Lalit', 'Manoj', 'Nisha']

ids = {}

for name in names:
    ids[name] = uuid.uuid5(
        uuid.NAMESPACE_DNS,
        name.lower() + ".example"
    )

for name, value in ids.items():
    print(name, str(value)[:8])

print(len(set(ids.values())) == len(ids))


# 2. Create UUID3 and UUID5
u3 = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
u5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")

print(u3 != u5, u3.version, u5.version)


# 3. Convert timestamp into different formats
ts = 1700000000

print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts)))

print(time.asctime(time.gmtime(ts)))

dt = datetime.fromtimestamp(ts, timezone.utc)

print(dt.strftime("%d %b %Y"))


# 4. Measure execution time
start = time.perf_counter()

total = sum(range(1_000_000))

end = time.perf_counter()

elapsed = end - start

print(total, type(elapsed).__name__, elapsed >= 0)
