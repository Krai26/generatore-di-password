def generatore_di_password():
    convalida="y"
    while convalida=="y" or convalida=="Y":
        generatore ()
        convalida= input ('''Per riutilizzare il programma digita "y" o "Y".Per uscire digita un tasto qualunque ''')
        print("Grazie per aver utilizzato il programma!")

def generatore ():
    import random

    print ('''GENERATORE DI PASSWORD''')
    caratteri= '''abcdefghijklmnopqrstuwxyz1234567890ABCDEFGHIJKLMNOPQRSTUWXYVZ!"£$%&/()=?^|\*+§°#:_;,.->[}{]'''

    lunghezza= int (input ('''Digita la lunghezza della password:'''))

    password = ""

    for x in range (lunghezza):
        password+= random.choice (caratteri)

        print("Password generata:", password)

generatore_di_password()