import re
import sys

File = sys.argv[1]

f = open(File, "r")

content = f.read()

list_matches = re.findall(r'~\\cite\{(.*?)\}', content)

for x in list_matches:
	print(x)

new = re.sub(r'~\\cite\{(.*?)\}', r' {cite}`\1`', content)

print(new)
f.close()

g = open(File, "w")

g.write(new)


