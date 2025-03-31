# Importing necessary modules required 
from playsound import playsound 
import speech_recognition as sr 
from translate import Translator
from gtts import gTTS 
import os


dic = {
    
	'afrikaans': 'af', 'arabic': 'ar', 'bengali': 'bn' , 'chinese': 'zh',
    'dutch': 'nl', 'english': 'en', 'french': 'fr', 'german': 'de',
    'greek': 'el', 'hindi': 'hi', 'italian': 'it', 'japanese': 'ja', 'korean':
    'ko', 'latin': 'la', 'nepali': 'ne', 'punjabi': 'pa', 'spanish': 'es', 
    'tamil': 'ta', 'urdu': 'ur' , 'sanskrit' : 'sa' 
       
}

# Function to convert Hindi to English
def translate_func(from_lang='en', to_lang='hi', text='hello'):
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    translation = translator.translate(text)
    return translation

# Capture Voice 
# takes command through microphone 
def takecommand(): 
	r = sr.Recognizer() 
	with sr.Microphone() as source: 
		print("listening.....") 
		r.pause_threshold = 1
		audio = r.listen(source) 

	try: 
		print("Recognizing.....") 
		query = r.recognize_google(audio, language='en-in') 
		print(f"user said {query}\n") 
	except Exception as e: 
		print("say that again please.....") 
		return "None"
	return query 

# Taking voice input from the user 
query = takecommand() 
while (query == "None"): 
	query = takecommand() 
 
def from_language(): 
	print("Enter the language from which you want to convert (Ex. Hindi , English , etc.)")
	print()
	from__lang = takecommand() 
	while (from__lang == "None"): 
		from__lang = takecommand() 
	from__lang = from__lang.lower()
	return from__lang 
 
def destination_language(): 
	print("Enter the language in which you want to convert (Ex. Hindi , English , etc.)") 
	print() 

	# Input destination language in which the user 
	# wants to translate 
	to_lang = takecommand() 
	while (to_lang == "None"): 
		to_lang = takecommand() 
	to_lang = to_lang.lower()
	return to_lang 

from__lang = from_language() 

# Mapping it with the code 
while (from__lang not in dic): 
	print("Language in which you are trying to convert from is currently not available ,please input some other language") 
	print() 
	from__lang = from_language() 

from__lang = dic[from__lang]
print(from__lang)

to_lang = destination_language() 

# Mapping it with the code 
while (to_lang not in dic): 
	print("Language in which you are trying to convert is currently not available ,please input some other language") 
	print() 
	to_lang = destination_language() 

to_lang = dic[to_lang]
print(to_lang)


# Translating from src to dest 
translated_text = translate_func(from_lang=from__lang, to_lang=to_lang, text=query)

# Using Google-Text-to-Speech ie, gTTS() method 
# to speak the translated text into the 
# destination language which is stored in to_lang. 
# Also, we have given 3rd argument as False because 
# by default it speaks very slowly 
speak = gTTS(text=translated_text, lang=to_lang, slow=False) 

# Using save() method to save the translated 
# speech in capture_voice.mp3 
speak.save("captured_voice.mp3") 

# Using OS module to run the translated voice. 
playsound('captured_voice.mp3') 
os.remove('captured_voice.mp3') 
print(translated_text) 
