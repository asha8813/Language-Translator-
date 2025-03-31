
import tkinter as tk
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

dic = {
    
    'afrikaans': 'af', 'arabic': 'ar', 'bengali': 'bn' , 'chinese': 'zh',
    'dutch': 'nl', 'english': 'en', 'french': 'fr', 'german': 'de',
    'greek': 'el', 'hindi': 'hi', 'italian': 'it', 'japanese': 'ja', 'korean':
    'ko', 'latin': 'la', 'nepali': 'ne', 'punjabi': 'pa', 'spanish': 'es', 
    'tamil': 'ta', 'urdu': 'ur' , 'sanskrit' : 'sa'
       
}

class VoiceTranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Voice Translator")

        # Load the image
        self.image = tk.PhotoImage(file="C:/Users/mahla/OneDrive/Pictures/Picture1.png")

        # Create a label to display the image
        self.image_label = tk.Label(master, image=self.image)
        self.image_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.label = tk.Label(master, text="Enter the sentence to translate:")
        self.label.grid(row=1, column=0, columnspan=2, pady=10)

        self.entry = tk.Entry(master)
        self.entry.grid(row=2, column=0, columnspan=2, pady=10)

        self.translate_button = tk.Button(master, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.translation_label = tk.Label(master, text="")
        self.translation_label.grid(row=4, column=0, columnspan=2, pady=10)

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            return "None"
        return query

    def destination_language(self):
        print("Enter the language in which you want to convert: Ex. Hindi, English, etc.")
        print()

        to_lang = self.take_command()
        while to_lang == "None":
            to_lang = self.take_command()
        to_lang = to_lang.lower()
        return to_lang

    def translate_text(self):
        query = self.entry.get()
        to_lang = self.destination_language()

        while to_lang not in dic:
            print("Language is currently not available, please input some other language")
            print()
            to_lang = self.destination_language()

        to_lang = dic[to_lang]
        translator = Translator()
        text_to_translate = translator.translate(query, dest=to_lang)
        text = text_to_translate.text

        speak = gTTS(text=text, lang=to_lang, slow=False)
        speak.save("captured_voice.mp3")

        playsound('captured_voice.mp3')
        os.remove('captured_voice.mp3')

        self.translation_label.config(text=f"Translated Text: {text}")

# Create the Tkinter window
root = tk.Tk()
app = VoiceTranslatorApp(root)

# Run the Tkinter main loop
root.mainloop()


'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

dic = {
    
	 'afrikaans': 'af', 'arabic': 'ar', 'bengali': 'bn' , 'chinese (simplified)':
    'zh-cn', 'dutch': 'nl', 'english': 'en', 'french': 'fr', 'german': 'de',
    'greek': 'el', 'hindi': 'hi', 'italian': 'it', 'japanese': 'ja', 'korean':
    'ko', 'latin': 'la', 'nepali': 'ne', 'punjabi': 'pa', 'spanish': 'es', 
    'tamil': 'ta', 'urdu': 'ur' , 'sanskrit' : 'sa'
       
}


class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Translator")
        
        # Load the image
        image = Image.open("C:/Users/mahla/OneDrive/Pictures/Picture1.png")  # Replace with the path to your image file
        image = image.resize((100, 100), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(image)

        # Create a label to display the image
        img_label = tk.Label(root, image=self.img)
        img_label.grid(row=0, column=3, rowspan=4, padx=10, pady=10)

        # Entry for user input
        self.input_entry = ttk.Entry(root, width=50)
        self.input_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Button to initiate translation
        translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
        translate_button.grid(row=1, column=1, pady=10)

        # Dropdown for selecting source language
        self.from_lang_var = tk.StringVar()
        self.from_lang_var.set("Select Source Language")
        self.from_lang_dropdown = ttk.Combobox(root, textvariable=self.from_lang_var, values=list(dic.keys()))
        self.from_lang_dropdown.grid(row=2, column=0, padx=10, pady=10)

        # Dropdown for selecting destination language
        self.to_lang_var = tk.StringVar()
        self.to_lang_var.set("Select Destination Language")
        self.to_lang_dropdown = ttk.Combobox(root, textvariable=self.to_lang_var, values=list(dic.keys()))
        self.to_lang_dropdown.grid(row=2, column=1, padx=10, pady=10)

        # Label to display translated text
        self.translated_label = ttk.Label(root, text="")
        self.translated_label.grid(row=3, column=0, columnspan=3, pady=10)

    def take_command(self):
        # Implement the take command logic from your existing code here
        pass

    def translate_text(self):
        # Implement the translation logic using the provided input and language selections
        # Update the translated_label with the result
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()

'''
