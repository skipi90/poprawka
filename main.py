import sys
import math
import cmath

#zadanie 1
lista1 = [1,2,3,4,20,6,7,8,9,11]
lista2=[]
def funkcja(lista=[]):
    dlg = len(lista)
    suma = int(lista[0])+int(lista[dlg-1])
    print(suma)
    for x in lista:
        if x > suma:
            lista2.append(x)

funkcja(lista1)
print(lista2)

# zadanie 2
# lista=[]
# for x in range(1,11):
#     lista.append(x)
#
# print(lista)
#
# lista1=[math.sqrt(x) for x in lista]
#
# zadanie 3
# a = math.pow((14/26),(1/3))
# b = math.pow((4/9), 4)
# c = math.sin(67)
# d = math.log1p(c)
# print(round(a+b+d,2))
#
# zadanie 4
# znaki = []
# plik = open("tekst.txt","r",encoding='utf-8')
# lista = plik.read()
# plik.close()
# licznik1=1
# licznik_e=0
# for x in lista:
#     if licznik1<37:
#         licznik1 = licznik1 + 1
#     else:
#         if licznik1<37+26+1:
#             znaki.append(lista[licznik1+1])
#             licznik1 = licznik1 + 1
# for x in znaki:
#     if x=='ę':
#         licznik_e=licznik_e+1
# print("liczba wystąpięń ę:{}".format(licznik_e))
#
# zadanie 5
#
# try:
#     n = input("Podaj liczbe calkowita ")
#     n = int(n)
#     iloczyn = 1
#     if n > 0:
#         for x in range(1,n+1):
#            iloczyn = iloczyn * x
#     else:
#         print("Nie podales liczby dodatniej")
#     plik = open("zadanie5.txt","w")
#     plik.write(str(iloczyn))
# except ValueError:
#     print("nie podales liczby calkowitej")