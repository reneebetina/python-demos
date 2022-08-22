regex_integer_in_range = r"^[1-9][0-9]{5}"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d).[^$1]"	# Do not delete 'r'.
# captures digit, followed by something (.) and then checks if the next digit is not like the captured one

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# Sample Input
# 110000

# Sample Output
# False