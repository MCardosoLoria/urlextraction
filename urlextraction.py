## Extract all urls and put them in a list called URLS

from bs4 import BeautifulSoup
import requests
import pandas as pd

## Extract all emails and names from each url and upload them to a .csv

urls = pd.read_csv("facebook.com_27th_Feb_2024 (1).csv")

for url in urls:
    response = requests.get(url)
    age_content = response.text
    doc = BeautifulSoup(response.text, 'html.parser')  ## Parse (convert the information into something easier to work with) the HTML using beautiful soup



def get_shop_names():
    selection_class = "x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz"
    shop_name_tags = doc.find_all('h1',{'class':selection_class})
    shop_names = []

    for tag in shop_name_tags:
        shop_names.append(tag)

    return shop_names


def get_shop_emails():
    selection_class = "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h"
    shop_email_tags = doc.find_all('span',{'class':selection_class})
    shop_emails = []

    for tag in shop_email_tags:
        shop_emails.append(tag)

    return shop_emails

def all_urls():

    shop_dict = {
        'Names':[],
        'Emails':[],
    }

    names = get_shop_names()
    emails = get_shop_emails()

    for i in names:
        shop_dict['Names'].append(names[i])
        shop_dict['Emails'].append(emails[i])

    return pd.DataFrame(shop_dict)


shops = all_urls()


shops.to_csv(r'Copywriting\shops.csv', index = None, encoding = 'utf-8')




