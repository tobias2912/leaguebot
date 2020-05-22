from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
commands=["build", "update", "counter"]
abbriviations={"Blade of the Ruined King":"BORK", "Guardian Angel":"GA", "The Black Cleaver": "Black Cleaver", "Rabadon's Deathcap":"Rabadon's", "Zhonya's Hourglass":"Zhonya"}
allChampions=[]

def updateChampions():
    fil = open("champs.txt")
    champs=[]
    for l in fil.read().split('\n'):
        if l != "":
            champs.append(l.lower())
            allChampions.append(l.lower())
    #liste=champs
    print("finished reading ",len(allChampions), "champions")

updateChampions()

def init(string):
    words = string.split()
    command = words[0]
    if command in commands:
        if command=="build":
            if len(words)==0:
                raise AssertionError("incorrect length")
            return getBuild(words[1:])
        if command=="update":
            updateChampions()
            return "updated"
        if command=="counter":
            if len(words)==0:
                raise AssertionError("incorrect length")
            return getCounter(words[1:])

    else:
        return ""

def getBuild(champ):
    originalChamp=getchampname(champ[0])
    soup = getSoup(originalChamp)
    res = soup.find_all('span', class_='rb-item-img-text obt-css')
    items = []
    for r in res:
        item = r.text
        print(item)
        if item in abbriviations:
            items.append(abbriviations[item])
        else:
            items.append(item)
    string = ', '.join(items)
    if items != []:
        return originalChamp+" build: "+string
    else:
        raise AssertionError("found no items")

def getCounter(champ):
    originalChamp=getchampname(champ[0])
    soup = getSoup(originalChamp)
    res = soup.find("div", class_="counters-sidebar-strong-against")
    items = []
    for r in res:
        item = r.text
        items.append(item)
    items.pop(0)
    string = ', '.join(items)
    if items != []:
        return originalChamp+" counters: "+string
    else:
        raise AssertionError("found no items")

def getchampname(input):
    for champ in allChampions:
        if champ.startswith(input):
            return champ
    raise AssertionError("no mathcing champions on "+input)

def getSoup(champ):
    champ=champ.replace(" ","-").replace("'", "-")
    url = "https://rankedboost.com/league-of-legends/build/"+champ
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    return BeautifulSoup(html, 'html.parser')