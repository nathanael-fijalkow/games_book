import re

def macros_transformer(path, file):
	f = open(path + file, "r")
	content = f.read()
	f.close()

	#### Remove comments
	content = re.sub(r'%(.*?)\n', r'\n', content)

	#### Remove "re"
	content = re.sub(r'\\renewcommand\{(.*?)\}\{(.*?)\}\s',\
		r'\\ifdefined\1\n    \\renewcommand{\1}{\2}\n\\else\n    \\newcommand{\1}{\2}\n\\fi', content)

	# print(content)

	g = open(path + "norenew_" + file, "w")
	g.write(content)
	g.close()
