
# 1. Import package
import bankkit

# 2. Import fees with full path
import bankkit.fees as fe

# 3. Import functions from sub-package
from bankkit.reports.statement import line, banner

# 4. Print package version
print(bankkit.VERSION)

# 5. Simple interest
from bankkit import simple_interest

print(simple_interest(10000, 5, 2))

# 6. Compound interest
print(bankkit.interest.compound(1000, 10, 2))

# 7. Fees
print(fe.late_fee(4), fe.is_waived(80))

# 8. Report
banner("Report")
line("Total", 1210)

