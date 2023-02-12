# Programs and Stuff

## Log.py

Every day run the program and enter information about the day.

### Setup

Open log.py and change the directory on lines `24, 75 and 107` to your own preffered directory. 

Optionally create an alias:  
`echo "alias log='python3 ~/Programs/My-Programs/log.py'" >> ~/.bashrc`

### Usage

New entry:  
`python3 log.py`

Lookup specific date:  
`python3 log.py -d yymmdd`

Lookup specific term:  
`python3 log.py -s SearchTerm yy`  
or  
`python3 log.py -s SearchTerm yymm`

Program will automatically add results to yesterday if run before 1300. 

## mdToGroff.py

Script to convert a standard markdown file to a groff file and then compile it into a pdf.  
Usage: `python3 mdToGroff.py input.md output.pdf`

Very WIP, so far only titles, paragraphs and code blocks are working. 
