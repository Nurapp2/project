import re

content = "DdNdJdcvFcvbfcvghfcvbhnjh"

match = re.split(r'[A-Z]', content)

print(match)