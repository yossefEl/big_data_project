#!/usr/bin/python3
import data_scrapers.flipkart_scraper as fs
from sys import argv,exit

if len(argv) ==1:
    print('Please enter a keyword or enter ./main.py -h to get help')
elif len(argv)==2 and argv[1]=='-h':
    print('-s for the keyword:\n\t usage: ./main.py -s "keyword here"')
    print('-o for the output:\n\t usage: ./main.py -o "filename"')
    print('-l for the limit number of pages scrapped:\n\t usage: ./main.py -l number')
elif len(argv)==3 and argv[1]=='-s':
    print('hellllllll')
    if argv[2] == None :
        print('please enter a keyword as follows : main.py -s keyword')
    else:
        keyword=argv[2]
        fs.scrape(keyword=keyword,filename='data')
elif len(argv)==5:
    if argv[1] == '-s': 
        if argv[2]!= None:
            keyword=argv[2]
        else: 
            print('please enter a keyword as follows : ./main.py -s keyword')
            
    if argv[3] == '-o':
        if argv[4]!= None:
            output=argv[4]
            #start scraping 
            fs.scrape(keyword=keyword,filename=output)
        else :
            output="data"
            #start scraping 
            fs.scrape(keyword=keyword,filename=output)
elif len(argv)==7:
    if argv[1] == '-s': 
        if argv[2] != None:
            keyword=argv[2]
            print('please enter a keyword as follows : main.py -s keyword')
        else: sys.exit
    if argv[3] == '-o':
        if argv[4]!= None: 
            output=argv[4]
        else : 
            output="data"
    if argv[5] == '-l':
        if argv[6]!= None: 
            limit=argv[6]
            #start scraping 
            fs.scrape(keyword=keyword,filename=output,limit=limit)
        else :
            print('limits could not be empty: please specify a limit of number of pages')
            sys.exit


    
        




