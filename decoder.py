import stepic
from PIL import Image
from cryptography.fernet import Fernet

key= input("KEY: ")
dec=Fernet(key)

file=input("PHOTO: ") 

img=Image.open(file)
decoded=stepic.decode(img)
text_dec=dec.decrypt(decoded.encode())

print("The hidden text is: "+text_dec.decode())
