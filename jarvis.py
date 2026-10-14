

# # AI Jarvis chatbot, personal assistant

# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# from app import GROQ_API_KEY
# import musiclibrary
# import requests
# from groq import Groq
# import os
# from dotenv import load_dotenv
# load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# newsapi ="pub_d7056e99b66d4a06b126b9cde6b22d85"


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


# def process_command(c):
#     command = c.lower()

#     if "open youtube" in command:
#         print("Opening YouTube")
#         webbrowser.open("https://www.youtube.com")

#     elif "open google" in command:
#         print("Opening Google")
#         webbrowser.open("https://www.google.com")

#     elif "open stackoverflow" in command:
#         print("Opening Stack Overflow")
#         webbrowser.open("https://stackoverflow.com")

#     elif "open linkedin" in command:
#         print("Opening LinkedIn")
#         webbrowser.open("https://www.linkedin.com")

#     elif "open twitter" in command:
#         print("Opening Twitter")
#         webbrowser.open("https://www.twitter.com")

#     elif "open facebook" in command:
#         print("Opening Facebook")
#         webbrowser.open("https://www.facebook.com")

#     elif "open instagram" in command:
#         print("Opening Instagram")
#         webbrowser.open("https://www.instagram.com")

#     elif "open my instagram" in command:
#         print("Opening My Instagram")
#         webbrowser.open("https://www.instagram.com/_alokk_xviii/")

#     elif "open my github" in command:
#         print("Opening My GitHub")
#         webbrowser.open("https://github.com/AlokkAi")

#     elif command.startswith("play"):
#         song = command.replace("play", "", 1).strip()

#         if song in musiclibrary.music:
#             link = musiclibrary.music[song]
#             webbrowser.open(link)
#         else:
#             print(
#                 f"Sorry, I couldn't find the song "
#                 f"{song} in the music library."
#             )

#     elif "open chatbot" in command:

#         client = Groq(
#             api_key=GROQ_API_KEY
#         )

#         try:
#             with sr.Microphone() as source:

#                 print("Listening for ques...")

#                 audio = recognizer.listen(source)

#                 ques = recognizer.recognize_google(audio)

#             print("You ask for", ques)

#             if ques.lower() == "exit":
#                 print("Goodbye")
#                 return

#             response = client.chat.completions.create(
#                 model="openai/gpt-oss-20b",
#                 messages=[
#                     {"role": "user", "content": ques}
#                 ]
#             )

#             answer = response.choices[0].message.content

#             print("Bot:", answer)
#             speak(answer)

#         except sr.WaitTimeoutError:
#             print("No speech detected.")

#         except sr.UnknownValueError:
#             print("Could not understand the audio.")

#         except sr.RequestError as e:
#             print("Speech recognition service error:", e)

#         except Exception as e:
#             print("Error:", e)

#     elif "news" in command:
#         print("Getting the latest news")

#         try:
#             url = "https://newsdata.io/api/1/latest"

#             params = {
#                 "apikey": newsapi,
#                 "country": "in",
#                 "language": "en",
#                 "category": "top"
#             }

#             response = requests.get(
#                 url,
#                 params=params,
#                 timeout=10
#             )

#             print("News status:", response.status_code)

#             if response.status_code == 200:

#                 data = response.json()

#                 articles = data.get("results", [])

#                 print("Articles found:", len(articles))

#                 if len(articles) == 0:
#                     print("I could not find any news.")
#                     speak("I could not find any news.")

#                 else:
#                     print("Here are the latest headlines.")
#                     speak("Here are the latest headlines.")

#                     for article in articles[:5]:

#                         title = article.get("title")

#                         if title:
#                             print(title.split())
#                             speak(title)

#             else:
#                 print(response.text)
#                 speak("Sorry, I could not get the news.")

#         except Exception as e:
#             print("NEWS ERROR:", e)
#             speak("There was an error getting the news.")

#     else:
#         print("Sorry, I don't understand that command.")
#         speak("Sorry, I don't understand that command.")


# if __name__ == "__main__":

#     print("=====================================")
#     print("= I AM JARVIS YOUR PERSONAL ASSISTANT =")
#     print("=====================================")
#     print()

#     speak("Hey, I am Jarvis. Please identify yourself.")

#     while True:

#         print("--------------")
#         print("Recognizing...")
#         print("--------------")

#         try:

#             # Listen for the wake word "Jarvis"
#             with sr.Microphone() as source:

#                 print("Listening...")

#                 audio = recognizer.listen(
#                     source,
#                     timeout=5,
#                     phrase_time_limit=3
#                 )

#             word = recognizer.recognize_google(audio)

#             if word.lower() == "jarvis":

#                 print("-----------------")
#                 print("Audio received...")
#                 print("-------------------------------------------")
#                 print("You have been identified. You said:", word)
#                 print("-------------------------------------------")

#                 print("----------------------------------------")
#                 print("JARVIS: Hey Alok, what can I do for you?")
#                 print("----------------------------------------")

#                 # Listen for command
#                 with sr.Microphone() as source:

#                     print("Listening for command...")

#                     audio = recognizer.listen(source)

#                     command = recognizer.recognize_google(audio)

#                 print("You said:", command)

#                 process_command(command)

#         except sr.WaitTimeoutError:
#             print("No speech detected.")

#         except sr.UnknownValueError:
#             print("Could not understand the audio.")

#         except sr.RequestError as e:
#             print("Speech recognition service error:", e)

#         except Exception as e:
#             print("Error:", e)

#             #Put Jarvis back to sleep 
#             if ( "sleep" in command.lower or "go to sleep" in command.lower ):
#                  speak("Okay, going to sleep.")
#                  active = False
#             else:
#                 process_command(command)
#         except sr.WaitTimeoutError:
#             print("No speech detected.")
#         except sr.UnknownValueError:
#             print("Could not understand the audio.")
#         except sr.RequestError as e:
#             print("Speech recognition service error:", e)
#         except Exception as e:
#             print("Error:", e)


# AI Jarvis chatbot, personal assistant

import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from groq import Groq
import os
from dotenv import load_dotenv
import random
load_dotenv()

import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

news_api_key=NEWS_API_KEY

def speak(text):
    engine.say(text)
    engine.runAndWait()


def process_command(c):
    command = c.lower()

    if "open youtube" in command:
        print("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return "Opening YOUTUBE"
     

    elif "open google" in command:
        print("Opening Google")
        webbrowser.open("https://www.google.com")
        return "Opening GOOGLE"
             

    elif "open stackoverflow" in command:
        print("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
        return "Opening STACKFLOW"
                        

    elif "open linkedin" in command:
        print("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        return "Opening LINKEDIN"
                                
    elif "open twitter" in command:
        print("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
        return "Opening TWITTER"
        

    elif "open facebook" in command:
        print("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        return "Opening FACEBOOK"
        

    elif "open instagram" in command:
        print("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
        return "Opening INSTAGRAM"
        

    elif "open my instagram" in command:
        print("Opening My Instagram")
        webbrowser.open("https://www.instagram.com/_alokk_xviii/")
        return "Opening MY Ig"
    
    elif "open my linkedin" in command:
        print("Opening My linkedin")
        webbrowser.open("https://www.linkedin.com/in/alok-kumar-97825242b/")
        return "Opening MY Linkedin"
        

    elif "open my github" in command:
        print("Opening My GitHub")
        webbrowser.open("https://github.com/AlokkAi")
        return "Opening GITHUB"
    
    elif "Password Tool" in command:
        return "PASSWORD_TOOL"
        print("Hey user choose option")

        print("Choose 1 to generate password ")
        print("Choose 2 to check strength of password ")

        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        a = int(input("Enter no : "))
        s = "!@#$%^&*()_-=+"

        password = random.randint(000000,999999)
        if(a == 1):
         result = ""
         for i in range(6):
            result += random.choice(characters)
         special = random.choice(s)
         password = str(password)
         p = result+password+special


         print("Your password is ", p)
        elif(a == 2):
         b = input("Enter your password : ")
         strength = len(b)
         if(strength<=4):
            print("Your password is weak" , b)

         elif(strength<=6):
            print("Your password is moderate")

         elif(strength<=8):
            print("Your password is strong")

         elif(strength>8):
            print("Your password is too strong" , b)

     
    elif command.startswith("play"):
        song = command.replace("play", "", 1).strip()

        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            webbrowser.open(link)
        else:
            print(
                f"Sorry, I couldn't find the song "
                f"{song} in the music library."
            )

    elif "open chatbot" in command:

        client = Groq(
            api_key=GROQ_API_KEY
        )

        try:
            with sr.Microphone() as source:

                print("Listening for ques...")

                audio = recognizer.listen(source)

                ques = recognizer.recognize_google(audio)

            print("You ask for", ques)

            if ques.lower() == "exit":
                print("Goodbye")
                return

            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {"role": "user", "content": ques}
                ]
            )

            answer = response.choices[0].message.content

            print("Bot:", answer)
            speak(answer)

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Could not understand the audio.")

        except sr.RequestError as e:
            print("Speech recognition service error:", e)

        except Exception as e:
            print("Error:", e)

    elif "news" in command:
     print("Getting the latest news")

     try:
        url = "https://newsdata.io/api/1/latest"

        params = {
            "apikey": news_api_key,
            "country": "in",
            "language": "en",
            "category": "top"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            articles = data.get("results", [])

            if not articles:
                return "I could not find any news."

            headlines = []

            for article in articles[:5]:
                title = article.get("title")

                if title:
                    headlines.append(title)

            if not headlines:
                return "I could not find any news headlines."

            return "Here are the latest headlines:\n" + "\n".join(
                f"{i}. {title}"
                for i, title in enumerate(headlines, start=1)
            )

        else:
            print("News API error:", response.status_code)
            return "Sorry, I could not get the news."

     except Exception as e:
        print("NEWS ERROR:", e)
        return "There was an error getting the news."
    else:
        print("Sorry, I don't understand that command.")
        speak("Sorry, I don't understand that command.")


if __name__ == "__main__":

    print("=====================================")
    print("= I AM JARVIS YOUR PERSONAL ASSISTANT =")
    print("=====================================")
    print()

    speak("Hey, I am Jarvis. Please identify yourself.")

    while True:

        print("--------------")
        print("Recognizing...")
        print("--------------")

        try:

            # Listen for the wake word "Jarvis"
            with sr.Microphone() as source:

                print("Listening...")

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":

                print("-----------------")
                print("Audio received...")
                print("-------------------------------------------")
                print("You have been identified. You said:", word)
                print("-------------------------------------------")

                print("----------------------------------------")
                print("JARVIS: Hey Alok, what can I do for you?")
                print("----------------------------------------")

                # Listen for command
                with sr.Microphone() as source:

                    print("Listening for command...")

                    audio = recognizer.listen(source)

                    command = recognizer.recognize_google(audio)

                print("You said:", command)

                process_command(command)

        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Could not understand the audio.")

        except sr.RequestError as e:
            print("Speech recognition service error:", e)

        except Exception as e:
            print("Error:", e)

            #Put Jarvis back to sleep 
            if ( "sleep" in command.lower or "go to sleep" in command.lower ):
                 speak("Okay, going to sleep.")
                 active = False
            else:
                process_command(command)
        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print("Speech recognition service error:", e)
        except Exception as e:
            print("Error:", e)
