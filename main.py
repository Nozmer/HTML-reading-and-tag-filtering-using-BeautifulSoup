from bs4 import BeautifulSoup
import requests

link = "https://www.undp.org/pt/brazil/idhm-munic%C3%ADpios-2010"
data = requests.get(link).text

soup = BeautifulSoup(data, "html.parser")
data = soup.find_all('td')

infoData = []

Município = []
IDHM = []
IDHMRenda = []
IDHMLongevidade = []
IDHMEducação = []

for data in soup.find_all('td'):
    infoData += [data.text]

for x in range(len(infoData)):
    if x % 6 == 0:
        Município += [(infoData[1 + x])]
        IDHM += [(infoData[2 + x])]
        IDHMRenda += [(infoData[3 + x])]
        IDHMLongevidade += [(infoData[4 + x])]
        IDHMEducação += [(infoData[5 + x])]

print("Total: " + str(len(Município)))
print(Município)
