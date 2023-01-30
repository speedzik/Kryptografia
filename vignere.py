alphabet = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ'

def cleanup_pt(plaintext):
    plaintext = plaintext.replace(" ","")
    plaintext = plaintext.upper()
    return plaintext

def cleanup_k(klucz):
    klucz = klucz.replace(" ","")
    klucz = klucz.upper()
    return klucz    


def Vigenere(plaintext, klucz):
    plaintext = cleanup_pt(plaintext)
    klucz = cleanup_k(klucz)
    cyphertext = []
    indeks_klucza = 0
    for letters in plaintext:
        num = alphabet.find(letters)
        num += alphabet.find(klucz[indeks_klucza])
        num %= len(alphabet)
        cyphertext.append(alphabet[num])

        indeks_klucza += 1
        if indeks_klucza == len(klucz):
            indeks_klucza = 0
    return "".join(cyphertext)

if __name__ == "__main__":
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ'
    plaintext = str(input("Podaj hasło do zaszyfrowania (bez liter i znaków specjalnych): "))
    klucz = str(input("Podaj klucz do szyfru (bez liter i znaków specjalnych): "))
    cyphertext = Vigenere(plaintext,klucz)
    print(plaintext + " >>>>> " + cyphertext)
