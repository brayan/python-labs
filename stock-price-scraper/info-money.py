import requests
import bs4
  
text = "vale-vale3"
url = 'https://www.infomoney.com.br/cotacoes/b3/acao/' + text

result = requests.get(url)
  
soup = bs4.BeautifulSoup(result.text, "html.parser")
# print(soup)

span_objects = soup.find_all('div')

section = soup.find('div', attrs={'class':"value"})

texto = section.find_next('p').get_text(strip=True)
print(texto)


# for info in span_objects:
# 	print(info)
# 	print("------")