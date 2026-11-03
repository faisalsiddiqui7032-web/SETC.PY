
print("bankkit loaded")

VERSION = "3.1"

from .interest import simple_interest


#The __init__.py file is used to make a
#  directory behave as a Python package.
#  It executes when the package is imported. 
# It can also initialize package variables and import 
# functions from other modules, making them accessible
#  directly through the package.