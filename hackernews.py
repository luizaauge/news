import requests
from bs4 import BeautifulSoup
import csv

# Pega o conteúdo do URL usando o módulo requests e armazena o resultado na variável 'res'
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# res.text obtém a string e o analisador HTML converte o conteúdo da string em um soup object.
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# Uma vez que você tenha a variável soup, você pode trabalhar com .select nela.
# O .select retorna uma lista em Python de todos os elementos.
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')  # seleciona todos os elementos HTML que têm a classe subtext
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


# organiza a ordem dos dados obtidos
def mais_votadas(hnlista):
    return sorted(hnlista, key=lambda k: k['votes'], reverse=True)


# Extrai e armazena dados de acordo com as instruções
def create_custom_hn():
    # Criar top_items como uma lista vazia
    lista_hn = []
    # Extrai os valores dos atributos da mesma maneira que se extrai os valores de um dicionário, usando a função get.
    for idx, item in enumerate(mega_links):
        title = mega_links[idx].getText()
        href = mega_links[idx].get('href', None)
        vote = mega_subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ' '))
            if points > 99:
                # usa .append para adicionar esse dicionário na lista_hn
                lista_hn.append({'title': title, 'link': href, 'votes': points})
    return mais_votadas(lista_hn)

csv_columns = ['title', 'link', 'votes']
csv_file = "list_hn.csv"
try:
    with open(csv_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns, delimiter = ';')
        writer.writeheader()
        for data in create_custom_hn():
            writer.writerow(data)
            file.flush()
except IOError:
    print("I/O error")