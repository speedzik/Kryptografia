



def enigma(plaintext, Rt1, Rt2, Rt3, Rg1, Rg2, Rg3, Ref1, Ref2):
    cyphertext = ''
    alfabet = 'abcdefghijklmnopqrstuwvxyz'
    plaintext = plaintext.lower()
    ctr1 = 0
    ctr2 = 0

    rotor1 = []
    rotor2 = []
    rotor3 = []

    ring1 = []
    ring2 = []
    ring3 = []

    reflektor1 = []
    reflektor2 = []


    for i in range(len(alfabet)):
        char = alfabet[i]
        rotor1 += chr((ord(char) + Rt1 - 97) % 26 + 97)
        ring3 += chr((ord(char) + Rg3 - 97) % 26 + 97)

    for j in range(len(alfabet)):
        char = rotor1[j]
        rotor2 += chr((ord(char) + Rt2 - 97) % 26 + 97)
        ring2 += chr((ord(char) + Rg2 - 97) % 26 + 97)

    for k in range(len(alfabet)):
        char = rotor2[k]
        rotor3 += chr((ord(char) + Rt3 - 97) % 26 + 97)
        ring1 += chr((ord(char) + Rg1 - 97) % 26 + 97)
    
    for l in range(len(alfabet)):
        char = rotor2[l]
        reflektor1 += chr((ord(char) + Ref1 - 97) % 26 + 97)
        reflektor2 += chr((ord(char) + Ref2 - 97) % 26 + 97)

    # print("Rotor1: " + str(rotor1))
    # print("Rotor2: " + str(rotor2))
    # print("Rotor3: " + str(rotor3))
    # print("Ring1: " + str(ring1))
    # print("Ring2: " + str(ring2))
    # print("Ring3: " + str(ring3))
    # print("Reflektor1: " + str(reflektor1))
    # print("Reflektor2: " + str(reflektor2))



    for m in range(len(plaintext)):
        if plaintext[m] != ' ':
            step0 = rotor1.index(plaintext[m])
            step1 = ring1.index(rotor1[step0])
            step2 = ring2.index(rotor2[step1])
            step3 = ring3.index(rotor3[step2]) 

            reflect1 = reflektor2.index(reflektor1[step3])
            reflect2 = reflektor1.index(reflektor2[reflect1])

            step4 = rotor3.index(ring3[reflect2])
            step5 = rotor2.index(ring2[step4])
            step6 = rotor1.index(ring1[step5])
        
            cyphertext = cyphertext + alfabet[step6]
        else:
            cyphertext = cyphertext + ' '
        if ctr1 < 26:
            rotate(rotor1, ring1, ctr1)
        else:
            ctr1 == 0
            if ctr2 < 26:
                rotate(rotor2, ring2, ctr2)
            else:
                ctr2 == 0
                rotate(rotor3, ring3, None)

    return cyphertext

def rotate(rotor, ring, ctr = None):
    temp1 = rotor[0]
    temp2 = ring[0]
    for i in range(len(rotor)):
        if i == 25:
            rotor[i] = temp1
            ring[i] = temp2
            if ctr != None:
                ctr += 1

        else:
            rotor[i] = rotor[i+1]
            ring[i] = ring[i+1]
        
        
        
        





plaintext = input("Podaj hasło do zakodowania: ")
Rt1 = int(input("Podaj ustawienie pierwszego rotora: "))
Rt2 = int(input("Podaj ustawienie drugiego rotora: "))
Rt3 = int(input("Podaj ustawienie trzeciego rotora: ")) 
Rg1 = int(input("Podaj ustawienie pierwszego pierścienia: "))
Rg2 = int(input("Podaj ustawienie drugiego pierścienia: "))
Rg3 = int(input("Podaj ustawienie trzeciego pierścienia: "))
Ref1 = int(input("Podaj pierwsze ustawienie reflektora: "))
Ref2 = int(input("Podaj drugie ustawienie reflektora: "))

print(enigma(plaintext, Rt1, Rt2, Rt3, Rg1, Rg2, Rg3, Ref1, Ref2))








        



