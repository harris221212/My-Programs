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
If you make a mistake, just re-run the program and it will overwrite the current days data. 

## mdToGroff.py

Script to convert a standard markdown file to a groff file and then compile it into a pdf.  
Usage: `python3 mdToGroff.py input.md output.pdf`

Very WIP, so far only titles, paragraphs and code blocks are working. 

## rofiA/B.py

Very simple bookmarking program using rofi

### Setup

`pip3 install pyperclip3 python-rofi`

Change path in files to where ever you want the bookmarks to be stored.  
Map `rofiA.py` and `rofiB.py` to keybaord shortcuts. `rofiA.py` is used to set new bookmarks and `rofiB.py` is used to access bookmakrs, so I have mapped `rofiA.py` to `Super+Shift+V` and `rofiB.py` to `Super+V`
