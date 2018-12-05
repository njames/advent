# get input from command line by redirection
# to test we will simply print the file to output

import sys

lines = []
total = 0

for line in sys.stdin:
  stripped = line.strip()
  if not stripped: break
  lines.append(stripped)
  total += int(stripped)
  # total = total + int(stripped)

# for line in lines:
print(total)
