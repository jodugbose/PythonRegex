import tkinter as tk
from tkinter import ttk
from tkinter import *
from translate import Translator
import cv2
from PIL import Image
import threading
import easyocr
from gtts import gTTS
import os
from tkinter import PhotoImage
from PIL import ImageTk, Image
from tkinter import Tk, Label

Window = tk.Tk()
Window.title("Weaver's Text Detection & Translator")
screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()
Window.geometry(f"{screen_width}x{screen_height}")
Window.configure(bg="#E0F2F1") 

# Supported languages for translation
your_languages = ['en']
Languages = {'Hindi', 'German', 'English', 'French', 'Spanish', 'Japanese', 'Latin',
            'Chinese', 'Russian', 'Italian', 'Korean', 'Arabic', 'Igbo', 'Yoruba', 'Hausa', 'Croatian'}
language_map = {'English': 'en','Hindi': 'hi','German': 'de','French': 'fr','Spanish': 'es','Japanese': 'ja',
    'Latin': 'la','Chinese': 'zh','Russian': 'ru','Italian': 'it','Korean': 'ko','Arabic': 'ar',
    'Igbo': 'ig','Yoruba': 'yo','Hausa': 'ha','Croatian': 'hr'}
 

Input_lang = StringVar()
Output_lang = StringVar()
Input_lang.set('English')
Output_lang.set('French')

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=6, font=("Arial", 12, "bold"), background="#008CBA", foreground="white")
style.configure("TLabel", font=("Arial", 14), foreground="#333", background = "#E0F2F1")

def resize_image(imagePath, new_width, new_height):
    img = Image.open(imagePath)
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    return resized_img

def webcam_and_detect():
    def start_webcam():
        camera = cv2.VideoCapture(0)
        while True: 
            _, image = camera.read()
            cv2.imshow("Text Detection", image)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                cv2.imwrite('spanishimg.jpg', image)
                detected_text = ocr('spanishimg.jpg')
                TextVar.delete("1.0", "end")  # Clear existing text
                TextVar.insert("1.0", detected_text)
                # TextVar.set(detected_text)
                break
        camera.release()
        cv2.destroyAllWindows()
        resized_img1 = resize_image('spanishimg.jpg', 600, 400)
        detected_text = ocr(resized_img1) 
        translate_text() 
    # Create a new thread to run the webcam capture in the background
    webcam_thread = threading.Thread(target=start_webcam)
    webcam_thread.start()


def ocr(image):
    reader = easyocr.Reader(your_languages)  # Specify the languages you want to support
    result = reader.readtext(image)
    if not result:
        return "No text detected"
    detected_text = ""
    for detection in result:
        detected_text += detection[1] + " "  # Concatenate the detected text
    return detected_text

# Function to handle translation
def translate_text():
    global translating
    detected_text = TextVar.get('1.0', tk.END)
    translator = Translator(from_lang=Input_lang.get(), to_lang=Output_lang.get())
    Translation = translator.translate(detected_text)
    print(Translation)
    TranslatedTextBox.delete('1.0', tk.END)  # Clear existing text
    TranslatedTextBox.insert(tk.END, Translation)
    translating = False 

def on_output_lang_change(*args):
    try:
        translate_text()
    except Exception as e:
        print("Translation error:", e)

def on_output_lang_change(*args):
    if not translating:  # Check if the change is not due to translation
        translate_text()
Output_lang.trace("w", on_output_lang_change)

def translate_to_speech():
    translated_text = TranslatedTextBox.get('1.0', tk.END)  
    target_language = language_map[Output_lang.get()]
    print("Translated Text:", translated_text)
    try:
        tts = gTTS(text=translated_text, lang=target_language, slow=False)
        temp_voice = 'speech.mp3'
        tts.save(temp_voice)
        os.system(f'mediaplayer {temp_voice}')
    except ValueError as e:
        print("Error:", e) 

def translate_text_button():
    global translating
    translating = True
    translate_text()

# Create the widgets for the GUI
top_message = ttk.Label(Window, background="#E0F2F1", foreground="red" ,text="Click the 'Start Webcam' button to capture video from the webcam", style="TLabel")
top_message.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

start_button = ttk.Button(Window, text="Start Webcam", command=webcam_and_detect, style="TButton")
start_button.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

Label(Window, background="#E0F2F1", text="Choose a Language:", font=("Arial", 14)).grid(row=2, column=0, padx=50, pady=10, sticky='w')
InputLanguageChoiceMenu = OptionMenu(Window, Input_lang, *Languages)
InputLanguageChoiceMenu.grid(row=2, column=0, padx=250, pady=10, sticky='w')

Label(Window, background="#E0F2F1",text="Translated Language:", font=("Arial", 14)).grid(row=2, column=3, padx=150, pady=10, sticky='e')
NewLanguageChoiceMenu = OptionMenu(Window, Output_lang, *Languages)
NewLanguageChoiceMenu.grid(row=2, column=3, padx=50, pady=10, sticky='e')

Label(Window, text="Detected Text:", bg="#E0F2F1", font=("Arial", 14), foreground="blue").grid(row=5, column=0, padx=50, pady=10, sticky='w')
initial_text = "Detected text will appear here..."
TextVar = tk.Text(Window, font=("Arial", 14), wrap=tk.WORD, width=40, height=10)
TextVar.grid(row=6, column=0, padx=10, pady=10, sticky='w')
TextVar.insert("1.0", initial_text)
TextVar.tag_configure("faint", foreground="gray")
# Apply the tag to the initial text
TextVar.tag_add("faint", "1.0", "1.end")

 
Label(Window, background="#E0F2F1",text="Translated Text:", font=("Arial", 14), foreground="blue").grid(row=5, column=0, columnspan=4, padx=50, pady=10, sticky="e")
initial_text = "Translated text will appear here..."
TranslatedTextBox = tk.Text(Window, font=("Arial", 14), wrap=tk.WORD, width=40, height=10)
TranslatedTextBox.insert("1.0", initial_text)
TranslatedTextBox.grid(row=6, column=3, padx=10, pady=10, sticky='e')
TranslatedTextBox.tag_configure("faint", foreground="gray")
# Apply the tag to the initial text
TranslatedTextBox.tag_add("faint", "1.0", "1.end")

#Load the image
fast_forward_img = Image.open("fast-foward.png")
desired_width = 70
desired_height = 70
fast_forward_img.thumbnail((desired_width, desired_height), Image.LANCZOS)
# Convert the resized image to PhotoImage
resized_image1 = ImageTk.PhotoImage(fast_forward_img)
image_label = Label(Window, background="#E0F2F1",image=resized_image1)
image_label.bind("<Button-1>", lambda event: translate_text_button())
image_label.place(x=600, y=420)

speech_img = Image.open("speaking.png") 
desired_width = 50
desired_height = 50
speech_img.thumbnail((desired_width, desired_height), Image.LANCZOS)
resized_image2 = ImageTk.PhotoImage(speech_img)
image_label = Label(Window, background="#E0F2F1",image=resized_image2)
image_label.bind("<Button-1>", lambda event: translate_to_speech())
image_label.place(x=600, y=560)

 
Label(Window, background="#E0F2F1",text="Text Translate", font=("Arial", 14), foreground="navy blue").place(x=550,y=400)
Label(Window, background="#E0F2F1",text="Voice Translate", font=("Arial", 14), foreground="navy blue").place(x=550,y=528)

# TextVar = StringVar()
TargetLanguageChoice = StringVar()

scrollbar = tk.Scrollbar(Window, command=TranslatedTextBox.yview)
scrollbar.grid(row=6, column=4, sticky='ns')
TranslatedTextBox.config(yscrollcommand=scrollbar.set)


for col in range(4):
    Window.grid_columnconfigure(col, weight=1)

for row in range(9):
    Window.grid_rowconfigure(row, weight=1)

Window.mainloop()