import re

def macros_transformer(path, file):
	f = open(path + file, "r")
	content = f.read()
	f.close()

	#### Remove comments
	content = re.sub(r'%(.*?)\n', r'\n', content)

	new_content = ""

	list_com = re.findall(r'\\(re)?newcommand\{\\(.*?)\}\[(\d*?)\]\{(.*?)\}[^\}]*?\n', content)

	for com in list_com:
		new_com = "          \"" + com[1] + "\"      : " + "[\"" + com[3].replace("\\", "\\\\") + "\", " + com[2] + "]"
		# print(new_com)
		new_content = new_content + "\n" + new_com

	list_com = re.findall(r'\\(re)?newcommand\{\\(.*?)\}\{(.*?)\}[^\}]*?\n', content)

	for com in list_com:
		new_com = "          \"" + com[1] + "\"      : " + "\"" + com[2].replace("\\", "\\\\") + "\""
		# print(new_com)
		new_content = new_content + "\n" + new_com

	new_content = re.sub(r'\\textsc', r'\\textbf', new_content)

	print(new_content)
	return(new_content)

	# g = open("_config.yml", "a")
	# g.write(new_content)
	# g.close()

# macros_transformer("", "macros.tex")
