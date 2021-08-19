import requests
from bs4 import BeautifulSoup
import csv
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

file = open('car.txt','r')

for f in file:
    car_detail = f
    car_detail = car_detail.split('===')
    url = car_detail[2]

    print(url)

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

    response = requests.request("GET", url, headers=headers)

    html1 = BeautifulSoup(response.content, 'html.parser')

    a_tag = html1.find('a',{'class':'🏎3LSUxq 🏎24v-G6 🏎2t432k 🏎3SwFU2 🏎25tTC- 🏎36UD1o'})
    a_tag = a_tag.get('href')

    print(a_tag)

    cars = open('car1.txt', 'a+')
    cars.write(car_detail[0] + '===' + car_detail[1] + '===' + a_tag + '\n')
    cars.close()