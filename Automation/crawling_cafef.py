from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
website = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content = website.read().decode('utf-8')
website.close()

#create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

#tìm thẻ table rồi tìm thẻ tbody
tbody = soup.find('table', id='tableContent')
#tìm find all các thẻ tr
tr_list = tbody.find_all('tr')
# print(tr_list)

#tìm find all các thẻ td
data_list = []

for tr in tr_list:
    # print(tr)
    # print("*" *20)
    td_list = tr.find_all('td')
    data = {}
    for index, td in enumerate(td_list):
        content = td.string
        if content != None:
            if index == 0:
                data['title'] = content.strip()
            elif index == 1:
                data['Quy 4 - 2016'] = content
            elif index  ==   2:
                data['Quy 1 - 2017'] = content
            elif index == 3:
                data['Quy 2 - 2017'] = content
            else:
                data['Quy 3 - 2017'] = content
            # print(content.strip())
    if data != {}:
        data_list.append(data)
# print(data_list)
pyexcel.save_as(records=data_list, dest_file_name="cafef.xls")
