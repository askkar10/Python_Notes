# scrapping html data
# bs4
# pip install bs4
# load the text and create a beautiful group parser (bs4)
import bs4
html = open('test.html').read()
bs = bs4.BeautifulSoup(html,'html.parser')

a_list = bs('a')
print(a_list)
a_item = a_list[0]
print(a_item.text)
print(a_item['href'])
special_list = bs.select('.special')
print(special_list)
special_item = special_list[0]
print(special_item.text)
print(special_item['class'])