from PyPDF2 import PdfReader
from gtts import gTTS


text_p = ""
reader = PdfReader('Read.pdf')  # replace with desired file
n_pages = len(reader.pages)
for i in range(n_pages):
    page = reader.pages[i]
    text_p += page.extract_text()

language = 'en'

myobj = gTTS(text=text_p,lang=language,slow=False)

myobj.save("play,mp3")

