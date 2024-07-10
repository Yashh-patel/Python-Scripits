import requests
from bs4 import BeautifulSoup

URL = "https://github.com/Yashh-patel"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

print("Get Header")
print(soup.head)

print("Get <p> of body")
print(soup.body.p)

print("Get children")
print(soup.body.find_all('p'))

print("DESCENDENTS")
# print(soup.body.descendants)
for descendent in soup.body.descendants:
    print(descendent)
    
print("Parent of head")
print(soup.head.parent)

print("Find tags for class= row no-gutters")
print(soup.find_all(attrs={"class":"row no-gutters"}))

#make me a list of all the motorcycle names in the webpage use coding, dont do it manually
print("Print all the motorcycles names")
# print(soup.body.h3)

motorcycle_names = []
for h3_tag in soup.find_all('h3'):
    name = h3_tag.get_text(strip = True)
    motorcycle_names.append(h3_tag.text)
    
for name in motorcycle_names:
    print(name)