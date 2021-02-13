import subprocess

list_command = [\
"python chapter_transformer.py 1 Introduction 1_Introduction/",\
"python chapter_transformer.py 2 Regular 2_Regular/",\
"python chapter_transformer.py 3 Parity 3_Parity/",\
"python chapter_transformer.py 4 Payoffs 4_Payoffs/"\
]

for chap in list_command:
	subprocess.call(chap, shell=True)
