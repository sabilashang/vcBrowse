import speech_recognition as sr
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the web browser
browser = webdriver.Chrome()
browser.get("https://google.com")
time.sleep(1)

# Function to perform actions based on voice commands
def perform_action(command):
    if "search" in command:
        # Perform a search
        search_query = command.replace("search", "").strip()
        search_box = browser.find_element(By.XPATH,'//*[@id="APjFqb"]')
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    elif "type" in command:
        # Type into the text box
        text_to_type = command.replace("type", "").strip()
        text_box = browser.find_element(By.XPATH,'//*[@id="APjFqb"]')
        text_box.send_keys(text_to_type, " ")

    elif "delete" in command:
        # Delete the last word
        text_box = browser.find_element(By.XPATH,'//*[@id="APjFqb"]')
        text_box.send_keys(Keys.CONTROL + Keys.BACKSPACE)

    elif "thank you for your service" in command:
        # Termination of Program
        print("Terminating...")
        exit()

# Function to listen for voice commands
def listen_for_commands():
    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("Command:", command)
        perform_action(command)

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Loop to continuously listen for commands
while True:
    listen_for_commands()
