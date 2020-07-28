"""
Date : 27/07/2020
Devs: CAPELLE Bryan , AMIOT Vincent , DEHOUSSE Erwan
Objectif : regrouper un ensemble de fonction permettant de hasher une chaine de caractere
"""


Alpha = {"a":0,"b":1,"c":2, "d":3,"e": 4, "f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,"A":26,"B":27,"C":28,"D":29,"E":30,"F":31,"G":32,"H":33,"I":34,"J":35,"K":36,"L":37,"M":38,"N":39,"O":40,"Q":41,"R":42,"S":43,"T":44,"U":45,"V":46,"W":47,"X":48,"Y":49,"Z":50,"0":51,"1":52,"2":53,"3":54,"4":55,"5":56,"6":57,"7":58,"8":59,"9":60," ":61}
#Je n'ai pas ajouté les caractères spéciaux
def decalage(àhasher):
    #Renvoie un dictionnaire indiquant le nb de décalage à ajouter par occurence.
    dict = dict()
    List = []
    for i in range (1,àhasher.length()) :
        caract = àhasher.substring(i-1,i)
        if (not caract in List) :
            List.add(caract)
            dict[caract]=1
        else :
            if caract in dict.values() :
                dict[caract]=dict[caract] + 1
    return dict
def id(formule):
    #Renvoie un dictionnaire modifiant les propriétées du dico de base
    Beta = Alpha
    for i in Beta.keys() :
        i = i * formule # A MODIFIER
    return Beta
"""
la formule pour connaitre le décalage est :
dict[caract]
Il faut ensuite faire : dict[caract] = dict[caract] - 1

Ne pas oublier au début du chiffrage de créer le dico avec la phrase non crypté.

Il n'est pas possible de déchiffrer notre algorithme (impossibilité de retrouver le nb d'occurence
des lettres)

L'algorithme de Ceasar est dispo en python sur internet.
"""
stri = "Janvier"
stri = ' '.join(format(ord(x), 'b') for x in stri).split(" ")
print(stri)
def binary_to_hexa(bin):
    hexa_list = []
    hexa_carac = [ "A", "B", "C", "D", "E", "F"]
    somme = 0
    def inner_parse(hexa,somme):
        two_power = [8,4,2,1]
        for i in range(0,4):
            if hexa[i] == "1":
                somme += two_power[i]
        if somme > 9:
            somme -= 10
            return hexa_carac[somme]
        else:
            return somme
    for byte in bin:
        hexa = "0"+byte
        somme = 0
        first = inner_parse(hexa[0:4],somme)
        somme = 0
        second = inner_parse(hexa[4:8],somme)
        hexa_list.append(str(first)+str(second))
    return hexa_list

def hexa_to_binary(hexa):
    hexa_carac = { "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}
    bin = []
    for elt in hexa:
        renvoi = ""
        for j in range (0,2):
            try:
                number = int(elt[j])
                add = "{0:b}".format(number)
                longueur = len(add)
                while longueur!=4:
                    add = "0"+add
                    longueur +=1
                renvoi = renvoi + add
            except:
                renvoi = renvoi+hexa_carac[elt[j]]

        bin.append(renvoi)
    return bin



def jules_cesar() :
    pass

print(binary_to_hexa(stri))
print(hexa_to_binary(binary_to_hexa(stri)))

def jules_cesar(chaine, decalage) :
    stri="" #initialisation de la chaine de caractere
    for i in range(0,len(chaine)):
        lettre = Alpha[chaine[i]] # on recherche la valeur de cette lettre
        lettre+= decalage  # on additionne alors la valeur de la lettre a celle du decalage afin d'obtenir la valeur de la nouvelle lettre
        key_list = [k for (k, val) in Alpha.items() if val == lettre]
        stri += key_list[0]  # on recupere la liste (qui contient un seul element ) et on l'ajoute
    return stri
