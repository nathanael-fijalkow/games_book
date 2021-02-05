import re
import sys

File = sys.argv[1]

f = open(File, "r")

content = f.read()

content = re.sub(r'\{\\"u}', r'&uuml;', content)
content = re.sub(r'\{\\"i}', r'&iuml;', content)
content = re.sub(r'\{\\\'e}', r'&eacute;', content)
content = re.sub(r'\{\\\`e}', r'&egrave;', content)

print(content)
f.close()

g = open(File, "w")

g.write(content)


