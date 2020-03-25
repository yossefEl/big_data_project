import requests
from bs4 import BeautifulSoup
import lxml
import csv
import sys



def scrape(keyword):
    print(keyword)
    with open('data.csv', mode='w') as csv_file:
        fieldnames = ['productName', 'priceInDollar', 'rating', 'numberOfRates']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    url = 'https://www.flipkart.com/search?q=' + keyword.replace(
        ' ', '+'
    ) + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent':
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    pages = soup.find_all("div", class_="_2zg3yZ")
    if len(pages)!=0:
        numberOfPages = pages[0].span.text.split(" ")
        numberOfPages = numberOfPages[3].replace(",", '')
    else:
        print('No products found')
        sys.exit()
    print(numberOfPages)

    # for pageNumber in range(1,int(numberOfPages)+1):
    for pageNumber in range(1, int(numberOfPages) + 1):
        url2 = url + "&page=" + str(pageNumber)
        result = requests.get(url2)
        soup = BeautifulSoup(result.content, "lxml")
        titles = soup.find_all("a", title=True, class_="_2cLu-l")
        ratings = soup.find_all("div", class_="hGSR34")
        numberRaters = soup.find_all('span', class_='_38sUEc')
        prices = soup.find_all("div", class_="_1vC4OE")

        print(len(numberRaters))
        for index in range(len(titles)):
            title = titles[index]['title'].strip('\"')
            price = round(
                float(prices[index].text.replace('₹', '').replace(',', '')) /
                76.27, 2)
            if index < len(numberRaters):
                ratersNB = numberRaters[index].text.replace('(', '').replace(
                    ')', '')
                rating = ratings[index].text
            else:
                ratersNB = 0
                rating = 0

            with open('data.csv', mode='a') as csv_file:
                fieldnames = [
                    'productName', 'priceInDollar', 'rating', 'numberOfRates'
                ]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({
                    'productName': title,
                    'priceInDollar': price,
                    'rating': rating,
                    'numberOfRates': ratersNB
                })

                # writerow= csv.writer(csv_file)
