import bs4
html = open('test.html').read()
bs = bs4.BeautifulSoup(html,'html.parser')
a_list = bs('a')
print(a_list)
print(a_list[0])
print(a_list[0].text)
print(a_list[0]['href'])

special = bs.select('.special')
print(special)
print(special[0])
print(special[0].text)
print(special[0]['class'])