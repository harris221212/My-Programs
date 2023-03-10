# Programs and Stuff

## Log.py

Every day run the program and enter information about the day.

### Setup

Open log.py and change the directory on lines `24, 75 and 107` to your own preffered directory. 

Optionally create an alias:  
`echo "alias log='python3 ~/Programs/myPrograms/log.py'" >> ~/.bashrc`

### Usage

New entry:  
`python3 log.py`

Lookup specific date:  
`python3 log.py -d yymmdd`

Lookup specific term:  
`python3 log.py -s SearchTerm yy`  
or  
`python3 log.py -s SearchTerm yymm`

Program will automatically add results to yesterday if run before 1400.  
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
Map `rofiA.py` and `rofiB.py` to keyboard shortcuts. `rofiA.py` is used to set new bookmarks and `rofiB.py` is used to access bookmakrs, so I have mapped `rofiA.py` to `Super+Shift+V` and `rofiB.py` to `Super+V`

### Usage

To add bookmark, run `rofiA.py` and paste in the text you want to save.  
To access bookmark, run `rofiB.py` and press `Enter` over desired text. It will be copied to the clipboard.  
To remove bookmark, press `Alt+w` to remove selected bookmark.  


## appleMusic.py

Used to download album art from Apple Music in high quality. 

### Setup

`pip3 install requests`  
Install aria2c

### Usage

`python3 appleMusic.py link artist_name`  
The link should be a link to either an an artists albums page, or ep/singles page. (e.g. LINK or LINK)

The output will be a `.sh` file. `chmod +x toDownload.sh` to make excecutable, and then run it. 

## musicCSV.py 

WIP, used to get a csv file of song data from an artists Wikipedia songs page (i.e. pages like this: LINK)

### Setup

`pip3 install pandas requests`

### Usage

`python3 musicCSV.py link artist_name`

## podcasts.py\sh

Used to download all podcasts from an RSS feed

### Usage

`./podcasts.sh rss.xml`
