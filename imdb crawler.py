import urllib.request as url
import bs4,lxml

home_path = "https://www.imdb.com/"\

movie_name = input("Enter Movie Name : ")
movie_name = movie_name.replace(" ","+")
#movie search page
path="https://www.imdb.com/find?q="+movie_name
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
td = data.find("td",class_="result_text")
a_href = td.find('a')['href']
#movie Page
path = home_path+a_href
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
h1 = data.find("h1",class_="sc-b73cd867-0 eKrKux")
print(f"Movie Name => {h1.text}")
date = data.find("span",class_="sc-8c396aa2-2 itZqyK")
print(f"Movie Release Date =>{date.text}")
span = data.find("span",class_="sc-7ab21ed2-1 jGRxWM")
print(f"Rating => {span.text}/10.0")

div= data.find("div",class_="sc-66a20916-0 lQXVY")
a_href= div.find("a")["href"]

#Review Page
path = home_path+a_href
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
a_list = data.findAll("a",class_="title")
for i in range(len(a_list)):
    a_list[i]=a_list[i].text.replace("\n","")
    print(f"{i+1}. {a_list[i]}")
