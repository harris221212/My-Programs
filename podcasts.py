import sys

inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "w")

fullXML = inputFile.read()
inputFile.close()

splitXML = fullXML.split("\"")
beforeString = "enclosure url"
i = 0

for currentString in splitXML:
	i += 1
	if beforeString in currentString:
		outputFile.write(splitXML[i] + "\n")
outputFile.close()
