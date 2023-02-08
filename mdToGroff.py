import sys
import re
import subprocess

f = open(sys.argv[1], "r")
groff = open(sys.argv[2], "w")
fileString = f.read()
f.close()

splitString = fileString.split("\n")

# groff file setup
groff.write(".nr HM 1\n")
curLine = 0
insideCode = False

# function to do checking for syntax

def code(curLine):
	curLine += 1
	codeString = ""
	while not splitString[curLine] == "```":
		codeString += splitString[curLine] + "\n"
		curLine += 1
	codeString = codeString.rstrip() # strip trailing newline
	fileName = "temp." + language
	f = open(fileName, "w")
	f.write(codeString)
	f.close()
	#result = subprocess.Popen(["highlight", "-O", "truecolor", fileName, "|", "groffhl"], stdout=subprocess.PIPE)
	ps = subprocess.run(["highlight", "-O", "truecolor", fileName], check=True, capture_output=True) # get highlighted code
	processNames = subprocess.run(["groffhl"], input=ps.stdout, capture_output=True) # convert to groff format with groffhl
	codeFormatted = processNames.stdout.decode('utf-8').strip() # get result as string
	codeFormatted = codeFormatted.replace("]\n", "]\n.br\n") # add line breaks in the code part to make it format properly
	# following code is to replace default highlight colours with my preffered colours
	codeFormatted = codeFormatted.replace("1.000000f", "0.169000f") # replace white with black
	codeFormatted = codeFormatted.replace("0.815686f 0.815686f 0.270588f", "0.000000f 0.000000f 1.000000f") # replace color of import
	codeFormatted = codeFormatted.replace("0.325490f 0.741176f 0.988235f", "0.000000f 0.502000f 0.000000f") # comments
	codeFormatted = codeFormatted.replace("0.058824f 0.576471f 0.058824f", "0.149000f 0.498000f 0.600000f") # name = value
	codeFormatted = codeFormatted.replace("0.411765f 0.780392f 0.537255f", "1.000000f 0.000000f 0.000000f") # null
	codeFormatted = codeFormatted.replace("0.901961f 0.298039f 0.901961f", "0.035000f 0.525000f 0.345000f") # numbers
	codeFormatted = codeFormatted.replace("0.776471f 0.254902f 0.776471f", "0.639000f 0.082000f 0.082000f") # string
	codeFormatted = codeFormatted.replace("0.972549f 0.819608f 0.819608f", "1.000000f 0.000000f 0.000000f") # newline
	
	groff.write(codeFormatted + "\n") # write to file

	

def check(x, curLine):
	global insideCode
	global language
	# check if line is a title
	if x[0] == "#":
		groff.write(".TL\n")
		groff.write(x[2:len(x)] + "\n")
		groff.write(".PP\n")
		
	# check for code blocks
	elif x[0:3] == "```":
		if insideCode:
			insideCode = False
		else:
			language = x[4:len(x)]
			language = language.lower()
			if language == "python":
				language = "py"
			if language == "haskell":
				language = "has"
			if language == "c++":
				language = "cpp"
			code(curLine)
			insideCode = True
	
	elif not insideCode:
		groff.write(".PP\n")
		groff.write(x + "\n")


for x in splitString:
	if not len(x) == 0:
		check(x, curLine)
	curLine += 1
		


groff.close()
pdfFileName = sys.argv[2] + ".pdf"
pdfOutput = subprocess.run(["groff", "-ms", "-Tpdf", sys.argv[2]], capture_output=True) # get highlighted code
pdf = pdfOutput.stdout
pdfFile = open(pdfFileName, "wb")
pdfFile.write(pdf)
pdfFile.close()