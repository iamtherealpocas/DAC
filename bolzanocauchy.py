#import mathlib #SE QUISERES TRABALHAR NISTO VAI PARA A BRANCH MATHLIB
#IGNORA ISTO PARA JÁ print("Há uma função f que interseta um certo valor d.\nDefina esse valor e o programa irá encontrar o intervalo mais próximo desse valor definido com a função:")
def f(x):
    return 2**x -x**2
print("f(x) = 2**x - x**2")
#d = int(input("d: ")) #IGNORA ISTO PARA JÁ
erro = float(input("\nInsira o valor do erro: "))
xmin = float(input("a: "))
xmax = float(input("b: "))
numiteracoes = 0
amplitude = xmax - xmin
pontomedio = amplitude / 2 + xmin

fmin = f(xmin)
fmax = f(xmax)


while xmax - xmin > erro:
    if fmax >0 and fmin <0: #a
        amplitude = xmax - xmin
        pontomedio= amplitude/2 + xmin
        print("Ponto Médio = ", pontomedio)
        if f(pontomedio) >0:
            xmax = pontomedio
            fmax = f(pontomedio)
            numiteracoes += 1
            #print("a")
            print("[", xmin, ",", xmax, "]")

        else: #b
            xmin = pontomedio
            fmin = f(pontomedio)
            numiteracoes += 1
            #print("b")
            print("[", xmin, ",", xmax, "]")
    elif fmax <0 and fmin > 0:
        amplitude = xmax - xmin
        pontomedio = amplitude / 2 + xmin
        print("Ponto médio = ", pontomedio)
        if f(pontomedio) <0:
            xmax = pontomedio
            fmax = f(pontomedio)
            numiteracoes += 1
            #print("c")
            print("[", xmin, ",", xmax, "]")

        else:
            xmin = pontomedio
            fmin = f(pontomedio)
            numiteracoes += 1
            #print("d")
            print("[", xmin, ",", xmax, "]")
    else:
        print("Não há zeros ou tem mais do que 1 zero!")
        break

print("\n\nNúmero de iterações: ", numiteracoes)
if numiteracoes != 0:
    print("Está no intervalo: ", "[", xmin, ";", xmax, "]")