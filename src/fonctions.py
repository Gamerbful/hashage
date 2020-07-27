"""
Date : 27/07/2020
Devs: CAPELLE Bryan , AMIOT Vincent , DEHOUSSE Erwan
Objectif : regrouper un ensemble de fonction permettant de hasher une chaine de caractere
"""
Alpha = {"a":0,"b":1,"c":2, "d":3,"e": 4, "f":5,"g" : 6,"h":7}
def decalage(hash):
    dict = {"a":1}
    for i in hash:
        pass
    return dict

str = "Hello"
str = ' '.join(format(ord(x), 'b') for x in str).split(" ")
def binary_to_hexa(bin):
    print(len(bin))
    for byte in bin:
        print(byte)

binary_to_hexa(str)
