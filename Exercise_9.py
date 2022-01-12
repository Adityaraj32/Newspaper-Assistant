import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

# Type your personal api key 
apiKey = "cf21b1d84ba541bf9ef43b8097610211"

print("Categories are:\n\tBusiness(bu)\n\tEntertainment(en)\n\tHealth(he)\n\tScience(sc)\n\tSports(sp)\n\tTechnology(tec)")
categaryInput = input("Enter the Category: ")

categaryInput.lower()
if categaryInput == "bu":
    # urlData = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=cf21b1d84ba541bf9ef43b8097610211"
    urlData = f"https://newsapi.org/v2/top-headlines?sources=Moneycontrol&country=in&category=business&apiKey=cf21b1d84ba541bf9ef43b8097610211"
    urldataGet = requests.get(urlData).text
    urldatagetDict = json.loads(urldataGet)
    # articleName = urldatagetDict["articles"]
    # for articles in articleName:
        # print(articles['title'])
        # speak(articles['title'])
        # print("Moving onto nest news.Liten carefully")
        # speak("Moving onto nest news.Liten carefully")
    articles = urldatagetDict["articles"]
    for Moneycontrol in urldatagetDict:
        speak(articles["title"])
        print("Moving onto nest news.Liten carefully")
        speak("Moving onto nest news.Liten carefully")