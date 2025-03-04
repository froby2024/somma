# programma che calcola la somma dei numeri interi a partire da 1 fino ad un valore massimo n
# con la condizione che tale somma non superi il valore 1000.
# 1 + 2 + 3 + 4 + ... + n <1000 e 1 + 2 + 3 + 4 + ... + (n+1) >= 1000

print("Sommatoria s dei numeri naturali fino a n, con s<1000")

# primo numero naturale
n = 0
# variabile per la sommatoria
s = 0

# continua a sommare i numeri naturali consecutivi mentre s è minore di 1000
while s<1000:
    n += 1
    s += n
    print("n =", n, "\ts =", s)

# quando esce dal ciclo while il valore 1000 è stato raggiunto o superato
# quindi sottraggo da s l'ultimo n sommato e diminuisco n di 1
s -= n
n -= 1

print("Il risultato richiesto è:")
print("n =", n)
print("s =", s)