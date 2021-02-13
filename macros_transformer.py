import re

def macros_transformer(path, file):
	f = open(path + file, "r")
	content = f.read()
	f.close()

	#### Remove comments
	content = re.sub(r'%(.*?)\n', r'\n', content)

	content = re.sub(r'\\renewcommand(.*?)',r'\\newcommand\1', content)

	print(content)

	g = open(path + "norenew_" + file, "w")
	g.write(content)
	g.close()

macros_transformer("", "macros.tex")
