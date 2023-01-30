
import math
import numpy as np

alphabet = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','W','V','X','Y','Z']



def koordynaty(litera,macierz):
    p = [0,0]
    for i in range(5):
        for j in range(5):
            if macierz[i][j] == litera:
                p[0] = i
                p[1] = j
    return p
                


def cleanup_k(key):
    ready_key = []
    key = key.upper()
    key = key.replace(' ', '')
    key = key.replace('J', 'I')
    for k in key:
        if k not in ready_key:
            ready_key += k
        else:
            pass
    return ready_key


def cleanup_pt(plaintext):
    ready_text = []
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("J","I")
    plaintext = plaintext.replace(" ", "")
    ready_text += plaintext[0]
    for p in range(1,len(plaintext)):
        if plaintext[p] == plaintext[p-1]:
            ready_text += alphabet[22]
            ready_text += plaintext[p]     
        else:
            ready_text += plaintext[p]
    if len(ready_text) % 2 != 0:
        ready_text += alphabet[22]
    return ready_text

def stworz_macierz(ready_key):
    A = ready_key
    M = [[0 for n in range(5)] for m in range(5)]
    for i in range(len(alphabet)):
        if alphabet[i] not in A:
            A += alphabet[i]
        else:
            pass
    for r in range(5):
        for k in range(5):
            M[k][r] = A[0]
            if len(A) != 0:
                A.pop(0)
    return M

def enkrypcja(ready_text, M):
    szyfrogram = []
    for l in range(0,len(ready_text),2):
        kord1 = koordynaty(ready_text[l], M)
        kord2 = koordynaty(ready_text[l+1], M)
        print(kord1)
        print(kord2)
        
        if kord1[0] == kord2[0]: #wiersze takie same
            szyfrogram += M[(kord1[0]+1)%5][kord1[1]]
            szyfrogram += M[(kord2[0]+1)%5][kord2[1]]
        
        if kord1[1] == kord2[1]: #kolumny te same
            szyfrogram += M[kord1[0]][(kord1[1]+1)%5]
            szyfrogram += M[kord2[0]][(kord2[1]+1)%5]
        else:
            szyfrogram += M[kord2[0]][kord1[1]]
            szyfrogram += M[kord1[0]][kord2[1]]

    return szyfrogram




if __name__ == "__main__":

    plaintext = str(input("Podaj hasło do zaszyfrowania (bez cyfr i znaków specjalnych): "))
    klucz = str(input("Podaj klucz do szyfru (bez cyfr i znaków specjalnych): "))
    
    ready_plaintext = cleanup_pt(plaintext)
    print(ready_plaintext)
    ready_klucz = cleanup_k(klucz)

    Macierz = stworz_macierz(ready_klucz)
    cyphertext = enkrypcja(ready_plaintext, Macierz)
    print(cyphertext)








