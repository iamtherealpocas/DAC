import numpy as np
from matplotlib import pyplot as plt
def f(x):
    return 2**x -x**2
print("PARA O PROGRAMA CORRER FECHE A JANELA DO GRÁFICO!")
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
x= np.linspace(-10, 10, 100)

plt.plot(x, f(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True, alpha=0.3)

plt.show() #SE DER ERRO TENS DE INSTALAR A PACKAGE "PyQT6" PARA O PROGRAMA CORRER O GRÁFICO!

print("Há uma função f com um zero.\nDetermina um intervalo que tenha apenas um zero e seleciona o erro que desejas que apresente esse mesmo.")

erro = float(input("\nInsira o valor do erro: "))
xmin = float(input("a: "))
xmax = float(input("b: "))
numiteracoes = 0
amplitude = xmax - xmin
pontomedio = amplitude / 2 + xmin

fmin = f(xmin)
fmax = f(xmax)

#print(fmin, ";", fmax)

while xmax - xmin > erro:
    if fmax >0 and fmin <0: #a
        amplitude = xmax - xmin
        pontomedio= amplitude/2 + xmin
        print("Ponto Médio = ", pontomedio)
        if f(pontomedio) >0:
            xmax = pontomedio
            fmax = f(pontomedio)
            numiteracoes += 1
            print("a")
            print("[", xmin, ",", xmax, "]")

        else: #b
            xmin = pontomedio
            fmin = f(pontomedio)
            numiteracoes += 1
            print("b")
            print("[", xmin, ",", xmax, "]")
    elif fmax <0 and fmin > 0:
        amplitude = xmax - xmin
        pontomedio = amplitude / 2 + xmin
        print("Ponto médio = ", pontomedio)
        if f(pontomedio) <0:
            xmax = pontomedio
            fmax = f(pontomedio)
            numiteracoes += 1
            print("c")
            print("[", xmin, ",", xmax, "]")

        else:
            xmin = pontomedio
            fmin = f(pontomedio)
            numiteracoes += 1
            print("d")
            print("[", xmin, ",", xmax, "]")
    else:
        print("O número mais próximo do zero da função é ", pontomedio) #DA ERRADO SE NAO TIVER ZEROS
        print("Está no intervalo ", "[", xmin, ",", xmax, "]")
        break

print("Número de iterações: ", numiteracoes)
print("Está no intervalo: ", xmin, ";", xmax)