#Created June 9 2020 by Swayam Parekh.

#imports all modules - $pip install
import requests
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import ssl
import wikipedia
import webbrowser
import subprocess
import PySimpleGUI as sg
sg.theme('DarkBlue14')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Enter'), sg.Button('Sleep')]]
UIWindow = sg.Window('Jarvis UI', layout)
#ssl._create_default_https_context = ssl._create_unverified_context #<-- used to bypass security features on Mac, I normally comment this out so that the certificate system works normally when I'm not using the program

#calls necessary lists that are used in functions

#list stores common responses for yes or no to work for almost every logical response imaginable
yesList = ["yes", "yeah", "yuh", "yea", "yas", "y","ya", "sure", "of course", "mhm", "why not", "ok", "okay", "yup"]
noList = ["no", "nah", "nuh-uh", "nope", "n", "not right now", "later", "maybe later", "can't"]

#initiallizes the text to speech system that enables Jarvis to talk. From the documentation 
engine = pyttsx3.init()
def say(audio):
    engine.say(audio)
    engine.runAndWait()
    

def lamejokes():
    #jokes are randomly generated from a bank, normally these would be in a files and then appended to the jokebank list but at the time, I wanted to have less files
    joke1 = """What's the best thing about Switzerland? Personally, I don't know, but their flag is a huge plus!"""
    joke2 = """A few hours ago, I invented a new word! Plagiarism!"""
    joke3 = "Hey, did you hear about the mathematician who's afraid of negative numbers? I hear he'll stop at nothing to avoid them!"
    joke4 = """" A woman in labor suddenly shouted,"Shouldn't! Wouldn't! Couldn't! Didn't! Can't!" "Don't worry," said the doc. "Those are just contractions."  """
    joke5 = "Why don’t scientists trust atoms?, Because they make up everything"
    joke6 = """A Spaniard is walking through a grocery store. He spies a carton on the shelf labeled "Soy Milk" He smiles to himself and says softly "yes you are"""
    joke7 = "Where are average things manufactured? I hear it's in a place called The satisfactory."
    joke8 = """How do you make a tissue dance? It's simple really, put a little boogie in it. """
    joke9 = """Why can't you hear a pterodactyl go to the bathroom? Because the "P" is silent. """
    joke10 = "What do you call the king of your pencil case? The ruler!"
    joke11 = "Two blood cells fell in love. Alas! it was all in vein"
    joke12 = "A customer at the bank where I work asked me to check her balance. So naturally, I pushed her over."
    joke13 = """A spanish guy is passing through the united states and realizes he didn't bring any socks, so he goes to buy some, but doesn't say english at all. Goes to a cloth store, but the clerk doesn't understand so he keeps showing the guy different clothing articles, until finally he shows some socks.The spanish guy exclaims "¡Eso sí que es!" (which means that's it in spanish). Angry, the clerk says "if you knew how to spell it, why didn't you?"""
    joke14 = """An English man, a french man, a Spaniard and a German are all standing watching a street performer do some excellent juggling. The juggler notices that the four gentleman have a very poor view, so he stands on a wooden box and calls out, "Can you all see me now?" The four men respond, "Yes." "Oui." "Si." "Ja." """
    joke15 = "Ok, this one is either very funny or lame, its a 50 50. Hitler and Goring are standing atop the Berlin radio tower. Hitler says he wants to do something to put a smile on Berliners' faces. So Goring says: 'Why don't you jump?' However, Don't laugh too hard - a German factory worker was reportedly executed for telling this one."
    joke16 = """ Hah! You are very  unlucky. This is  very long joke that will bore you to death. I better stop talking and make it longer! An Afghan, an Albanian, and Algerian, an American, an Andorran, an Angolan, an Antiguan, an Argintine, an Armenian, and Austrailian, an Austrian, an Azerbaijani,a Bahamian, a Bahraini, a Bangladeshi, a Barbadian, a Barbudans, a Batswanan, a Belarusian, a Belgian, a Belizean, a Beninese, a Bhutanese,a Bolivian, a Bosnian, a Brazilian, a Brit, a Bruneian, a Bulgarian, a Burkinabe, a Burmese, a Burundian, a Cambodian, a Cameroonian,a Canadian, a Cape Verdean, a Central African, a Chadian, a Chilean, a Chinese, a Colombian, a Comoran, a Congolese, a Costa Rican,a Croatian, a Cuban, a Cypriot, a Czech, a Dane, a Djibouti, a Dominican, a Dutchman, an East Timorese, an Ecuadorean, an Egyptian,an Emirian, an Equatorial Guinean, an Eritrean, an Estonian, an Ethiopian, a Fijian, a Filipino, a Finn, a Frenchman, a Gabonese,a Gambian, a Georgian, a German, a Ghanaian, a Greek, a Grenadian, a Guatemalan, a Guinea-Bissauan, a Guinean, a Guyanese, a Haitian,a Herzegovinian, a Honduran, a Hungarian, an I-Kiribati, an Icelander, an Indian, an Indonesian, an Iranian, an Iraqi, an Irishman,an Israeli, an Italian, an Ivorian, a Jamaican, a Japanese, a Jordanian, a Kazakhstani, a Kenyan, a Kittian and Nevisian, a Kuwaiti,a Kyrgyz, a Laotian, a Latvian, a Lebanese, a Liberian, a Libyan, a Liechtensteiner, a Lithuanian, a Luxembourger, a Macedonian,a Malagasy, a Malawian, a Malaysian, a Maldivan, a Malian, a Maltese, a Marshallese, a Mauritanian, a Mauritian, a Mexican,a Micronesian, a Moldovan, a Monacan, a Mongolian, a Moroccan, a Mosotho, a Motswana, a Mozambican, a Namibian, a Nauruan,a Nepalese, a New Zealander, a Nicaraguan, a Nigerian, a Nigerien, a North Korean, a Northern Irishman, a Norwegian, an Omani,a Pakistani, a Palauan, a Palestinian, a Panamanian, a Papua New Guinean, a Paraguayan, a Peruvian, a Pole, a Portuguese, a Qatari,a Romanian, a Russian, a Rwandan, a Saint Lucian, a Salvadoran, a Samoan, a San Marinese, a Sao Tomean, a Saudi, a Scottish,a Senegalese, a Serbian, a Seychellois, a Sierra Leonean, a Singaporean, a Slovakian, a Slovenian, a Solomon Islander, a Somali,a South African, a South Korean, a Spaniard, a Sri Lankan, a Sudanese, a Surinamer, a Swazi, a Swede, a Swiss, a Syrian, a Taiwanese,a Tajik, a Tanzanian, a Togolese, a Tongan, a Trinidadian or Tobagonian, a Tunisian, a Turkish, a Tuvaluan, a Ugandan,a Ukrainian, a Uruguayan, a Uzbekistani, a Venezuelan, a Vietnamese, a Welshman, a Yemenite, a Zambian and a Zimbabwean all go to a nightclub...The doorman stops them and says "Sorry I can’t let you in without a Thai.”"""
    joke17 = """A Spaniard, an American, and a Japanese man are approached by a billionaire. The billionaire asks them to participate in a year-long experiment wherein they will be taken to a deserted island to survive. He assigns them each tasks according to their heritage: The Spaniard will be in charge of food. The American will be in charge of shelter. And the Japanese man will be in charge of supplies.A year passes on the island and the billionaire returns to find only the Spaniard and American left."What happened?! Where is the Japanese man?" he asks."We're not sure! As soon as we got here he took off into the forest and we haven't seen him since." Worried for the Japanese man, they decide to search the island. After a few minutes of walking, all of the sudden, the Japanese man leaps out from the bushes and yells, "SUPPLIES!" """
    jokebank = [joke1, joke2, joke3, joke4, joke5, joke6, joke7, joke8, joke9, joke10, joke11, joke12, joke13, joke14, joke15, joke16, joke17]
    jokes = random.choice(jokebank)        
    print(jokes)
    say(jokes)

def askjoke():
    sg.PopupNonBlocking(jokes)
    say(jokes)
    say("Hahaha! I tell the lamest jokes!")
       
def weather():
    #getting data from weather API and using syntax from the documentation    
    webaddress="http://api.openweathermap.org/data/2.5/weather?q=Oakville&appid=e64b1e137bac554a3b8fdc230f8279ed&units=metric"
    weatherdata = requests.get(webaddress).json()
    temperature = weatherdata["main"]["temp"]
    feelslike = weatherdata["main"]["feels_like"]
    lowtemp = weatherdata["main"]["temp_min"]
    hightemp = weatherdata["main"]["temp_max"]
    say ('As for the weather, Currently, the weather outside is' + str(round(temperature)) + '° celsius, with a low of' + str(round(lowtemp)) + '& a high of' + str(round(hightemp)) + ', Although it feels like' + str(round(feelslike)) + '° celsius')
    conditions()

def conditions():
    #getting weather conditions data from weather API and using syntax from the documentation    
    webaddress='http://api.openweathermap.org/data/2.5/weather?q=Oakville&appid=e64b1e137bac554a3b8fdc230f8279ed&units=metric'
    weatherdata = requests.get(webaddress).json()
    condition = weatherdata['weather'][0]['main']
    description = weatherdata['weather'][0]['description']
    if ((condition == 'Clouds') and (description == 'overcast clouds')):
        say ("Based on my analysis, I suggest you keep an umbrella with you as the skies are somewhat cloudy")

    elif ((condition == 'Rain') and (description == 'light rain' or description == 'light intensity shower rain')):
        say ("It's raining a light amount outside and it could get worse, I suggest you carry an umbrella")

    elif ((condition == 'Rain') and (description == 'moderate rain')):
        say ("It's raining a lot and it could get worse, I suggest you carry an umbrella")

    elif ((condition == 'Rain') and (description == 'ragged rain')):
        say ("By the way, its raining and its is pouring at irregular times and with irregular amounts, to be safe, I suggest you carry an umbrella")

    elif ((condition == 'Rain') and (description == 'heavy intensity rain' or description == 'very heavy rain' or description == 'heavy intesity rain' or description == 'extreme rain')):
        say ("Conditions-wise, Yikes! It is pouring like crazy! But we're not at Thunderstorm level yet. I like to classify this as extremly intense rain! If you go outside carry an umbrella!")

    elif ((condition == 'Rain') and (description == 'freezing rain')):
        say ("Oh no! There is freezing rain outside! Be careful!")

    elif ((condition == 'Rain') and (description == 'freezing rain')):
        say ("Oh no! There is freezing rain outside! Be careful!")

    elif ((condition == 'Clouds') and (description == 'scattered clouds' or description == 'few clouds')):
        say ("There are a few clouds here and there but the skies are pretty clear!")

    elif ((condition == 'Clouds') and (description == 'broken clouds')):
        say ("There are quite a few clouds, and there is a decent chance of rain. Carry an umbrella in case. You never know when things go south.")

    elif ((condition == 'Rain') and (description == 'light rain')):
        say ("By the way, Its raining outside right now. But its merely a light pour, I don't think an umbrella is neccessary but if you want to carry one in case, by all means.")

    elif ((condition == 'Drizzle') and (description == 'light intensity drizzle' or description ==  'drizzle' or description == 'light intensity drizzle rain' or description == 'drizzle rain')):
        say ("By the way,  it's drizzling outside, carry an umbrella in case!")

    elif ((condition == 'Drizzle') and (description == 'heavy intensity drizzle rain' or description ==  'shower drizzle' or description == 'heavy shower rain and drizzle' or description == 'heavy intensity drizzle')):
        say ("By the way, it's drizzling outside quite heavily, carry an umbrella in case, I have a good feeling it will start pouring harder soon!")

    elif condition == 'haze' or condition == 'fog' or condition == 'foggy' or condition == 'mist' or condition == 'misty':
        say ("It's a bit foggy outside so drive safe!")

    elif condition == 'Clear' or condition == 'clear sky':
        say(", As for the weather conditions, it looks like you have nothing to worry about, the skies are clear!")

    else:
        say ("As for the weather conditions, there is a thunderstorm going on oustide with aa decent amount of rain, carry an umbrella and don't get elctrocuted!!! ")

def weather2():
    #getting data from weather API and using syntax from the documentation
    webaddress="http://api.openweathermap.org/data/2.5/weather?q=Oakville&appid=e64b1e137bac554a3b8fdc230f8279ed&units=metric"
    weatherdata = requests.get(webaddress).json()
    temperature = weatherdata["main"]["temp"]
    feelslike = weatherdata["main"]["feels_like"]
    lowtemp = weatherdata["main"]["temp_min"]
    hightemp = weatherdata["main']['temp_max"]
    say ("Currently, the weather is" + str(round(temperature)) + "°, with a low of" + str(round(lowtemp)) + "& a high of" + str(round(hightemp)) + ", Although it feels like" + str(round(feelslike)) + "°")
    conditions()
    
def date():
    year = datetime.datetime.now().year()
    month = datetime.datetime.now().month()
    date = datetime.datetime.now().day()
    say(date + month + year)

def assistantAI():
    event, values = UIWindow.read()    
    while True:
        if event in (None, 'Sleep'):
            say("Going to Sleep...Good Night")
            break

        elif ("who are you" or "what are you?" or "jarvis") in values[0].lower():
            jarvis = "I'm Jarvis, your personal assistant. But enough about me, let's see what else I can do for you!"
            sg.PopupNonBlocking(jarvis)
            say(jarvis)
        
        elif ("weather" or "umbrella" or "raincoat" or "sunscreen") in values[0].lower():
            print(values[0].lower())
            weather2()
            sg.PopupNonBlocking(weather())

        elif ("joke" or "laugh" or "amusing" or "amuse") in values[0].lower():
            askjoke()
            say("I am hilarious aren't I?")
            
        elif ("what day" or "today" or "date" or "month" or "year" or "day" or "season") in values[0].lower():
            date()
            
        elif "play" in values[0].lower():
            songKeywords = ['play', 'Play', 'Song', 'song']
            for terms in range (len(songKeywords)):
                if songKeywords[terms] in values[0].lower():
                    values[0] = values[0].replace(songKeywords[terms],"")
            mp3 = values[0] +".mp3"
            FileName = "/Users/swayam/Songs/"+mp3
            songs = "filler string. the commented out portion only works on my laptop, feel free to change the file direcotires as you please!"#os.listdir("/Users/swayam/Songs")
            if mp3 in songs:
                say("Playing" + songchoice + "Enjoy!")
                subprocess.call(['open', FileName])
            else:
                say('This song does not exist on your computer, let me search youtube!')
                url = 'https://www.youtube.com/results?search_query='+ values[0] + ' song'
                webbrowser.get().open(url)                
            
        elif ("search" or "who is" or "what is" or "why is" or "when is") in values[0].lower():
            searchKeywords = ["search", "who is", "what is"]
            for terms in range (len(searchKeywords)):
                if searchKeywords[terms] in values[0].lower():
                    values[0] = values[0].replace(searchKeywords[terms],"") 
            url = 'https://google.com/search?q=' + values[0]
            webbrowser.get().open(url)
            say ('Here is  what I found for' + values[0])

        else:
            try:
                wikiCheck = wikipedia.suggest(values[0])
                wikiResponse = wikipedia.summary(values[0], sentences=2,auto_suggest=True)
                sg.PopupNonBlocking(wikiResponse)
                say(wikiResponse)
                
            except wikipedia.exceptions.DisambiguationError:
                searchKeywords = ["search", "who is", "what is",]
                for terms in range(len(searchKeywords)):
                    if searchKeywords[terms] in values[0].lower():
                        values[0] = values[0].replace(searchKeywords[terms],"") 
                url = "https://google.com/search?q=" + values[0]
                webbrowser.get().open(url)
                say ("Here is  what I found for" + values[0])                
            
            except wikipedia.exceptions.PageError:
                searchKeywords = ["search", "who is", "what is",]
                for terms in range(len(searchKeywords)):
                    if searchKeywords[terms] in values[0].lower():
                        values[0] = values[0].replace(searchKeywords[terms],"") 
                url = "https://google.com/search?q=" + values[0]
                webbrowser.get().open(url)
                say ("Here is  what I found for" + values[0])
        break
        
say("Welcome to Jarvis! I am a personal virtual assistant created June 9th 2020. Enter a Command and press the Go button to Continue! There are no specific commands, just ask me anything! I can play songs already on your laptop if the code is modified or find them on YouTube, I can tell you the weather and what you need to bring with you and random pieces of information you want to know, like who Justin Trudeau is.")        
say("Firstly however, lets get you all set up. Please enter your name")
while True:
    name = input("Enter your first name only to begin: ")    
    if name == ' ' or name.isalpha() == False:
        say("Enter only your first name")
        print("Actually enter your name!")
        continue
    
    #used when testing to get by the normal greeting quickly
    elif name.lower() == "override":
        break
    
    else:
        say("Wow " + name + "! What a nice name!")
        hour = int(datetime.datetime.now().hour)
        if hour>=8 and hour<12:
            say("Good Morning" + name + "! Welcome")
            time = (datetime.datetime.now())
            currenttime = time.strftime(" %I %M").replace(" 0","")
            say ("Its " + currenttime + "A M to be precise")
            weather()
            say("Alright, let's see what I can do for you on this fine morning!")
            
        elif hour>=12 and hour<19:
            say("Good Afternoon" + name + "! Welcome to Jarvis!")
            time = (datetime.datetime.now())
            currenttime = time.strftime(" %I %M").replace(" 0","")
            say ("It's " + currenttime + " P M to be precise")
            weather()
            say("Alright, let's see what I can do for you this afternoon!")
            
        elif hour>=19 and hour<23:
            say("Good Evening" + name + "Welcome to Jarvis!")
            time = (datetime.datetime.now())
            currenttime = time.strftime(" %I %M").replace(" 0","")
            say ("It's" + currenttime + "P M to be precise")
            weather()
            say("Alright, let's see what I can do for you on this fine evening!")  
            
        elif hour>=5 and hour<8:
            say("Looks like someone woke up fairly early! Good Morning" + name + "!")
            time = (datetime.datetime.now())
            currenttime = time.strftime(" %I %M").replace(" 0","")
            say ("It's " + currenttime + " A M to be precise")
            weather()
            say("Alright, let's see what I can do for you on this fine morning!")
        else:
            time = (datetime.datetime.now())
            currenttime = time.strftime(" %I %M").replace(" 0","")
            weather()
            say ("Wow! It's quite late! It's " + currenttime + " A M. I suggest you go back to sleep and get your full 8 hours! If you're still here, let's see what I can do for you tonight.")

        #asks user if they'd like to hear a randomly generated joke.
        say("Before I continue, would you like to hear a hilarious joke to brighten up your day?")
        while True:
            joke = input("Would you like to hear a joke? ")
            
            if joke.lower() in yesList:
                lamejokes()
                say("Ha Ha Ha. I should be a comedian")
                break

            elif joke.lower() in noList:
                say("Ok.")
                break
            else:
                say("Please answer in a valid form of yes or no")
        break

#calls the main search function
assistantAI()

say ('Is there anything else you need? Go back to the shell and enter your response.')
while True:
    goagain = input ('Is there anything else you need? ')
    if goagain in yesList:
        UIWindow.close()        
        sg.theme('DarkBlue14')
        layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Enter'), sg.Button('Sleep')]]
        UIWindow = sg.Window('Jarvis UI', layout)
        assistantAI()
        continue
    
    elif goagain in noList:
        say ("Okay, I'll see you again" + name + 'Goodbye for now')
        UIWindow.close()
        exit()
        break
    
    else:
        say("I don't understand. Please enter yes or no")
        continue
                
