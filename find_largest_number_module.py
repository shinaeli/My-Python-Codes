# Using 'import' only imports all the entities present in the 'utils' module
import utils
# Using 'from - imports' imports only the needed function from the 'utils' module
from utils import find_max
test_list = [5, 2, 1, 8, 3, 16, 9, 11, 7]

print(utils.find_max(test_list))
print(find_max(test_list))