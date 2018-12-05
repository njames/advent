# get input from command line by redirection
# to test we will simply print the file to output

import sys

lines = []
current = [0]
counter = 0

for line in sys.stdin:
  stripped = line.strip()
  if not stripped: break
  lines.append(stripped)
  current.append(current[counter] + int(stripped))
  counter += 1
  if current[counter] in current[:counter]:
  	print(current[counter])
  	break

print('nooooooo')
