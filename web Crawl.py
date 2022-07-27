import urllib.request as url
import bs4,lxml

home_path ="https://www.news18.com/"
print('''
Press 1 for Politics
Press 2 for India
Press 3 for World
Press 4 for Education
''')
choice = input("Enter Catagory : ")

if choice=='1':
    path = home_path+"politics"
    response = url.urlopen(path)
    data = bs4.BeautifulSoup(response,'lxml')
    #news=data.find("h3",class_="jsx-3328680553")
    news = data.find("div",class_="jsx-3328680553 top_story_right")
    news = news.findAll("h3")
    for i in range(0,len(news)):
        print(f"=>   {news[i].text}")

    
