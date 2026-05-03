import numpy as np
from matplotlib import pyplot as plt
def f(x):
    return 2**x -x**2
print("PARA O PROGRAMA CORRER FECHE A JANELA DO GRÁFICO!")
xaxis=0
yaxis=0
plt.rcParams["figure.figsize"] = [7.50, 3.50] #???
plt.rcParams["figure.autolayout"] = True #FORMATAÇÃO DA JANELA
x= np.linspace(-5, 5.5, 100) #NÃO TENHO A CERTEZA DO QUE ISTO FAZ? NÃO MEXER NO NÚMERO 100!!!
xminfun=-2
xmaxfun=5
yminfun=-5
ymaxfun=5

plt.plot(x, f(x))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)
ax = plt.gca()
ax.set_xlim([xminfun, xmaxfun])
ax.set_ylim([yminfun, ymaxfun])
plt.axhline(0, color='black', linewidth=.5)
plt.axvline(0, color='black', linewidth=.5)

plt.show() #SE DER ERRO TENS DE INSTALAR A PACKAGE "PyQT6" PARA O PROGRAMA CORRER O GRÁFICO!

print("Defina uma constante d e um intervalo [a,b] da função dada, em que estes se intersetem.\nO programa irá bissetar esse intervalo até obter um erro inferior entre a constante e o intervalo da função que escreveu\n")
print("f(x) = 2**x - x**2")
d = int(input("d: "))
erro = float(input("\nInsira o valor do erro: "))
xmin = float(input("a: "))
xmax = float(input("b: "))
numiteracoes = 0
amplitude = xmax - xmin
pontomedio = amplitude / 2 + xmin

fmin = f(xmin)
fmax = f(xmax)


while xmax - xmin > erro:
    if fmax >d and fmin <d:
        amplitude = xmax - xmin
        pontomedio= amplitude/2 + xmin
        print("Ponto Médio = ", pontomedio)
        if f(pontomedio) >d:
            xmax = pontomedio
            fmax = f(pontomedio)
            numiteracoes += 1
            print("[", xmin, ",", xmax, "]")

        else:
            xmin = pontomedio
            fmin = f(pontomedio)
            numiteracoes += 1
            print("[", xmin, ",", xmax, "]")
    elif fmax <d and fmin > d:
        amplitude = xmax - xmin
        pontomedio = amplitude / 2 + xmin
        print("Ponto médio = ", pontomedio)
        if f(pontomedio) <d:
            xmax = pontomedio
            fmax = f(pontomedio)
            numiteracoes += 1
            print("[", xmin, ",", xmax, "]")

        else:
            xmin = pontomedio
            fmin = f(pontomedio)
            numiteracoes += 1
            print("[", xmin, ",", xmax, "]")
    else:
        print("A constante d não interseta com a função OU interseta mais do que uma vez")
        break

print("\n\nNúmero de iterações: ", numiteracoes)
if numiteracoes != 0:
    print("Está no intervalo: ", "[", xmin, ";", xmax, "]")