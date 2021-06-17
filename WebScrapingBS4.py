import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"

# Step1: get the HTML
r = requests.get(url)
htmlContent = r.content

soup  = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)
title = soup.title

# print(title)
# print(type(soup)) #BeautfilSoup
# print(type(title)) #Tag
# print(type(title.string)) #NavigableString

#get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

anchors = soup.find_all('a')
# print(anchors)

# print(htmlContent)

# print(soup.find('p')) #Gives the first para
# print(soup.find('p')['class']) #Gives ['lead', 'text-muted'] i.e classes of the first element

# find all the elements with class lead
# print(soup.find_all("p",class_="lead")) #Gives a list of p tags with class lead

#Get the texts from the elements/tags/soups
# print(soup.find('p').get_text()) #As soup.find('p') gives the first p. We will get the text in first p tags


# Get all the links on the page(i.e getting href of anchor tags)
all_links = set()
for link in anchors:
    if(link.get('href')!='#'):
        linktext = "https://www.codewithharry.com"+link.get('href')
        all_links.add(linktext)
        # print(linktext)

#Suppose there is a div with id as navbarSupportedContent then we can get it by using line just below and then we can
#Iterate through all its items like whatever is inside this div using the latter two lines using .contents method
navbarContent = soup.find(id='navbarSupportedContent')
# for elem in navbarContent.children: also works
for elem in navbarContent.contents:
    print(elem)

#this will only print the strings/innerHTML
for elem in navbarContent.strings:
    print(elem)

print(navbarContent.parent) #WIll print the parent of the div class
#For example if
# div class="p1"
#     div id="navbarContent"
# Then we will get div p1 as the parent

for p in navbarContent.parents:
    print(p.name)#Getting the complete tree of parents


# Getting the previous and next sibling
#If there is no next or previous sibling it will print none
#Reminder:Spaces are considered as siblings
# print(navbarContent.next_sibling)
# print(navbarContent.previous_sibling)
# print(navbarContent.next_sibling.next_sibling) #This also works to get the sibling next to next sibling


#CSS selectors
elem = soup.select('#loginModal')
print(elem)
# To get elem using class
# elem2 = soup.select('.class_name')
# print(elem2)
