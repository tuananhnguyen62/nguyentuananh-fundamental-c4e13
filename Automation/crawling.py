from urllib.request import urlopen
from bs4 import BeautifulSoup
#download html content
website = urlopen("http://dantri.com.vn")
html_content = website.read().decode('utf-8')
website.close()

#create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
ul_news = soup.find('ul', 'ul1 ulnew')
li_news_list = ul_news.find_all('li')

for li in li_news_list:
    a_detail = li.h4.a
    title = a_detail['title'] #Attribute
    content = a_detail.string
    # print(title)
    print(content)
    print("*" * 20)
