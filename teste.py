import math
# definindo variáveis
G = 9.8 # m/s**2
angulo = 30 # graus
v0 = 20 # m/s
h = 45 # m 

# decomponto a velocidade no eixo x e y
v0x = v0 * math.cos(v0)
v0y = v0 * math.sin(v0)

# acelerações
ax = 0
ay = -G



# posição x começando em 0
x = 0
# posição y começa sendo a altura inicial h
y = h

# vai se manter assim
vx = v0x

# vai variar
vy = v0y

# tempo começa com 0
t = 0
# i seria o tempo
while y <= 0:
    # tempo vai aumentando de 0.1 s
    t += 0.1
    print("tempo = {}".format(t))
    # posição no eixo x
    # como vx é constante, a posição em x vai ser sempre v * t
    x += vx * t
    print("posição no eixo x: {:.2f}".format(x))

    # variação da posicao em y -> vy =  vy + a * t
    vy += ay * t
    print("velocidade no  eixo y = {:.2f}".format(vy))

    # posição no eixo y
    y += vy * t




