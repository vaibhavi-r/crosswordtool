# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:47:04 2016
This is a first attempt at a Webscrapingtool to access Cryptic Guardian Crosswords :D
@author: Vibes
"""

from lxml import html
import requests


#User Introduction
intro= """This is a first attempt at a Webscraping tool   :)

What does that mean?:
---------------------
1. User inputs how many cryptic crosswords they want.
2. Program fetches that many crosswords from 23rd December (Number-27075) going backward 
3. Program outputs the the clues, and also which cells are blocked in the 15x15 Grid
4. No graphical output yet. Crossword cells are numbered like in Excel(Rows- number, Columns- Alphabet)
--------------------------------------------------------------------------------------------
"""
print intro




numOfXwords = input("So, how many crosswords do you need? : ")
baseUrl= "https://www.theguardian.com/crosswords/accessible/cryptic/"
crosswordId=27075; 


for count in range (0, numOfXwords):    
    #Access the relevant URL for crosswords
    page = requests.get(baseUrl+str(crosswordId-count))
    tree = html.fromstring(page.content) 
    #Need to use page.content instead of page.text becuase html.fromstring implicitly expects bytes as input

    blankLines = tree.xpath('//div[@class="crossword__accessible-data"]/ul/li/span/text()')
    blankCells = tree.xpath('//div[@class="crossword__accessible-data"]/ul/li/text()')
    cluesAcross= tree.xpath('//div[@class="crossword__clues--across"]/ol/li/text()')
    cluesDown= tree.xpath('//div[@class="crossword__clues--down"]/ol/li/text()')
    

    print '\n\nGuardian Cryptic Crossword Number :', crosswordId-count  
    print 'URL : ', baseUrl+str(crosswordId-count)
    print '\nACROSS : '
    for clue in cluesAcross:
        print clue
    print '\nDOWN : '
    for clue in cluesDown:
        print clue
    print '\nBLANKS : '    
    for line, cells in zip(blankLines,blankCells):
        line = line, cells
        print line  
    
    print "---------------------------------------------------------------------"


"""                
WAYS TO EXPAND & IMPROVE:
   A) CODE: (Maximize Learning)
     Combine lists (Blanks: line nums & Cells) into single informative column - DONE
     Create a Class for each crossword (crosswordID, date, blankLines, blankCells, and clues : Across, Down)
     Logic to fetch latest crossword number for Guardian instead of static
     Add ML - Predict Difficulty/Easiness of crossword,
     Draw a crossword with python libraries given blank cells
    
   B) FUNCTIONALITY: (Maximize Usability )
     Get multiple crosswords at once - DONE
     Give choice of Cryptic / Quick Crossword to user      
     Print the output crosswords into a text file
     Add solution sets along with the crossword
"""    
    
    


