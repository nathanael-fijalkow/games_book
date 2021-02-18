import re

def rewrite_macros(path, file):
	f = open(path + file + ".md", "r")
	content = f.read()
	f.close()

	list_macros = re.findall(r'\\newcommand{(.*?)}{(.*?)}\s', content)

	match = re.search(r'([\s\S]*)```{math}[\s\S]*?```([\s\S]*)', content)
	pre_macro = match.group(1) 
	post_macro = match.group(2)

	# print("list macros unprotected:\n{}".format(list_macros))
	# print("text before the macros:\n{}".format(pre_macro))
	# print("text after the macros:\n{}".format(post_macro))

	macros = []
	for (macro, replace) in list_macros:
		macro = re.sub(r'\\', r'\\\\', macro)
		macro = re.sub(r'\?', r'[?]', macro)
		macro = re.sub(r'\+', r'[+]', macro)
		macro = macro + r"[\W]"
		replace = re.sub(r'\\', r'\\\\', replace)
		macros.append((macro,replace))

	# print("list macro protected:\n{}".format(macros))

	useful_macros = []

	# for (macro, replace) in macros:
	# 	match = re.search(macro, post_macro)
	# 	useful_macros.append((macro,replace))
	# 	post_macro = re.sub(macro, replace, post_macro)
	# 	print("macro: {}".format(macro))
	# 	print("replace: {}".format(replace))
	# 	print("new text:\n{}".format(post_macro))

	changed = True
	while changed:
		changed = False
		for (macro, replace) in macros:
			match = re.search(macro, post_macro)
			while match:
				useful_macros.append((macro,replace))
				changed = True
				match = re.search(macro, post_macro)
				post_macro = re.sub(macro, replace, post_macro)
				# print("macro: {}".format(macro))
				# print("replace: {}".format(replace))
				# print("new text:\n{}".format(post_macro))
	# print(post_macro)
	# print(useful_macros)

	final_macros = []
	text_macros = ""
	for (macro, replace) in useful_macros:
		macro = re.sub(r'\\\\', r'\\', macro)
		macro = macro[:-4]
		replace = re.sub(r'\\\\', r'\\', replace)
		if not (macro,replace) in final_macros:
			final_macros.append((macro,replace))
			text_macros = text_macros + r"\newcommand{" + macro + r"}{" + replace + "}\n"

	# print(text_macros)
	new_content = pre_macro + "\n```{math}\n" + text_macros + "```\n" + post_macro
	# print(new_content)

	g = open(path + file + ".md", "w")
	g.write(new_content)
	g.close()
