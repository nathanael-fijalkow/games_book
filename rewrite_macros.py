import re

def rewrite_macros(path, file):
	f = open(path + file + ".md", "r")
	content = f.read()
	f.close()

	# print(content)
	
	list_macros = re.findall(r'\\newcommand{(.*?)}{(.*?)}\s', content)

	match = re.search(r'```{math}([\s\S]*?)```', content)
	(begin_macro,end_macro) = match.span()
	pre_macro = content[:begin_macro]
	existing_macro = match.group(1) 
	post_macro = content[end_macro:]

	# print("text macros:\n{}".format(existing_macro))
	# print("list macros unprotected:\n{}".format(list_macros))
	# print("text before the macros:\n{}".format(pre_macro))
	# print("text after the macros:\n{}".format(post_macro))

	macros = []
	for (macro, replace) in list_macros:
		macro = re.sub(r'\\', r'\\\\', macro)
		macro = re.sub(r'\?', r'[?]', macro)
		macro = re.sub(r'\+', r'[+]', macro)
		# Checking whether the next symbol is non-alphanumeric is to avoid prefixes (\col for \colouring)
		replace = re.sub(r'\\', r'\\\\', replace)
		macro += r"([\W_^])"
		replace += r"\1"
		macros.append(("_" + macro,"_" + replace))
		macros.append((r"\$" + macro,r"$" + replace))
		macros.append((macro," " + replace))

# \times\vertices: when replacing \vertices we replace by \times V: we need to introduce a space before
# E_\colour: when replacing \colour we replace by E_c: we cannot introduce a space before
# We need to check in replace whether the character before is a _, in which case we don't introduce a space

	# print("list macro protected:\n{}".format(macros))

	##### Rewrite macros with one parameter
	list_macros1 = re.findall(r'\\newcommand{(.*?)}\[1\]{(.*?)}\s', content)
	macros1 = []
	for (macro, replace) in list_macros1:
		macro = re.sub(r'\\', r'\\\\', macro)
		macro = re.sub(r'\?', r'[?]', macro)
		macro = re.sub(r'\+', r'[+]', macro)
		macro += r"\{([\s\S]*?)\}"
		# Checking whether the next symbol is non-alphanumeric is to avoid prefixes (\col for \colouring)
		replace = re.sub(r'\\', r'\\\\', replace)
		replace = re.sub(r'#1', r'\\1', replace)
		# print(replace)
		macros1.append(("_" + macro,"_" + replace))
		macros1.append((r"\$" + macro,r"$" + replace))
		macros1.append((macro," " + replace))

	##### Rewrite macros with two parameters
	list_macros2 = re.findall(r'\\newcommand{(.*?)}\[2\]{(.*?)}\s', content)
	macros2 = []
	for (macro, replace) in list_macros2:
		macro = re.sub(r'\\', r'\\\\', macro)
		macro = re.sub(r'\?', r'[?]', macro)
		macro = re.sub(r'\+', r'[+]', macro)
		macro += r"\{([\s\S]*?)\}\{([\s\S]*?)\}"
		# Checking whether the next symbol is non-alphanumeric is to avoid prefixes (\col for \colouring)
		replace = re.sub(r'\\', r'\\\\', replace)
		replace = re.sub(r'#1', r'\\1', replace)
		replace = re.sub(r'#2', r'\\2', replace)
		# print(replace)
		macros2.append(("_" + macro,"_" + replace))
		macros2.append((r"\$" + macro,r"$" + replace))
		macros2.append((macro," " + replace))

	##### Rewrite macros with three parameters
	list_macros3 = re.findall(r'\\newcommand{(.*?)}\[2\]{(.*?)}\s', content)
	macros3 = []
	for (macro, replace) in list_macros3:
		macro = re.sub(r'\\', r'\\\\', macro)
		macro = re.sub(r'\?', r'[?]', macro)
		macro = re.sub(r'\+', r'[+]', macro)
		macro += r"\{([\s\S]*?)\}\{([\s\S]*?)\}\{([\s\S]*?)\}"
		# Checking whether the next symbol is non-alphanumeric is to avoid prefixes (\col for \colouring)
		replace = re.sub(r'\\', r'\\\\', replace)
		replace = re.sub(r'#1', r'\\1', replace)
		replace = re.sub(r'#2', r'\\2', replace)
		replace = re.sub(r'#3', r'\\3', replace)
		# print(replace)
		macros3.append(("_" + macro,"_" + replace))
		macros3.append((r"\$" + macro,r"$" + replace))
		macros3.append((macro," " + replace))

	# Rewrite macros in the file

	all_macros = macros + macros1 + macros2 + macros3
	changed = True
	while changed:
		changed = False
		for (macro, replace) in all_macros:
			match = re.search(macro, post_macro)
			while match:
				changed = True
				post_macro = re.sub(macro, replace, post_macro)
				match = re.search(macro, post_macro)

	new_list_macros = re.sub(r'\\newcommand\{.*?\}(\[\d\])?\{.*?\}\s', r'', existing_macro)

	# # Rewrite macros in the remaining macros
	# changed = True
	# while changed:
	# 	changed = False
	# 	for (macro, replace) in all_macros:
	# 		# print(macro)
	# 		match = re.search(macro, new_list_macros)
	# 		while match:
	# 			changed = True
	# 			new_list_macros = re.sub(macro, replace, new_list_macros)
	# 			match = re.search(macro, new_list_macros)

	# print("new\n" + new_list_macros)

	new_content = pre_macro + "\n```{math}\n" + new_list_macros + "```\n" + post_macro

	# Last cleanup: remove consecutive line breaks
	match = re.search(r'\s*?\n\s*?\n\s*?\s*?\n', new_content)
	while match:
		new_content = re.sub(r'\s*?\n\s*?\n\s*?\s*?\n', r'\n\n', new_content)
		match = re.search(r'\s*?\n\s*?\n\s*?\s*?\n', new_content)		

	# print(new_content)

	g = open(path + file + ".md", "w")
	g.write(new_content)
	g.close()

# rewrite_macros("5_MDP/", 'notations')