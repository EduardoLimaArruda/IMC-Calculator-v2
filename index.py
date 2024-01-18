print("Calculadora de IMC\n")

altura = input("Qual a sua altura?\n")
peso = input("Qual o seu peso?\n")
altura_int = float(altura)
peso_int = int(peso)

IMC = peso_int / (altura_int ** 2)
print("Seu IMC é:" + str(round(IMC,1)))

if IMC <= 18.5:
    print("Você está abaixo do peso!")
elif IMC <= 25:
    print("Seu peso está normal!")
elif IMC <= 30:
    print("Você está sobrepeso!")
elif IMC <= 35:
    print("Você está obeso!")  
elif IMC <= 40:
    print("Você está com obesidade severa!")
else:
    print("Você está com obesidade mórbida!")

enter = input("\nAperte Enter para fechar")