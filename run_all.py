import subprocess

list_command = [\
"python run.py 1 Introduction Introduction/",\
"python run.py 2 Regular Classic/2_Regular/",\
"python run.py 3 Parity Classic/3_Parity/",\
"python run.py 4 Payoffs Classic/4_Payoffs/"\
]

for chap in list_command:
	subprocess.call(chap, shell=True)
