import binascii
import random

def generuj_klucz(p):
    
    klucz = ""
    p = int(p)
    
    for i in range(p):
        
        temp = random.randint(0,1)
        temp = str(temp)
        klucz = klucz + temp
        
    return(klucz)

def xor(a,b,n):
    
    temp = ""
    
    for i in range(n):
        if (a[i] == b[i]):
            temp += "0"
        else:
            temp += "1"
            
    return temp

def BinToDec(pt_Ascii):
    string = int(pt_Ascii, 2)
    return string

def TexttoAscii(plaintext):
    pt_Ascii = [ord(x) for x in plaintext]
    return pt_Ascii

def AsciitoBin(pt_Ascii):
    PT_Bin = [format(y,'08b') for y in pt_Ascii]
    PT_Bin = "".join(PT_Bin)
    return PT_Bin

def BintoText(bin_text):
    ciphertext = ""
    for i in range(0, len(bin_text), 7):
        temp = bin_text[i:i + 7]
        Ascii_Text = BinToDec(temp)
        ciphertext = ciphertext + chr(Ascii_Text)
    return ciphertext

        
        



def Encrypt(plaintext, flag):

    pt_Ascii = TexttoAscii(plaintext)
    pt_bin = AsciitoBin(pt_Ascii)
    n = int(len(pt_bin)//2)
    klucz1 = generuj_klucz(n)
    klucz2 = generuj_klucz(n)
    L1 = pt_bin[0:n]
    R1 = pt_bin[n::]
    r = len(R1)
    #Pierwsza Runda
    F1 = xor(R1,klucz1,n)
    R2 = xor(F1,L1,n)
    L2 = R1
    #Druga Runda
    F2 = xor(R2,klucz2,n)
    R3 = xor(F2,L2,n)
    L3 = R2
    #Szyfrogram
    bin_text = L3 + R3
    ciphertext = BintoText(bin_text)

    if flag:
        
        L4 = L3
        R4 = R3
        F3 = xor(L4,klucz2,n)
        L5 = xor(R4,F3,n)
        R5 = L4
        F4 = xor(L5,klucz1,n)
        L6 = xor(R5,F4,n)
        R6 = L5
        PT = L6+R6
        PT = int(PT, 2)
        PT = binascii.unhexlify( '%x'% PT)
        print("PLAINTEXT: ", PT)


    return ciphertext

if __name__ == "__main__":
    plaintext = "Warszawa"
    print(Encrypt(plaintext, True))
    