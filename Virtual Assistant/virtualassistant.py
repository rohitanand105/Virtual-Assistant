import pyttsx3  # For Text-to-Speech
import speech_recognition as sr  # For Speech Recognition
import wikipedia  # For Wikipedia Searches
import openai  # For ChatGPT-like responses
import wolframalpha  # For Math/Science Queries
import os
import subprocess
import webbrowser

# Initialize the TTS engine
engine = pyttsx3.init()

# OpenAI API Key
openai.api_key = "****"

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def take_command():
    """Capture voice input from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Microphone setup done. Listening...")
        recognizer.pause_threshold = 1
        try:
            print("Listening for audio...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Audio captured, recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition; {e}")
            return None

def open_youtube_in_chrome():
    """Open YouTube in Google Chrome."""
    try:
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Update if Chrome is installed elsewhere
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open("https://www.youtube.com")
        print("Opening YouTube in Chrome...")
    except Exception as e:
        print(f"Error opening YouTube in Chrome: {e}")

def open_whatsapp_desktop():
    whatsapp_path = r"C:\Program Files\WindowsApps\5319275A.WhatsAppDesktop_2.2450.6.0_x64__cv1g1gvanyjgm\WhatsApp.exe"
    try:
        os.startfile(whatsapp_path)
        print("Opening WhatsApp Desktop...")
    except FileNotFoundError:
        print("WhatsApp Desktop is not installed or the path is incorrect.")

def exit_whatsapp_desktop():
    """Terminate WhatsApp Desktop application."""
    try:
        os.system("taskkill /f /im WhatsApp.exe")
        print("WhatsApp Desktop has been closed.")
    except Exception as e:
        print(f"Error while closing WhatsApp Desktop: {e}")

def open_chrome():
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    try:
        os.startfile(chrome_path)
        print("Opening chrome")
    except FileNotFoundError:
        print("chrome not installed")

def search_wikipedia(query):
    """Search Wikipedia and return results."""
    speak("Searching Wikipedia...")
    results = wikipedia.summary(query, sentences=2)
    return results

def wolfram_query(app_id, query):
    """Query WolframAlpha for answers."""
    client = wolframalpha.Client(app_id)
    res = client.query(query)
    try:
        answer = next(res.results).text
        return answer
    except StopIteration:
        return "No results found."

def close_all_apps():
    """Close all user applications and folders."""
    try:
        process_list = subprocess.check_output("tasklist", shell=True).decode("utf-8")
        processes_to_skip = ["explorer.exe", "python.exe", "cmd.exe"]  # Add processes you want to skip

        print("Closing applications and folders...")
        for line in process_list.split("\n"):
            if ".exe" in line:
                process_name = line.split()[0]  # Extract process name
                if process_name.lower() not in processes_to_skip:
                    try:
                        os.system(f"taskkill /f /im {process_name}")
                        print(f"Closed: {process_name}")
                    except Exception as e:
                        print(f"Error closing {process_name}: {e}")

        print("All user applications and folders have been closed.")
    except Exception as e:
        print(f"An error occurred: {e}")

def ask_openai(prompt):
    """Generate a response using OpenAI's GPT."""
    try:
        response = openai.Chat.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful virtual assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error communicating with OpenAI: {e}"

# Main program
if __name__ == "__main__":
    speak("Initializing your personal assistant")
    while True:
        query = take_command()
        if query is None:
            continue
        
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            results = search_wikipedia(query)
            print(results)
            speak(results)
        
        elif "calculate" in query:
            app_id = "Your_WolframAlpha_App_ID"  # Add your WolframAlpha App ID here
            result = wolfram_query(app_id, query)
            print(result)
            speak(result)
        
        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a great day!")
            break

        elif "open whatsapp" in query:
            open_whatsapp_desktop()

        elif "close whatsapp" in query:
            exit_whatsapp_desktop()

        elif "close all" in query:
            close_all_apps()

        elif "open youtube" in query:
            open_youtube_in_chrome()
        
        elif "open chrome" in query:
            open_chrome()

        else:
            # Use OpenAI for handling general queries
            print("Querying OpenAI...")
            response = ask_openai(query)
            print(response)
            speak(response)
