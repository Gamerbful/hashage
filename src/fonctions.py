"""
Date : 27/07/2020
Devs: CAPELLE Bryan , AMIOT Vincent , DEHOUSSE Erwan
Objectif : regrouper un ensemble de fonction permettant de hasher une chaine de caractere
"""

str = bytes("Hello", "utf-8")

def binary_to_hexa(bin):
    print(len(bin))
    for byte in bin:
        print(byte)

binary_to_hexa(str)
