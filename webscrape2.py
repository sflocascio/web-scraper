from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#PAGE 4 of CAMP LISTINGS SECTION - Carolina Parent 
my_url = 'http://www.carolinaparent.com/CP/Camp-Listings/index.php/cp/4/si/150/'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#grabs each non featured camp 

contain  = page_soup.findAll("li",{"class":"free listing"})

filename = "camps2.csv"
f = open(filename, "w")

headers = "camp_name, city, phone\n"

f.write(headers)

for container in contain:
    camp_name = container.div.h5.a.text

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