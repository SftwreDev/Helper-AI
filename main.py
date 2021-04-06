import pyttsx3
import datetime
import time
import webbrowser
import speech_recognition as sr
import requests, json
import random

engine = pyttsx3.init()

def weather():
    '''Weather functions'''
    api_key = "a817c6788647660104cfcd938e49f798"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Lipa City"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        kelvin_to_celcius = current_temperature - 273.15
        celcius = round(kelvin_to_celcius)
        current_pressure = y["pressure"] 
        current_humidity = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 

        engine.say('''
        Temperature today is: {celcius} degrees celsius.
        Current Pressure is: {current_pressure} hPa.
        Humidity is: {current_humidity} %.
        The sky is {weather_description} today
        '''.format(celcius=celcius, current_pressure=current_pressure, current_humidity=current_humidity,weather_description=weather_description ))
        
def assistant():

    greetings = ['How are you today sir ?' , 'Today is a great day ! How can I help You ?' , 'Hello Sir']
    greetings_select = random.choice(greetings)
    date = datetime.date.today()
    time = datetime.time()
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', 200)
    engine.say("Hello. This is Janno. Your personal assistant. System is now processing")
    engine.say("Sir Gian, today is {0}, {1}".format(date, greetings_select))
    engine.runAndWait()
    # answer = input(">>> ")
    
    with sr.Microphone() as source:
       
        r = sr.Recognizer()
        print("Listening ...")
        audio = r.listen(source,  phrase_time_limit=3)
        print("Recognizing ...")
    try:
        answer = r.recognize_google(audio);
        google = ['open google', 'google', 'Google', 'i want to use google']
        if answer in google:
            engine.say("Now opening Google Browsers.")
            engine.runAndWait()
            webbrowser.open('http://www.google.com')
        
        elif answer == "what time is it":
            engine.say("It's {}".format(time))
            engine.runAndWait()

        elif answer == "open facebook":
            engine.say("Now opening Facebook.Com")
            engine.runAndWait()
            webbrowser.open("http://www.facebook.com")

        elif answer == "what is weather today":
            engine.say("Now checking the weather forecast")
            engine.runAndWait()
            weather()

        elif answer == "who are my parents":
            engine.say("Now checking the family history")
            engine.say(
                '''
                Your mother is Nenita Corazon L. Garcia, 59 years of age. She is the most brilliant woman right now.
                Your father is Doroteo M. Garcia, 63 years of age. He suffered a stroke 12 years ago and is now paralyzed.
                '''
            )

            engine.runAndWait()

        elif answer == "i'm sad":
            engine.say("Do you want a sexy young lady?")
            engine.runAndWait()


        
        else:
            engine.say("Sorry I can't provide your request")
            engine.runAndWait()
        
   

    except:
        engine.say("Sorry , I can't hear what you are saying")
        engine.runAndWait()
    
    
            

    

while True:
    assistant()
    with sr.Microphone() as source:
        engine.say("Sir Gian, do you have another request?")
        engine.runAndWait()
        r = sr.Recognizer()
        print("Listening ...")
        audio = r.listen(source,  phrase_time_limit=3)
        print("Recognizing ...")   
        answer = r.recognize_google(audio);
        try:
            if answer == 'yes':
                engine.say("I'm happy that I can serve you more")
                engine.runAndWait()
                assistant()
            
            elif answer == 'nothing':
                engine.say("Okay sir Gian, beep me if you need me!!")
                engine.say("System terminating. Good bye ! .")
                engine.runAndWait()
                break
        except:
            engine.say("I don't know what you are talking about")
            engine.runAndWait()
