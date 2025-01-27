import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pywhatkit
import pyautogui
import time
import os
import platform
import pytesseract
from PIL import ImageGrab, Image
import re
import win32com.client as win32

# Update the path to Tesseract if necessary
pytesseract.pytesseract.tesseract_cmd = r'your-tessaract-path'

contacts = {
    # Add contacts here as needed (removed sensitive contact information)
}

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

# Removed sensitive API keys
newsapi = "your-news-api-key"
ai2i_api_key = "your-ai-api-key"

def start_jarvis():
    return "Jarvis has started successfully!"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_whatsapp():
    # Provide the correct path to WhatsApp executable if needed
    whatsapp_path = r"C:\Path\To\WhatsApp.exe"
    os.startfile(whatsapp_path)
    time.sleep(5)

def open_spotify():
    spotify_path = r"C:\Path\To\Spotify.exe"
    os.startfile(spotify_path)
    time.sleep(5)

def increase_volume(times):
    for i in range(times):
        pyautogui.press('volumeup')
    speak(f"Increasing the volume {times} times")

def decrease_volume(times):
    for i in range(times):
        pyautogui.press('volumedown')
    speak("Decreasing the volume {times} times")

def get_volume_count(command):
    match = re.search(r'(\d+)', command)
    if match:
        return int(match.group(1))
    return 1

def generate_essay(topic, length=200):
    headers = {
        'Authorization': f'Bearer {ai2i_api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "prompt": f"Write an essay on {topic}",
        "maxTokens": length,
        "temperature": 0.7
    }
    
    response = requests.post('https://api.ai21.com/studio/v1/j2-ultra/complete', json=data, headers=headers)
    if response.status_code == 200:
        essay = response.json()['completions'][0]['data']['text']
        return essay.strip()
    else:
        print("Error:", response.status_code, response.text)
        return None

def open_word():
    word = win32.Dispatch('Word.Application')
    word.Visible = True
    doc = word.Documents.Add()
    return word, doc

def write_to_word(doc, text, save_path):
    doc.Content.Text = text
    doc.SaveAs(save_path)
    
def get_last_message():
    time.sleep(1)
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    
    last_message_region = (692, 822, 1229, 908)
    last_message_image = screenshot.crop(last_message_region)
    last_message_text = pytesseract.image_to_string(last_message_image)
    return last_message_text.strip()

def generate_reply(last_message):
    response = requests.post(
        "https://api.ai21.com/studio/v1/j2-ultra/complete",
        headers={
            "Authorization": f"Bearer {ai2i_api_key}",
            "Content-Type": "application/json"
        },
        json={
            "prompt": f"Reply to the following message: '{last_message}'",
            "maxTokens": 50,
            "temperature": 0.5
        }
    )

    if response.status_code == 200:
        data = response.json()
        return data["completions"][0]["data"]["text"]
    else:
        print(f"Error generating reply: {response.status_code}, {response.text}")
        return "Sorry, I couldn't generate a reply."

def reply_to_contact(contact_name):
    phone_number = contacts.get(contact_name)
    if phone_number:
        open_whatsapp()
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.typewrite(phone_number)
        time.sleep(2)
        pyautogui.moveTo(306, 284, duration=1)
        pyautogui.click()
        time.sleep(1)

        last_message = get_last_message()
        print(f"Last message from {contact_name}: {last_message}")
        reply = generate_reply(last_message)

        pyautogui.typewrite(reply)
        time.sleep(1)
        pyautogui.press('enter')
        speak(f"Reply sent to {contact_name}.")
    else:
        speak(f"Sorry, I don't have a contact saved as {contact_name}.")

def translate_to_english(text):
    translation_api_url = "https://libretranslate.de/translate"
    
    params = {
        "q": text,
        "source": "te",
        "target": "en",
        "format": "text"
    }
    
    r = requests.post(translation_api_url, json=params)
    if r.status_code == 200:
        translation_data = r.json()
        return translation_data['translatedText']
    else:
        return None

def aiProcess(command):
    if any(u'\u0c00' <= char <= u'\u0c7f' for char in command):
        translated_command = translate_to_english(command)
    else:
        translated_command = command  
    
    if translated_command:
        print(f"Translated Command: {translated_command}")
        if "your name" in translated_command.lower():
            return "My name is Jarvis, How can I help you sir?"

        r = requests.post(
            "https://api.ai21.com/studio/v1/j2-ultra/complete",
            headers={
                "Authorization": f"Bearer {ai2i_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": translated_command,
                "maxTokens": 50,
                "temperature": 0.5
            }
        )

        if r.status_code == 200:
            data = r.json()
            return data["completions"][0]["data"]["text"]
        else:
            print(f"Error: {r.status_code}, {r.text}")
            return "Sorry, I couldn't process that request."
    else:
        return "Sorry, I couldn't understand your command."

def sleep_laptop():
    try:
        if platform.system() == "Windows":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            speak("Sorry, I can't put your laptop to sleep on this operating system.")
    except Exception as e:
        print(f"Error putting the laptop to sleep: {e}")
        speak("Sorry, I couldn't put the laptop to sleep.")

def play_song_on_youtube(song_name):
    search_query = song_name.replace(" ", "+")
    youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(youtube_search_url)
    speak(f"Searching for {song_name} on YouTube.")

def processCommand(command):
    if command == "start":
        return "Jarvis has started successfully!"
    return "Command not recognized"

def processCommand(c):
    if "stop it jarvis" in c.lower():
        speak("Bye boss, see you later!")
        exit()

    elif "generate essay on" in c.lower():
        topic = re.search(r"generate essay on (.+?)(?: (\d+))?(?: lines)?$", c.lower())
        if topic:
            topic_text = topic.group(1).strip()
            length = int(topic.group(2)) if topic.group(2) else 200
            essay = generate_essay(topic_text, length)
            if essay:
                speak(f"Essay generated successfully with {length} tokens. Opening Word to save the essay.")
                word, doc = open_word()
                save_path = r'C:\Path\To\Generated_Essay.docx'
                write_to_word(doc, essay, save_path)
                doc.Close()
                word.Quit()
                speak(f"Essay saved to Microsoft Word at {save_path}.")
            else:
                speak("Sorry, I couldn't generate the essay.")
        else:
            speak("Please specify a topic for the essay.")
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("open the song"):
        song = ' '.join(c.lower().split(" ")[1:])
        play_song_on_youtube(song)
    elif c.lower().startswith("reply to"):
        contact_name = c.lower().split("reply to ")[1].strip()
        reply_to_contact(contact_name)
    elif c.lower().startswith("increase volume"):
        times = get_volume_count(c)
        increase_volume(times)
    elif c.lower().startswith("decrease volume"):
        times = get_volume_count(c)
        decrease_volume(times)
    elif c.lower().startswith("play the song"):
        song = c.lower().replace("play the song", "").strip()
        if song:
            open_spotify()
            time.sleep(3)
            pyautogui.moveTo(461, 42, duration=1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.typewrite(song)
            time.sleep(2)
            pyautogui.moveTo(779, 347, duration=0.5)
            pyautogui.click()
            time.sleep(1)
            speak(f"This is the song {song} you are searching for.")
        else:
            speak("I didn't catch that! Can you please say it again?")
    elif c.lower().startswith("send message to"):
        parts = c.lower().split("send message to ")
        if len(parts) > 1:
            recipient_message = parts[1].strip()
            recipient_name = recipient_message.split(" ")[0]
            message = ' '.join(recipient_message.split(" ")[1:])
            phone_number = contacts.get(recipient_name)
            if phone_number:
                open_whatsapp()
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'f')
                time.sleep(1)
                pyautogui.typewrite(phone_number)
                time.sleep(2)
                pyautogui.moveTo(306, 284, duration=1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(863, 970, duration=0.5)
                pyautogui.click()
                time.sleep(1)
                pyautogui.typewrite(message)
                time.sleep(1)
                pyautogui.press('enter')
                speak(f"Message sent to {recipient_name}.")
            else:
                speak(f"Sorry, I don't have a contact saved as {recipient_name}.")
        else:
            speak("I didn't catch that. Please say the recipient's name and the message.")
    elif c.lower().startswith("call"):
        parts = c.lower().split("call ")
        if len(parts) > 1:
            target = parts[1].strip()
            phone_number = contacts.get(target)
            if phone_number:
                open_whatsapp()
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'f')
                time.sleep(1)
                pyautogui.typewrite(phone_number)
                time.sleep(2)
                pyautogui.moveTo(306, 284, duration=1)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(1805, 113, duration=0.5)
                pyautogui.click()
                time.sleep(1)
                speak(f"Calling {target} on WhatsApp.")
            else:
                speak(f"Sorry, I don't have a contact saved as {target}.")
        else:
            speak("Please specify a number or contact name to call.")
    elif "open spotify" in c.lower():
        os.startfile(r"C:\Path\To\Spotify.exe")
        speak("Opening Spotify")
    elif "open whatsapp" in c.lower():
        os.startfile(r"C:\Path\To\WhatsApp.exe")
        speak("Opening WhatsApp.")
    elif "put my laptop into sleep mode" in c.lower() or "sleep mode" in c.lower():
        speak("Putting the system into sleep mode. Good night boss!")
        sleep_laptop()
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't retrieve the news.")
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=1)
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("em kaavalo cheppu boss")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print(command)
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
