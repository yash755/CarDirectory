import requests
from bs4 import BeautifulSoup
import csv
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from dateutil.parser import parse
import csv
file = open('car1.txt','r')

for f in file:
    car_detail = f
    car_detail = car_detail.replace('\n','')
    car_detail = car_detail.split('===')
    url = car_detail[2]

    page = 1

    while True:

        url_href = url + '&page=' + str(page)
        print(url_href)

        headers = {
            'sec-ch-ua': "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
            'sec-ch-ua-mobile': "?0",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'sec-fetch-site': "none",
            'sec-fetch-mode': "navigate",
            'sec-fetch-user': "?1",
            'sec-fetch-dest': "document",
            'cache-control': "no-cache",
            'postman-token': "d4770229-660c-153e-0909-a8e1a7cca86f"
        }

        response = requests.request("GET", url_href, headers=headers)

        html1 = BeautifulSoup(response.content, 'html.parser')

        results = html1.find_all('div',{'class':'result-contain'})

        if len(results) > 0:
            for result in results:

                car_name = ''
                model = car_detail[0]
                make = car_detail[1]
                year = ''
                price = ''
                miles = ''
                petrol = ''
                automatic = ''
                power = ''

                try:
                    headline = result.find('h3')
                    headline = headline.text.strip()
                    headline = headline.rsplit('(', 1)

                    if len(headline) >= 1:
                        car_name = headline[0]

                    if len(headline) >= 2:
                        year = headline[1]
                        year = year.replace(')','')

                except:
                    print("Headlue Error")

                try:
                    price_res = result.find('div',{'class':'price'})
                    price = price_res.text.strip()

                except:
                    print("Price Error")

                try:
                    ul = result.find('ul',{'class':'specs'})
                    lis = ul.find_all('li')

                    for li in lis:
                        li_str = str(li)

                        if miles == '':
                            if 'flaticon solid gauge-1' in li_str:
                                miles = li.text.strip()

                        if petrol == '':
                            if 'flaticon solid gas-1' in li_str:
                                petrol = li.text.strip()

                        if automatic == '':
                            if 'flaticon solid location-pin-4' in li_str:
                                automatic = li.text.strip()

                        if power == '':
                            if 'flaticon solid battery-charging-3' in li_str:
                                power = li.text.strip()

                except:
                    print(" Li Error")

                if car_name:
                    temp = []
                    temp.append(car_name)
                    temp.append(model)
                    temp.append(make)
                    temp.append(year)
                    temp.append(price)
                    temp.append(miles)
                    temp.append(petrol)
                    temp.append(automatic)
                    temp.append(power)
                    print(temp)

                    arr = []
                    arr.append(temp)

                    with open('main.csv', 'a+') as csvfile:
                        csvwriter = csv.writer(csvfile)

                        # writing the data rows
                        csvwriter.writerows(arr)

            page = page + 1

        else:
            break


