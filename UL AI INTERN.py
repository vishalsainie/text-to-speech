# import speech_recognition as sr
# import pyttsx3

# # initialise the recognizer
# r = sr.Recognizer()

# def record_text():
#     # loop in case of errors
#     while(1):
#         try:
#             # use the mic as the i/p source
#             with sr.Microphone() as source2:
#                 # prepare recognizer to recieve input
#                 r.adjust_for_ambient_noise(source2, duration=0.2)
                
#                 # listen for user i/p
#                 audio2=r.listen(source2)

#                 # use google to recognize audio
#                 MyText=r.recognize_google(audio2)

#         except sr.RequestError as e:
#             print("could not request result; {0}". format(e))
        
#         except sr.UnknownValueError:
#             print("Unknown error occured")
    
#     return

# def output_text():
#     # create a file that will have our o/p and in that file append the generated o/p at the end if more o/p is generated
#     f=open("output.txt", "a")
#     f.write(text)

#     # \n as when we say multiple things we will have the thing in new line always
#     f.write("\n")
#     f.close()
#     return

# while(1):
#     text=record_text()
#     output_text(text)
#     print("speech converted to text")

import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

def record_text(retries=3):
    for attempt in range(retries):
        try:
            # Use the microphone as the input source
            with sr.Microphone() as source2:
                print("Adjusting for ambient noise, please wait...")
                r.adjust_for_ambient_noise(source2, duration=1)  # Increased duration
                
                print("Please speak clearly into the microphone...")
                # Listen for user input
                audio2 = r.listen(source2)
                
                print("Recognizing speech...")
                # Use Google to recognize audio
                MyText = r.recognize_google(audio2)
                print("You said: " + MyText)
                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            log_error(f"RequestError: {e}")
            return None
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio. Please try again.")
            log_error("UnknownValueError: Could not understand audio.")

    return None  # Return None if all retries fail

def output_text(text):
    if text:  # Check if text is not None
        with open("output.txt", "a") as f:
            f.write(text + "\n")
        print("Text written to file.")
    else:
        print("No text to write")

def log_error(error_message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(error_message + "\n")

while True:
    text = record_text()
    if text:  # Proceed only if text was successfully recognized
        output_text(text)
        print("Speech converted to text and written to file")
