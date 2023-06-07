# 201805051 - Utku Enes Baki

# Importing necessary libraries
from tkinter import *
import tkinter.font as tkFont
import imutils
import cv2
from tkinter import filedialog as fd
import pytesseract
from tkinter import messagebox
from PIL import ImageTk, Image
from langdetect import detect
import pygame
from translate import Translator

# Initialize pygame
pygame.init()

# Creating array data structures with empty lists for further storage
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
translations = []
originalSentences = []

# For click sound, I've imported pygame above
def play_mp3():
    # Load and play the MP3 file
    pygame.mixer.music.load('sound/mouse-click.mp3')
    pygame.mixer.music.play()

#Selecting the image
def open_selected_image():
    play_mp3()
    global selectedImage, textImage, translatedImage
    try:
        file_path = fd.askopenfilename(title='Choose Photograph',
                                       filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))
        if not file_path:
            raise ValueError("No file selected")

        print("Path Is: " + file_path)
        selectedImage = cv2.imread(file_path)
        selectedImage = imutils.resize(selectedImage, width=600)
        textImage = selectedImage.copy()
        translatedImage = selectedImage.copy()
        originalSentences.clear()
        translations.clear()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


#Optical Character Recognition (OCR)-x,y,w,h represents coordinates and dimensions of a bounding box around text (with cv2.rectangle())
def ocr_image():
    play_mp3()
    try:
        data=pytesseract.image_to_data(selectedImage)
        for z,a in enumerate(data.splitlines()):
                if z!=0:
                    a=a.split()
                    if(len(a)==12):
                        x,y,w,h=int(a[6]),int(a[7]),int(a[8]),int(a[9])
                        #Select text with rectangles
                        cv2.rectangle(selectedImage,(x,y),(x+w,y+h),(0,255,0),1)
        #Showing the OCR image
        cv2.imshow('Image To OCR',selectedImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print("No image found.")

# Showing the text
def from_image_to_text():
    play_mp3()
    try:
        config = r'--oem 3 --psm 6 -l eng+tur+deu+fra+ita+spa'
        text = pytesseract.image_to_string(textImage, config=config)
        if len(originalSentences) == 0:
            originalSentences.append(text)
            #Printing the text with messagebox
            messagebox.showinfo("Target Text", f"Text on Image : \n{originalSentences[0]}")
            # Global language variable declaration for further usage
            global language
            language = detect(originalSentences[0])
            print("Sentences added to list")
            print(f"Detected language is: {language}")
    except:
        print("No image selected")

# From text to translation
def text_to_translate():
    play_mp3()
    if len(originalSentences) == 0:
        print("No text to translate")
    else:
        # Define the target languages and the translation to Turkish ("tr")
        target_languages = ['en', 'de', 'fr', 'es', 'it']
        target_language_tr = 'tr'
        translations = []

        for sentence in originalSentences:
            for lang in target_languages:
                # English
                if (language == 'en'):
                    try:
                        # Translate the text to Turkish
                        translator = Translator(from_lang='en', to_lang=target_language_tr)
                        translated = translator.translate(sentence)
                        translations.append(translated)
                        break  # Exit the inner loop after the first successful translation

                    except Exception as e:
                        print("Error:", e)

                    if len(translations) > 0:
                        break  # Exit the outer loop after the first successful translation

                # German
                if (language == 'de'):
                    try:
                        # Translate the text to Turkish
                        translator = Translator(from_lang='de', to_lang=target_language_tr)
                        translated = translator.translate(sentence)
                        translations.append(translated)
                        break  # Exit the inner loop after the first successful translation

                    except Exception as e:
                        print("Error:", e)

                    if len(translations) > 0:
                        break  # Exit the outer loop after the first successful translation

                # French
                if (language == 'fr'):
                    try:
                        # Translate the text to Turkish
                        translator = Translator(from_lang='fr', to_lang=target_language_tr)
                        translated = translator.translate(sentence)
                        translations.append(translated)
                        break  # Exit the inner loop after the first successful translation

                    except Exception as e:
                        print("Error:", e)

                    if len(translations) > 0:
                        break  # Exit the outer loop after the first successful translation

                # Spanish
                elif (language == 'es'):
                    try:
                        # Translate the text to Turkish
                        translator = Translator(from_lang='es', to_lang=target_language_tr)
                        translated = translator.translate(sentence)
                        translations.append(translated)
                        break  # Exit the inner loop after the first successful translation

                    except Exception as e:
                        print("Error:", e)

                    if len(translations) > 0:
                        break  # Exit the outer loop after the first successful translation

                # Italian
                elif (language == 'it'):
                    try:
                        # Translate the text to Turkish
                        translator = Translator(from_lang='it', to_lang=target_language_tr)
                        translated = translator.translate(sentence)
                        translations.append(translated)
                        break  # Exit the inner loop after the first successful translation

                    except Exception as e:
                        print("Error:", e)

                    if len(translations) > 0:
                        break  # Exit the outer loop after the first successful translation

                # For further language addition, this conditional state will be empty for now...
                else:
                    pass

        # Displaying the translated text in a messagebox
        if len(translations) > 0:
            # Join the translations into a single string
            translations_text = '\n'.join(translations)

            messagebox.showinfo("Translated Text", f"Text on Image:\n{originalSentences[0]}\n\nTranslation to Turkish:\n{translations_text}")

            originalSentences.clear()
            translations.clear()

#-------------------------------------------------- GUI --------------------------------------------------

#Sepya-#bfab50
#Facebook_Blue-#0394fc

window=Tk()

window.geometry('1200x580')
window.resizable(0, 0)
window.config(background="#ebe8e8")
window.title('Recognition Of Text From Image')
icon = PhotoImage(file='icons/favicon.png')
window.iconphoto(True,icon)

fontSettings = tkFont.Font(family='Helvetica',weight='bold')

label1 = Label(window,
              text="Recognition of Text from Image",
              font=('Arial', 25,'bold'),
              fg='white',
              bg='#5D5326',
              relief=RAISED,
              bd=10,
              padx=10,
              pady=10)

selectPhotoButton = Button(window,
                           text='Choose Photograph',
                           fg='white',
                           bg='#9e8d3e',
                           command=open_selected_image,
                           font=('Courier New', 24,'bold'),
                           width=20,
                           borderwidth=4)

ocrButton = Button(window,
                   text='Optical Character Recognition',
                   fg='white',
                   bg='#9e8d3e',
                   command=ocr_image,
                   font=('Courier New', 22,'bold'),
                   width=30,
                   borderwidth=4)

textButton = Button(window,
                    text='Show Text',
                    fg='white',
                    bg='#9e8d3e',
                    command=from_image_to_text,
                    font=('Courier New', 24,'bold'),
                    width=20,
                    borderwidth=4)

translatedButton = Button(window,
                          text='Translated Text',
                          fg='white',
                          bg='#9e8d3e',
                          command=text_to_translate,
                          font=('Courier New', 24,'bold'),
                          width=20,
                          borderwidth=4)

exitButton = Button(window,
                    text='Quit',
                    fg='white',
                    bg='#FF605C',
                    command=window.destroy,
                    font=('Courier New', 24,'bold'),
                    width=20,
                    borderwidth=4)

# Button placements
selectPhotoButton.place(x=660, y=110)
ocrButton.place(x=660, y=202)
textButton.place(x=660, y=290)
translatedButton.place(x=660, y=380)
exitButton.place(x=660, y=470)

label1.place(x=660, y=15)

# Importing the GUI page image
image2 = ImageTk.PhotoImage(Image.open("icons/picture.png"))

# Create a Label Widget to display the GUI image
label = Label(window,
              image = image2,)
label.place(x=-2, y=-2)

window.mainloop()