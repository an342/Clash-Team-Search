import webbrowser
import codecs

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def MasteryLink(summoner, region):
  link = "https://championmasterylookup.derpthemeus.com/summoner?summoner=" + summoner.strip() + "&region=" + region
  return link

def OPLink(summoner, region):
  link = "https://" + region + ".op.gg/summoner/userName=" + summoner.strip()
  return link

def MOBALink(summoner, region):
  summoner.replace(" ", "%20")
  link = "https://app.mobalytics.gg/profile/" + region + "/" + summoner
  return link

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Variables
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

index = 0
regions = ["NA", "EUW", "EUNE","OCE", "KR", "TR", "LAN", "JP", "BR", "LAS", "LAN", "RU"]
sites = ["OP.gg [OP]", "Champion Mastery Lookup [CML]", "Mobalytics [MOBAL]"]
sites2use = []

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
chrome_path_NW = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --new-window"
#firefox_path = "C:\\Program Files\\Mozilla Firefox\\Firefox.exe"
controller = webbrowser.get(chrome_path)
controllerNW = webbrowser.get(chrome_path_NW)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Please update the names in 'Summoners.txt' now.")
input("Press Enter to continue...")

while True:
  print ("list of supported regions:")
  for i in regions:
    print(i)
  region = input("Please enter region : ")
  if region in regions:
    break
  else:
    continue
  
while True:
  print ("list of supported sites:")
  for i in sites:
    print(i)
  site = input("Please enter a desiired site or 'exit' to open pages: ")
  if site == "exit":
    break
  sites2use.append(site)
  print(sites2use)


f = codecs.open('Summoners.txt', encoding='utf-8')
lines = f.readlines()
f.close()

if "CML" in sites2use:
  for i in lines:
    if index == 0:
      controllerNW.open(MasteryLink(i, region))
    elif index > 0:
      controller.open(MasteryLink(i, region))
    index += 1

index = 0

if "OP" in sites2use:
  for i in lines:
    if index == 0:
      controllerNW.open(OPLink(i, region))
    elif index > 0:
      controller.open(OPLink(i, region))
    index += 1

index = 0

if "MOBAL" in sites2use:
  for i in lines:
    if index == 0:
      controllerNW.open(MOBALink(i, region))
    elif index > 0:
      controller.open(MOBALink(i, region))
    index += 1