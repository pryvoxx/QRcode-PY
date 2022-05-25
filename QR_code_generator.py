# generer des qrcodes avec python 

# importer les modules 
import qrcode 
import os 
from pystyle import Colors, Colorate, Write

# installer les modules 
os.system('pip install qrcode')
os.system('pip install pystyle')

# clear le terminal
os.system('cls')

banner = ("""
.▄▄▄  ▄▄▄       ▄▄·       ·▄▄▄▄  ▄▄▄ .
▐▀•▀█ ▀▄ █·    ▐█ ▌▪▪     ██▪ ██ ▀▄.▀·
█▌·.█▌▐▀▀▄     ██ ▄▄ ▄█▀▄ ▐█· ▐█▌▐▀▀▪▄
▐█▪▄█·▐█•█▌    ▐███▌▐█▌.▐▌██. ██ ▐█▄▄▌
·▀▀█. .▀  ▀    ·▀▀▀  ▀█▄▀▪▀▀▀▀▀•  ▀▀▀ ░         

Coded by pryvox
    """)
print(Colors.green + banner)

qu = Write.Input("Voulez vous générer un QR code (y/n) ->", Colors.green_to_yellow, interval=0.006)
if qu == 'y':
    x = ".png"
    quest = Write.Input("\ncomment voulez vous appeler le nom du fichier du QR code ->", Colors.green_to_yellow, interval=0.006)
    rs = Write.Input("\nMettez ce que vous voulez que le QR code contienne (lien) ->", Colors.green_to_yellow, interval=0.006)
    while True:
        img = qrcode.make('' + rs)
        img.save('' + quest + x)
        Write.Print("\nSUCCESS\n", Colors.green_to_yellow, interval=0.1)
        
else:
    exit()
