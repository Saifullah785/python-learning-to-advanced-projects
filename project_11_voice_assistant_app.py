import pyttsx3 # Import the text-to-speech conversion library (pip install pyttsx3)
import speech_recognition as sr # Import the speech recognition library (pip install SpeechRecognition)
import datetime # Import the datetime module to work with dates and times
import wikipedia # Import the wikipedia library to fetch summaries (pip install wikipedia)
import webbrowser # Import the webbrowser module to open web pages
import os # Import the os module to interact with the operating system
import smtplib # Import the smtplib module to send emails



# Initialize the pyttsx3 engine with the SAPI5 voice (Windows speech API)
engine = pyttsx3.init('sapi5') 

# Get the available voices from the speech engine
voices = engine.getProperty('voices') 

# print(voices[1].id) # (Optional) Print the ID of the second available voice

# Set the voice to the first available voice (usually male)
engine.setProperty('voice', voices[0].id) 

# Define a function to convert text to speech
def speak(audio): 
    engine.say(audio) # Queue the text to be spoken
    engine.runAndWait() # Process the voice queue and speak the text


 # Define a function to greet the user based on the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)  # Get the current hour as an integer
    if hour>=0 and hour<12:   # If the hour is between 0 and 12 (morning)
        speak("Good Morning!")   # Say Good Morning
    elif hour>=12 and hour<18:   # If the hour is between 12 and 18 (afternoon)
        speak("Good Afternoon!")   # Say Good Afternoon
    else:                          # If the hour is 18 or later (evening)
        speak("Good Evening!")      # Say Good Evening
    speak("I am Jarvis Sir. Please tell me how may I help you")       # Introduce Jarvis and ask for a command


# Define a function to take voice input from the user and return it as a string
def takeCommand(): 
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() # Create a Recognizer object for speech recognition

    with sr.Microphone() as source: # Use the microphone as the audio source
        print("Listening...") # Print a message indicating listening has started
        r.pause_threshold = 1 # Set the pause threshold to 1 second
        audio = r.listen(source) # Listen for the first phrase and extract it into audio data

    try:
        print("Recognizing...")    # Print a message indicating recognition has started
        query = r.recognize_google(audio, language='en-in') # Recognize speech using Google Speech Recognition
        print(f"User said: {query}\n") # Print what the user said

    except Exception as e: # If an error occurs during recognition
        # print(e)    # (Optional) Print the error
        print("Say that again please...")  # Ask the user to repeat
        return "None" # Return "None" if recognition fails
    
    return query # Return the recognized text

# Define a function to send an email

def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to Gmail SMTP server on port 587
    server.ehlo() # Identify to the server
    server.starttls() # Start TLS encryption for security
    server.login('youremail@gmail.com', 'your-password') # Login with your email and password
    server.sendmail('youremail@gmail.com', to, content) # Send the email from your email to the recipient with the content
    server.close() # Close the connection to the SMTP server

# If this script is run directly (not imported)
if __name__ == "__main__": 
    wishMe() # Greet the user

    # Run an infinite loop to continuously listen for commands
    while True: 
        # if 1: # (Optional) Use this for debugging to run the loop once
        query = takeCommand().lower() # Take command from user and convert it to lowercase


        # Logic for executing tasks based on query
        # If the command contains 'wikipedia'
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') # Inform the user that Wikipedia is being searched
            query = query.replace("wikipedia", "") # Remove 'wikipedia' from the query
            results = wikipedia.summary(query, sentences=2) # Get a summary from Wikipedia (2 sentences)
            speak("According to Wikipedia") # Speak the source
            print(results) # Print the summary
            speak(results) # Speak the summary

        elif 'open youtube' in query: # If the command is to open YouTube
            webbrowser.open("youtube.com") # Open YouTube in the default web browser

        elif 'open google' in query: # If the command is to open Google
            webbrowser.open("google.com") # Open Google in the default web browser

        elif 'open stackoverflow' in query: # If the command is to open Stack Overflow
            webbrowser.open("stackoverflow.com")   # Open Stack Overflow in the default web browser

        elif 'play music' in query: # If the command is to play music
            music_dir = '' # Specify your music directory path here
            songs = os.listdir(music_dir) # List all files in the music directory
            print(songs)    # Print the list of songs
            os.startfile(os.path.join(music_dir, songs[0])) # Play the first song in the directory

        elif 'the time' in query: # If the command is to tell the time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    # Get the current time as a string
            speak(f"Sir, the time is {strTime}") # Speak the current time

        elif 'open code' in query: # If the command is to open code editor or a specific application
            codePath = "" # Specify the path to your code editor or application
            os.startfile(codePath) # Open the application at the specified path

        elif 'email to saif' in query: # If the command is to send an email to Saif
            try:
                speak("What should I say?") # Ask the user for the email content
                content = takeCommand() # Take the content from the user's voice
                to = "saifyourEmail@gmail.com"    # Specify the recipient's email address
                sendEmail(to, content) # Send the email
                speak("Email has been sent!") # Inform the user that the email was sent
            except Exception as e: # If an error occurs while sending the email
                print(e) # Print the error
                speak("Sorry my friend saif bhai. I am not able to send this email") # Inform the user of the