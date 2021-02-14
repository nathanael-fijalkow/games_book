import re
import os 

os.chdir('.') 

def rename():
	for f in os.listdir('.'):
		if os.path.splitext(f)[1] == ".tex":
			g = open(f, "r")
			content = g.read()
			g.close()
			content = re.sub(r'\\begin\{principle\}', r'\\begin{property}', content)
			content = re.sub(r'\\end\{principle\}', r'\\end{property}', content)
			g = open(f, "w")
			content = g.write(content)
			g.close()
		if os.path.isdir(f):
			os.chdir(f)
			rename_principle_into_convention()
			os.chdir('./..') 

rename()