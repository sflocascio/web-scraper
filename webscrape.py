from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'http://www.carolinaparent.com/CP/Camp-Listings/'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#grabs each non featured camp 

contain  = page_soup.findAll("li",{"class":"premium listing"})

filename = "camps1.csv"
f = open(filename, "w")

headers = "camp_name, city, phone\n"

f.write(headers)

for container in contain:
    camp_name = container.div.h4.a.text

    contact_container = container.findAll("div",{"class":"contact"})
    # address_container = container.findAll("p",{"class":"address1"})
    city_container  = container.findAll("p",{"class":"city"})
    phone_container = container.findAll("p",{"class":"phone"})

    # camp_address = address_container[0].text
    camp_city_state_zip = city_container[0].text
    camp_phone = phone_container[0].text


    print("camp:" + camp_name)
    # print("address:" + camp_address)
    print("city:" + camp_city_state_zip)
    print("phone:" + camp_phone)

    f.write(camp_name + "," + camp_city_state_zip.replace(",", "|") + "," + camp_phone + "\n")