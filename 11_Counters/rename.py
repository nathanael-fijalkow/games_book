import re
import os 

os.chdir('.') 

def rename():
	for f in os.listdir('.'):
		if os.path.splitext(f)[1] == ".tex":
			g = open(f, "r")
			content = g.read()
			g.close()
			content = re.sub(r' \$\\EXPSPACE\$\\', r' $\EXPSPACE$ ', content)
			g = open(f, "w")
			content = g.write(content)
			g.close()
		if os.path.isdir(f):
			os.chdir(f)
			rename()
			os.chdir('./..') 

rename()