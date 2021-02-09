import os 

os.chdir('.') 
print(os.getcwd()) 

def rename_main_into_index():
	for f in os.listdir('.'):
		if f == "main.tex":
			os.rename(f, "index.tex")
		if os.path.isdir(f):
			os.chdir(f)
			rename_main_into_index()
			os.chdir('./..') 

rename_main_into_index()