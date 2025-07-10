import pyttsx3
from pypdf import PdfReader


loct=input("Kindly Import the pdf for audiobook: ")

reader = PdfReader(loct)

a=int(input("Enter the page number to start reading from: "))
page= reader.pages[a]
text = page.extract_text()

speaker = pyttsx3.init()
speaker.say(text)
speak.runAndWait()  
