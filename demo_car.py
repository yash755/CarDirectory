import requests
from bs4 import BeautifulSoup
import csv
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time



url = "https://www.pistonheads.com/classifieds/used-cars#all"

# headers = {
#     'sec-ch-ua': "\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"",
#     'sec-ch-ua-mobile': "?0",
#     'upgrade-insecure-requests': "1",
#     'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
#     'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     'sec-fetch-site': "none",
#     'sec-fetch-mode': "navigate",
#     'sec-fetch-user': "?1",
#     'sec-fetch-dest': "document",
#     'cache-control': "no-cache",
#     'postman-token': "d4770229-660c-153e-0909-a8e1a7cca86f"
#     }
#
# response = requests.request("GET", url, headers=headers)
#
# html1 = BeautifulSoup(response.content, 'html.parser')


# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
#
# chrome_options = Options()
# # chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
# driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
#
# driver.get(url)
#
# html2 = driver.page_source
# html1 = BeautifulSoup(html2, "lxml", from_encoding="utf-8")


file = open('demo.html','r')



html1 = BeautifulSoup(file, 'html.parser')



divs = html1.find_all('div',{'class':'az-makerow grid grid-small'})



for div in divs:

    make_car = ''

    try:
        make = div.find('div',{'class':'col-1-4 az-make'})
        make = make.find('h4')

        make_car = make.text.strip()

    except:
        print("error")

    if make_car:
        try:
            model = div.find('div', {'class': 'col-3-4 az-models'})

            models = model.find_all('li')

            for li in models:
                model_car = li.text.strip()
                model_car = model_car.replace('\n','')
                model_car = model_car.split('(')
                print(model_car)
                model_car = model_car[0]


                model_car_a = li.find('a')
                model_car_a = model_car_a.get('href')
                print(make_car + '===' + model_car + '===' + model_car_a + '\n')
                cars = open('car.txt','a+')
                cars.write(make_car + '===' + model_car + '===' + model_car_a + '\n')
                cars.close()

        except:
            print("error")
