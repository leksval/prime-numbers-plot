
# importuję bibliotekę matplotlib w celu wygenerowania wykresu
import matplotlib.pyplot as plt
from time import time

def primeNumberGeneratorTimer(N):
    # rozpoczynam pomiar czasu
    start = time()
    # dwie pętle for będące algorytmem pozwalającym generować liczby pierwsze
    for x in range (1, N + 1):
           for i in range(2, x):
               if (x % i) == 0:
                   break
           else:
               print(x)
    # koniec pomiaru czasu
    end = time()
    generatingTime = end-start
    return generatingTime

def creatingArraysOfTimeAndNumbers():
    # deklaruję listę z 20 górnymi krańcami przedziału
    listOfNumbers = [5,50,100,300,500,900,1500,2000,4000,6000,8000,10000,12000,15000,20000,30000,40000,50000,60000,70000]
    timeOfGeneratingPrimes = []  
    # pętla generująca listę zawierającą czas wypisania wygenerowanych liczb pierwszych w określonym przedziale
    for number in listOfNumbers:
        timeOfGeneratingPrimes.append(primeNumberGeneratorTimer(number))
    # funkcja zwraca tablicę 2 wygenerowanych tablic potrzebną do utworzenia wykresu
    return [listOfNumbers, timeOfGeneratingPrimes]


def producePlotOfDependency(x, y):
    # za x przyjmujemy timeOfGeneratingPrimes
    # za y przyjmujemy listOfNumbers
    # funkcja generująca wykres punktowy ('ro')
    
    plt.plot(x, y, 'ro')
    plt.grid(True)
    plt.xlabel("amount of prime numbers")
    plt.ylabel("time [s]")
    plt.title("Plot of dependency between time and amount of prime numbers\n")
    # zapisanie wykresu do pliku i niżej wyświetlenie wykresu
    plt.savefig("plot.png", dpi = 1500)

def addingListsToFile(Ns, Ts):
    file = open("listsOfTandN.txt", "w")
    file.write('Tabela wartości N: \n[')
    for i in Ns:       
        file.write(str(i))
        if i == len(Ns):
            break
        file.write(', ')
    file.write(']\n')

    file.write('Tabela wartości t: \n[')
    for t in Ts:       
        file.write(str(round(t, 3)))
        if t == len(Ts):
            break
        file.write(', ') 
    file.write(']\n')
    file.close()


# wywołanie potrzebnej funkcji wraz z parametrami przekazanymi w tablicy 
# w celu wykonania zadania i wygenerowania wykresu 
listOfResults = creatingArraysOfTimeAndNumbers()

addingListsToFile(listOfResults[0], listOfResults[1])
producePlotOfDependency(listOfResults[0], listOfResults[1])

