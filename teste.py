n = int(input("Digite o valor de N: "))

s = 0

for i in range(1, n+1):
    s += i / (n+1 - i)
    print("a soma de {:.2f} / {:.2f} é = {:.2f}. Soma acumulada = {:.2f}".format(i,(n+1 - i), i / (n+1 - i), s))