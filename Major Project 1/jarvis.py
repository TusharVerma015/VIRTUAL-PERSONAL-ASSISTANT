from numpy import take
from psutil import sensors_battery
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import requests, json
import random
import pyautogui
import psutil
import os
import pyjokes

egg12 = pyttsx3.init('sapi5')
jarvisVoices = egg12.getProperty('voices')
egg12.setProperty('voice',jarvisVoices[0].id)
def speakJarvis(audio):
    egg12.say(audio)
    egg12.runAndWait()
def wishTheMaster():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speakJarvis("Good morning master, i hope you slept good.")
    elif(hour==12):
        speakJarvis("Good noon master, hope you're having a good day.")
    elif(hour>12 and hour<16):
        speakJarvis("Good Afternoon Master")
    else:
        speakJarvis("Good evening master, which voice do you want me to operate in ?")
def changeVoice(voice):
    if("male" in voice):
        egg12.setProperty('voice',jarvisVoices[0].id)
        print("Hi i am jarvis, How can i help you ? ")
        speakJarvis("Hi i am jarvis, How can i help you ? ")
    elif("female" in voice):
        egg12.setProperty('voice',jarvisVoices[1].id)
        print("Hi i am Female jarvis, How can i help you ? ")
        speakJarvis("Hi i am Female jarvis, How can i help you ? ")
    return True



def tcommandfromMaster():
    recGogNizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        speakJarvis("listening")
        recGogNizer.pause_threshold = 1
        recGogNizer.energy_threshold = 1000
        audio = recGogNizer.listen(source)
    try:    
        print("Recognizing...")
        speakJarvis("Recognizing")
        myQuery = recGogNizer.recognize_google(audio, language='en-in')
        print(f"{myQuery}\n")
    except Exception as e:
        
        print("Please say that again")
        speakJarvis("Please say that again")
        
        return "None"
    
    return myQuery
        
if __name__ == "__main__":
    wishTheMaster()
    myQuery = tcommandfromMaster().lower()
    while True:
        if "female" in myQuery:
            egg12.setProperty('voice',jarvisVoices[1].id)
            print("I am jarvis,  Tell me how can i help you .")
            speakJarvis("I am jarvis,  Tell me how can i help you .")
            myQuery = tcommandfromMaster().lower()

        if "male" in myQuery:
            egg12.setProperty('voice',jarvisVoices[0].id)
            print("I am jarvis,  Tell me how can i help you .")
            speakJarvis("I am jarvis,  Tell me how can i help you .")
            myQuery = tcommandfromMaster().lower()

        if "change voice" in myQuery:
            print("In which voice do you want me to operate in ?")
            speakJarvis("In which voice do you want me to operate in ?")
            x = tcommandfromMaster().lower()
            ret = changeVoice(x)
            myQuery = tcommandfromMaster().lower()


        if "hello" in myQuery:
            print("Hi There")
            speakJarvis("Hi There")
            myQuery = tcommandfromMaster().lower()
        if "calculate" in myQuery:
            print("Tell me the first number")
            speakJarvis("Tell me the first number")
            a = int(input("Enter here : "))
            b = int(input())
            speakJarvis("Tell me the operation")
            myQuery = tcommandfromMaster().lower()
            if "add"  in myQuery:
                print(a+b)
                speakJarvis(a+b)
            if "subtract" in myQuery:
                print(a-b)
                speakJarvis(a-b)
            if "multiply" in myQuery:
                print(a*b)
                speakJarvis(a*b)
            if "divide" in myQuery:
                print(a/b)
                speakJarvis(a/b)
            myQuery = tcommandfromMaster().lower()
        elif "joke" in myQuery:
            joke = pyjokes.get_joke(language='en',category='neutral')
            print(joke)
            speakJarvis(joke)
            myQuery = tcommandfromMaster().lower()
        
        elif "battery" in myQuery:
            cpu = str(sensors_battery().percent)
            print(f"You have  {cpu} %  battery")
            speakJarvis(f"You have  {cpu} %  battery")
            if(sensors_battery().percent<50):
                if(sensors_battery().power_plugged==False):
                    print("You should plugin your charger master")
                    speakJarvis("You should plugin your charger master")
            else:
                print("You can continue your work without plugging in")
                speakJarvis("You can continue your work without plugging in")

            myQuery = tcommandfromMaster().lower()

            
        elif "how are you" in myQuery:
            lst2 = ["I am good","Fine, what about you?", "Great, as always","amazing, have nothing to be sad about"]
            rndd = random.randint(0,3)
            print(lst2[rndd])
            speakJarvis(lst2[rndd])
            myQuery = tcommandfromMaster().lower()
            lst3 = ["Life is too short to be sad","That's good to hear","That's wonderful"]
            rnddd = random.randint(0,2)
            print(lst3[rnddd])
            speakJarvis(lst3[rnddd])
            myQuery = tcommandfromMaster().lower()
        elif "what are you doing" in myQuery:
            lst4 = ["Just hanging out with siri", "Serving you","Thinking ways to satisfy parent's expectations hahaha","Thinking about better ways to serve you","Learning new tasks","Pushing my limits","Chilling with a wine"]
            rndddd = random.randint(0,7)
            print(lst4[rndddd])
            speakJarvis(lst4[rndddd])
            speakJarvis("What about you")
            myQuery = tcommandfromMaster().lower()
            print(myQuery)
            print("Good, tell me what you have for me in the plate")
            speakJarvis("Good, tell me what you have for me in the plate")
            myQuery = tcommandfromMaster().lower()
        elif "screenshot" in myQuery:
            img = pyautogui.screenshot()
            img.save("C:\\Users\\TUSHAR VERMA\\Pictures\\Screenshots\\js.png")
            speakJarvis("Screenshot done, You can view it in C:\\Users\\TUSHAR VERMA\\Pictures\\Screenshots\\js.png ")
            myQuery = tcommandfromMaster().lower()
        elif "time" in myQuery:
            print(datetime.datetime.now().time())
            myQuery = tcommandfromMaster().lower()
        elif "time" and "hello" in myQuery:
            print(datetime.datetime.now().time())
            myQuery = tcommandfromMaster().lower()
        elif "write down" in myQuery:
            speakJarvis("What should i write down sir")
            notes = tcommandfromMaster()
            file1 = open('data.txt','w')
            file1.write(notes)
            file1.close()
            print("I have noted that sir , do you want me to repeat?")
            speakJarvis("I have noted that sir , do you want me to repeat?")
            myQuery = tcommandfromMaster().lower()
            if "yes" in myQuery:
                speakJarvis("I have noted: "+ notes)
            else:
                speakJarvis("okay")
            myQuery = tcommandfromMaster().lower()
        elif "remember" in myQuery:
            file1 = open("data.txt",'r')
            
            
            speakJarvis("You told me to remember that"+file1.read())
            myQuery = tcommandfromMaster().lower()

        elif "wikipedia" in myQuery:
            print("Searching wikipedia...")
            speakJarvis("Searching wikipedia")
            myQuery = myQuery.replace("wikipedia","")
            results = wikipedia.summary(myQuery,sentences=2)
            print("According to wikipedia...")
            speakJarvis("According to wikipedia")
            print(results)
            speakJarvis(results)
            myQuery = tcommandfromMaster().lower()


        elif "open youtube" in myQuery:
            print("opening youtube...")
            speakJarvis("opening youtube")
            webbrowser.open_new_tab("youtube.com")
            myQuery = tcommandfromMaster().lower()

        elif "open google" in myQuery:
            print("opening google...")
            speakJarvis("opening google")   
            webbrowser.open_new_tab("google.com")
            myQuery = tcommandfromMaster().lower()

        
        elif "outside" in myQuery:
            print("Which city's weather would you like to know?")
            speakJarvis("Which city's weather would you like to know?")
            city = tcommandfromMaster().lower()
            api_key = "8bdc1d60e7103c410fbe5ca70951a6f5"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + api_key + "&q=" + city
            response = requests.get(complete_url)
            rj =  response.json()
            if rj["cod"] != "404":
                w = rj["main"]
                current_temperature = int(w["temp"]-273.15)
                current_pressure = w["pressure"]
                current_humidity = w["humidity"]
                z = rj["weather"]
                weather_desc = z[0]["description"]
                print(" Temperature (in celcius unit) = " +
                    str(current_temperature) +" Celcius"+
                    "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
                    "\n humidity (in percentage) = " +
                    str(current_humidity) +
                    "\n description = " +
                    str(weather_desc))
                speakJarvis(current_temperature)
                speakJarvis(weather_desc+"  in  "+city)
            else:
                print("City not found")
                speakJarvis("City not found")
            myQuery = tcommandfromMaster().lower()
        elif "coin" in myQuery:
            lst1 = ["Heads","Tails"]
            result = random.randint(0,1)
            print("It's a " + lst1[result])
            speakJarvis("It's a " + lst1[result])
            myQuery = tcommandfromMaster().lower()
        elif "left" in myQuery:
            print("moving cursor to left")
            speakJarvis("moving cursor to left")
            pyautogui.moveTo(500,300,2)
            print("moved cursor to left")
            myQuery = tcommandfromMaster().lower()
        elif "open amazon" in myQuery:
            webbrowser.open("amazon.com")
            print("opening amazon...")
            speakJarvis("opening amazon")   
            myQuery = tcommandfromMaster().lower()

        elif "open flipkart" in myQuery:
            webbrowser.open("flipkart.com")
            print("opening flipkart...")
            speakJarvis("opening flipkart")   
            myQuery = tcommandfromMaster().lower()

        elif "open facebook" in myQuery:
            webbrowser.open("facebook.com")
            print("opening facebook...")
            speakJarvis("opening facebook")   
            myQuery = tcommandfromMaster().lower()

        elif "open instagram" in myQuery:
            webbrowser.open("instagram.com")
            print("opening instagram...")
            speakJarvis("opening instagram")   
            myQuery = tcommandfromMaster().lower()

        elif "open yahoo" in myQuery:
            webbrowser.open("yahoo.com")
            print("opening yahoo...")
            speakJarvis("opening yahoo")   
            myQuery = tcommandfromMaster().lower()

        elif "open gmail" in myQuery:
            webbrowser.open("gmail.com")
            print("opening gmail...")
            speakJarvis("opening gmail")   
            myQuery = tcommandfromMaster().lower()

        elif "open stack overflow" in myQuery:
            webbrowser.open("stackoverflow.com")
            print("opening stackoverflow...")
            speakJarvis("opening stackoverflow")   
            myQuery = tcommandfromMaster().lower()

        elif "open gfg" in myQuery:
            webbrowser.open("geeksforgeeks.org")
            print("opening geeksforgeeks...")
            speakJarvis("opening geeksforgeeks")   
            myQuery = tcommandfromMaster().lower()

        elif "open college website" in myQuery:
            webbrowser.open("jmit.ac.in")
            print("opening jmit...")
            speakJarvis("opening jmit")   
            myQuery = tcommandfromMaster().lower()

        elif "open spotify" in myQuery:
            webbrowser.open("spotify.com")
            print("opening spotify")
            speakJarvis("opening spotify")   
            myQuery = tcommandfromMaster().lower()

        elif "open gaana" in myQuery:
            webbrowser.open("gaana.com")
            print("opening gaana")
            speakJarvis("opening gaana")   
            myQuery = tcommandfromMaster().lower()

        elif "open hungama" in myQuery:
            webbrowser.open("hungama.com")
            print("opening hungama")
            speakJarvis("opening hungama")   
            myQuery = tcommandfromMaster().lower()

        elif "open twitter" in myQuery:
            webbrowser.open("twitter.com")
            print("opening twitter")
            speakJarvis("opening twitter")   
            myQuery = tcommandfromMaster().lower()

        elif "open udemy" in myQuery:
            webbrowser.open("udemy.com")
            print("opening udemy")
            speakJarvis("opening udemy")   
            myQuery = tcommandfromMaster().lower()

        elif "open leet code" in myQuery:
            webbrowser.open("leetcode.com")
            print("opening leetcode")
            speakJarvis("opening leetcode")   
            myQuery = tcommandfromMaster().lower()

        elif "open hacker Earth" in myQuery:
            webbrowser.open("hackerearth.com")
            print("opening hackerearth")
            speakJarvis("opening hackerearth")   
            myQuery = tcommandfromMaster().lower()

        elif "open maps" in myQuery:
            webbrowser.open("maps.google.com")
            print("opening maps")
            speakJarvis("opening maps")   
            myQuery = tcommandfromMaster().lower()

        elif "open netflix" in myQuery:
            webbrowser.open("netflix.com")
            print("opening netflix")
            speakJarvis("opening netflix")   
            myQuery = tcommandfromMaster().lower()

        elif "open Prime video" in myQuery:
            webbrowser.open("primevideo.com")
            print("opening prime video")
            speakJarvis("opening prime video")   
            myQuery = tcommandfromMaster().lower()

        elif "open hotstar" in myQuery:
            webbrowser.open("hotstar.com")
            print("opening hotstar")
            speakJarvis("opening hotstar")   
            myQuery = tcommandfromMaster().lower()

        elif "open my protein" in myQuery:
            webbrowser.open("myprotein.com")
            print("opening myprotein")
            speakJarvis("opening myprotein")   
            myQuery = tcommandfromMaster().lower()

        elif "open sony" in myQuery:
            webbrowser.open("sonyliv.com")
            print("opening sonyliv")
            speakJarvis("opening sonyliv")   
            myQuery = tcommandfromMaster().lower()

        elif "open airtel" in myQuery:
            webbrowser.open("airtel.in")
            print("opening airtel")
            speakJarvis("opening airtel")   
            myQuery = tcommandfromMaster().lower()

        elif "open v i" in myQuery:
            webbrowser.open("myvi.in")
            print("opening vodafone idea")
            speakJarvis("opening vodafone idea")   
            myQuery = tcommandfromMaster().lower()

        elif "open HDFC" in myQuery:
            webbrowser.open("hdfcbank.com")
            print("opening hdfc")
            speakJarvis("opening hdfc")   
            myQuery = tcommandfromMaster().lower()

        elif "open sbi" in myQuery:
            webbrowser.open("onlinesbi.com")
            print("opening sbi")
            speakJarvis("opening sbi")   
            myQuery = tcommandfromMaster().lower()

        elif "open linkedin" in myQuery:
            webbrowser.open("linkedin.com")
            print("opening linkedin")
            speakJarvis("opening linkedin")   
            myQuery = tcommandfromMaster().lower()

        elif "open microsoft" in myQuery:
            webbrowser.open("microsoft.com")
            print("opening microsoft")
            speakJarvis("opening microsoft")   
            myQuery = tcommandfromMaster().lower()

        

        elif 'play music' in myQuery:
            music_dir = 'D:\\song'
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))
            myQuery = tcommandfromMaster().lower()
        elif 'code' in myQuery:
            cpathh = "C:\\Users\\TUSHAR VERMA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(cpathh)
            myQuery = tcommandfromMaster().lower()

        elif 'pycharm' in myQuery:
            pypath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains'
            os.startfile(pypath)
            myQuery = tcommandfromMaster().lower()

        elif "right" in myQuery:
            print("moving cursor to right")
            speakJarvis("moving cursor to right")
            pyautogui.moveRel(1100,0,2)
            print("moved cursor to right")
            myQuery = tcommandfromMaster().lower()
        elif "left" in myQuery:
            print("moving cursor to left")
            speakJarvis("moving cursor to left")
            pyautogui.moveRel(-400,0,2)
            print("moved cursor to left")
            myQuery = tcommandfromMaster().lower()
        elif "down" in myQuery:
            print("moving cursor to down")
            speakJarvis("moving cursor to down")
            pyautogui.moveRel(600,700,2)
            print("moved cursor to down")
        elif "up" in myQuery:
            print("moving cursor to up")
            speakJarvis("moving cursor to up")
            pyautogui.moveTo(1266,15,2)

            myQuery = tcommandfromMaster().lower()
        elif "right click" in myQuery:
            pyautogui.click(x=1000,y=500,clicks=1,button='right')
            myQuery = tcommandfromMaster().lower()
        elif "bluetooth" in myQuery:
            print("Toggling Bluetooth")
            speakJarvis("Toggling Bluetooth")
            pyautogui.moveTo(1266,15,2)
            pyautogui.moveTo(1777,21,2)
            pyautogui.click()
            pyautogui.moveTo(1766,1054,2)
            pyautogui.click()
            
            pyautogui.moveTo(1683,570,2)
            pyautogui.click()
            myQuery = tcommandfromMaster().lower()

            

        
        elif "windows" in myQuery:
            pyautogui.press('win')
            myQuery = tcommandfromMaster().lower()
        elif "video" in myQuery:
            pyautogui.moveTo(1239,1047,2)
            pyautogui.click()
            pyautogui.moveTo(345,98,2)
            pyautogui.click()

            pyautogui.moveTo(707,119,2)
            pyautogui.click()
            pyautogui.press(keys=['p','y','t','h','o','n','space','i','n','space','o','n','e','space','v','i','d','e','o'])
            pyautogui.press('enter')
            myQuery = tcommandfromMaster().lower()







        elif ("quit" or "bye") in myQuery:
            lst = ["Until next time","Nice serving you","byee","Have a good day"]
            rnd = random.randint(0,3)
            speakJarvis(lst[rnd])
            exit()
        elif "game" in myQuery:
            print("Which game would you like to play. I have these")
            print("1.Guess a number \n 2.Guess the animal \n 3. Flip a coin and get a chance to command me more if you win ")
            speakJarvis("Which game would you like to play. I have these")
            
            x = int(input("Enter here: "))
            if(x==1):
                rnd = random.randint(0,100)
                speakJarvis("Guess the number")
                count =0
                flag=True
                while(flag):
                    inp = int(input("Guess the number: "))

                    if(inp>rnd):
                        print("Your number is larger")
                        speakJarvis("Your number is larger")
                        count+=1
                    if(inp<rnd):
                        print("Your number is smaller")
                        speakJarvis("Your number is smaller")
                        count+=1
                    else:
                        print("Yayy! You guessed it in "+ str(count)+" times")
                        speakJarvis("Yayy! You guessed it in "+ str(count)+" times")
                        flag=False
            if(x==2):
                speakJarvis("Guess the animal")
                lst = ["lion","giraffe","goat","dog","penguin","cat","monkey","tiger","cheetah","cow"]
                rndd = random.randint(0,9)
                anm = lst[rndd]
                print("3... 2... 1......")
                print("Guess it now...")
                inp = tcommandfromMaster().lower()
                if(inp==anm):
                    print("Congratulations you guessed")
                else:
                    print("Beep Beep wrong")
            myQuery = tcommandfromMaster().lower()
        else:
            speakJarvis("Sorry,That maybe beyond my abilities at the moment. Try Something different")
            myQuery = tcommandfromMaster().lower()



                    




        
        

            




