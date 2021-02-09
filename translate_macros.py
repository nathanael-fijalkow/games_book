import re

def translate():
	f = open("macros.tex", "r")
	content = f.read()
	f.close()

	#### Remove comments
	content = re.sub(r'%(.*?)\n', r'\n', content)

	new_content = ""

	list_com = re.findall(r'\\(re)?newcommand\{\\(.*?)\}\[1\]\{(.*?)\}[^\}]*?\n', content)

	for com in list_com:
		new_com = "          \"" + com[1] + "\"      : " + "[\"" + com[2].replace("\\", "\\\\") + "\", 1]"
		# print(new_com)
		new_content = new_content + "\n" + new_com

	list_com = re.findall(r'\\(re)?newcommand\{\\(.*?)\}\{(.*?)\}[^\}]*?\n', content)

	for com in list_com:
		new_com = "          \"" + com[1] + "\"      : " + "\"" + com[2].replace("\\", "\\\\") + "\""
		# print(new_com)
		new_content = new_content + "\n" + new_com

	print(new_content)

	# g = open("_config.yml", "a")
	# g.write(new_content)
	# g.close()

translate()