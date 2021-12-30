# 1- Regular Expressions

import re

my_string = "Let's write RegEx!"
result = re.findall(r"\w+", my_string)
print(result)

# re.split() and re.findall()

my_string = "Let's write RegEx!  Won't that be fun?  I sure think so.  Can you find 4 sentences?  Or perhaps, all 19 words?"

# Write a pattern to match sentence endings: sentence_endings
sentence_endings = (r"[.?!]")
print(re.split(sentence_endings, my_string))