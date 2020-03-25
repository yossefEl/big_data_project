import requests
from bs4 import BeautifulSoup
import lxml
import csv
from data_scrapers import flipkart_scraper as fs
from sys import argv,exit

if len(argv) ==0:
    print('Please enter a keyword or enter main.py -h to get help')
elif len(argv)==1 and argv[0]=='-h':
    print('-s for the keyword:\n\t usage: main.py -s "keyword here"')
    print('-o for the output:\n\t usage: main.py -o "filename"')
    print('-l for the limit number of pages scrapped:\n\t usage: main.py -l number')
elif len(argv)==2 and argv[0]=='-s':
    if argv[1] is None :
        print('please enter a keyword as follows : main.py -s keyword')
    else:
        keyword=argv[1]
elif len(argv)==4:
    if argv[0] is '-s': 
        if argv[1] is not None:
            keyword=argv[1]
            fs.scrape(keyword=keyword,filename='data')
        else: 
            
            print('please enter a keyword as follows : main.py -s keyword')
            sys.exit
    if argv[2] is '-o':
        if argv[3] is not None:
            output=argv[3]
            #start scraping 
            fs.scrape(keyword=keyword,filename=output)
        else :
            output="data"
            #start scraping 
            fs.scrape(keyword=keyword,filename=output)
elif len(argv)==6:
    if argv[0] is '-s': 
        if argv[1] is not None:
            keyword=argv[1]
            print('please enter a keyword as follows : main.py -s keyword')
        else: sys.exit
    if argv[2] is '-o':
        if argv[3] is not None: 
            output=argv[3]
        else : 
            output="data"
    if argv[4] is '-l':
        if argv[5] is not None: 
            limit=argv[3]
            #start scraping 
            fs.scrape(keyword=keyword,filename=output,limit=limit)
        else :
            print('limits could not be empty: please specify a limit of number of pages')
            sys.exit


    
        




