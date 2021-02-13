import re

def bib_transformer(nb_chap):
	f = open("chap" + nb_chap + ".bib", "r")
	content = f.read()
	f.close()

	content = re.sub(r'\n(.*?)([aA]uthor)(.*?)=(.*?,\n)', r'\n\1\2\3=\4\1chap\3  = {' + nb_chap + r'},\n', content)

	return(content)

# bib_transformer("1")
