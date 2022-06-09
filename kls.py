# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,47}
# C = {x: x∈B i x jest liczbą podzielną przez 2}
def zadanie1():
    a = [1-x for x in range(1,10)]
    b = [4 ** i for i in range(8)]
    c = [x for x in b if x % 2 == 0]
    print(a)
    print(b)
    print(c)

# zadanie1()
# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python Comprehension zdefiniuj
# nową listę, która będzie zawierała tylko parzyste elementy
def zadanie2():
    import random
    lista1 = []
    for i in range(10):
        n = random.randint(1, 100)
        lista1.append(n)
    print('lista 1', lista1)
    lista2 = [i for i in lista1 if i % 2 == 0]
    print('lista 2', lista2)

# zadanie2()
# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość
# - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
def zadanie3():
    produkty ={
        'jablka':'kilogramy',
        'awokoado':'sztuki',
        'gruszki':'sztuki',
        'woda':'litry'
    }
    print(produkty)
    # produkty2 = {value: key for key, value in produkty.items()}
    produkty2 = [i for i in produkty.values() if i=='sztuki']
    # produkty2 = [i for i in produkty if i.values() == 'sztuki']
    print(produkty2)

# zadanie3()
# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
def zadanie4():
    def trojkat(a,b,c):
        if a*a + b*b == c*c:
        # if pow(a)+pow(b)==pow(c):
            print('trojkat prostokatny')
        else: print('trojkat nie jest prostokatny')
    print(trojkat(3,4,5))

# zadanie4()
# Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
def zadanie5():
    def trapez(a,b,h):
        pole = (a+b)*(h/2)
        print(pole)
    trapez(10,10,5)

# zadanie5()
# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy),
# ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
def zadanie6():
    def iloczyn(a = 1, b = 4, ile = 10):
        for i in range(ile):
            print(a)
            a=a*b

    iloczyn(2,4,5)
    iloczyn()
# zadanie6()