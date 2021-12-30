# 1- Regular Expressions

import re

my_string = "Let's write RegEx!"
result = re.findall(r"\w+", my_string)
print(result)
