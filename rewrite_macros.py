import re

def match_next(s, open_parenthesis, closed_parenthesis, i=0, d=0):
	while (i < len(s)):
		if s[i:i + len(open_parenthesis)] == open_parenthesis:
		# if s.startswith(open_parenthesis, i):
			i += 1
			d += 1
		elif s[i:i + len(closed_parenthesis)] == closed_parenthesis:
		# elif s.startswith(closed_parenthesis, i):
			if d == 0:
				return i
			else:
				i += 1
				d -= 1
		else:
				i += 1
	return None

def rewrite_macros(path, file):
	f = open(path + file + ".md", "r")
	content = f.read()
	f.close()

	# print(content)
	
	# We're doing raisebox and scalebox here to avoid clashing with figures
	#### Rewrite raisebox 
	# \raisebox{-1pt}[0pt][0pt]{text}
	pattern = r'\\raisebox(\{.*?\})(\[.*?\])?(\[.*?\])?\{([\s\S]*?)$'
	match = re.search(pattern, content)
	while match:
		# print("\nRAISEBOX FOUND\n" + (match.group(0))[:100])
		(begin_eq,end_eq) = match.span()
		rest = match.group(4)
		end_eq = match_next(rest, '{', '}')
		new_eq = rest[:end_eq]
		# print("\nNEW EQ\n" + new_eq)
		content = content[:begin_eq] + new_eq + rest[end_eq+1:]
		# print("\nAFTER\n" + content[begin_eq-50:begin_eq + 50])
		match = re.search(pattern, content)

	# print(content)

	#### Rewrite scalebox
	# \scalebox{.5}{text}
	pattern = r'\\scalebox(\{.*?\})\{([\s\S]*?)$'
	match = re.search(pattern, content)
	while match:
		# print("\nSCALEBOX FOUND\n" + (match.group(0))[:100])
		(begin_eq,end_eq) = match.span()
		rest = match.group(2)
		end_eq = match_next(rest, '{', '}')
		new_eq = rest[:end_eq]
		# print("\nNEW EQ\n" + new_eq)
		content = content[:begin_eq] + new_eq + rest[end_eq+1:]
		# print("\nAFTER\n" + content[begin_eq-50:begin_eq + 50])
		match = re.search(pattern, content)


	##### REWRITING SIMPLE MACROS (no variables)
	list_macros = re.findall(r'\\(re)?newcommand{(.*?)}{(.*?)}\s', content)
	list_macros += re.findall(r'\\(pro)videcommand{(.*?)}{(.*?)}\s', content)

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
	for (x, macro, replace) in list_macros:
		macro = re.sub(r'\\', r'\\\\', macro)
		# Checking whether the next symbol is non-alphanumeric is to avoid prefixes (\col for \colouring)
		replace = re.sub(r'\\', r'\\\\', replace)
		macro += r"([\W_^])"
		replace += r"\1"
		macros.append(("_" + macro,"_" + replace))
		macros.append((r"\$" + macro,r"$" + replace))
		macros.append((macro," " + replace))

# Special cases:
# * \times\vertices: when replacing \vertices we replace by \times V: we need to introduce a space before
# * E_\colour: when replacing \colour we replace by E_c: we cannot introduce a space before
# We need to check in replace whether the character before is a _, in which case we don't introduce a space

	changed = True
	while changed:
		changed = False
		for (macro, replace) in macros:
			match = re.search(macro, post_macro)
			while match:
				changed = True
				post_macro = re.sub(macro, replace, post_macro)
				match = re.search(macro, post_macro)

	# print("list macro protected:\n{}".format(macros))

	##### REWRITING MACROS WITH PARAMETERS
	list_macros_param = re.findall(r'\\(re)?newcommand{(.*?)}\[(\d)\]{(.*?)}\s', content)
	list_macros_param += re.findall(r'\\(pro)videcommand{(.*?)}\[(\d)\]{(.*?)}\s', content)
	macros_param = []
	for (x, macro, number_param, replace) in list_macros_param:
		macro = re.sub(r'\\', r'\\\\', macro)
		# Checking whether the next symbol is non-alphanumeric is to avoid prefixes (\col for \colouring)
		macro += r"(?=\W)"
		replace = re.sub(r'\\', r'\\\\', replace)
		# print(replace)
		macros_param.append(("_" + macro, "_" + replace, int(number_param)))
		macros_param.append((r"\$" + macro, r"$" + replace, int(number_param)))
		macros_param.append((macro," " + replace, int(number_param)))

	# print(macros_param)
	changed = True
	while changed:
		changed = False
		for (macro, replace, number_param) in macros_param:
			match = re.search(macro, post_macro)
			while match:
				# print("post_macro", post_macro)
				print("macro", macro)
				print("replace", replace)
				print("number_param", number_param)
				changed = True
				(begin_match,end_match) = match.span()
				match = match.group(0)
				print("match", match)
				begin_rest = end_match + 1
				rest = post_macro[begin_rest:]
				instantiated_replace = replace
				for i in range(number_param):
					print("rest onwards", rest[:50])
					end_i = match_next(rest, '{', '}')
					repl_i = rest[: end_i]
					print("inside number", i, repl_i)
					repl_i = re.sub(r'\\', r'\\\\', repl_i)
					instantiated_replace = re.sub(r'#' + str(i+1), repl_i, instantiated_replace)
					begin_rest += end_i + 1
					print("instantiated_replace", instantiated_replace)
				post_macro = post_macro[:begin_match] + instantiated_replace + post_macro[begin_rest:]
				print("post_macro", post_macro)
				match = re.search(macro, post_macro)


	# print(existing_macro)
	new_list_macros = re.sub(r'\\(re)?newcommand\{.*?\}(\[\d\])?\{.*?\}\s', r'', existing_macro)
	new_list_macros = re.sub(r'\\providecommand\{.*?\}(\[\d\])?\{.*?\}\s', r'', new_list_macros)
	# print(new_list_macros)

	post_macro = re.sub(r'\\\\', r'\\', post_macro)

	match = re.search(r"macro", new_list_macros)
	if match:
		new_content = pre_macro + "\n```{math}\n" + new_list_macros + "```\n" + post_macro
	else:
		new_content = pre_macro + "\n" + post_macro		

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