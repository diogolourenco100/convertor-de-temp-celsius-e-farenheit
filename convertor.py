#import os

#os.system("cls")

f = input("Digite a temperatura em Farenheit: ")

#os.system("cls")

def convercao(f):
    return int(5 * ((int(f) - 32) / 9))

result = convercao(f)
print(f"A temperatura {f}°F é equivalente à {result}°C.")
print("")
input("Pressione alguma tecla para continuar...")
#os.system("cls")
