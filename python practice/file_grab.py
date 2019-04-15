import os, glob

os.chdir("E:\images")
for file in glob.glob("*.jpg"):
	print(file)