# Program który policzy za którym razem komputerowi udało się wygrać w LOTTO
# Będziemy losować 6 różnych liczb, tak długo aż będą to liczby z poprzedniego losowania LOTTO
import random
#wynik = [10, 15, 18, 26, 32, 40]
wynik = [10, 15, 18, 26, 32, 40]
t = []
licznik = 0
while t != wynik:
    licznik += 1
    t = []
    for i in range(6):
        x = random.randint(1, 49)
        while t.__contains__(x):
            x = random.randint(1, 49)
        else:
            t.append(x)
    t.sort()
    print(t)
print(f"Udało się wylosować wygrane liczby, za {licznik} razem")