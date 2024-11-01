print("\033[1:34m Nesse programa, você calculará ou o seu ou de outrem em particular, \033[1:33mo IMC (Índice de Massa Corporea)\033[1:34m \nsendo como preciso digitar o \033[1:33mpeso \033[1:34mdo paciênte, e tambêm a sua \033[1:33maltura\033[1:34m, para que se realize o cálculo \nnecessário, entregando-lhe o resultado:\033[0:39m")

nome = str(input(" Nome: "))
altura = float(input(" Altura: "))
peso = float(input(" Peso: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(" {} têm um Índice de Massa Corpórea de {:.2f}, constando-o na faixa de \033[1:37m'abaixo do peso ideal'\033[1:39m - em um \033[1:33mIMC \033[1:39m\nabaixo de: \033[1:37m18.5\033[1:39m.".format(nome, imc))
elif imc > 18.5 and imc <= 25:
    print(" {} têm um Índice de Massa Corporea de {:.2f}, constando na faixa de \033[1:33mPeso Ideal\033[1:39m - em um \033[1:33mIMC\033[1:39m entre: \n\033[1:33m18.5 à 25.\033[1:39m".format(nome, imc, altura, peso))
elif imc > 25 and imc <= 30 :
    print(" {} têm um Índice de Massa Corporea de {:.2f}, constando na faixa de \033[1:34mSobrepeso\033[1:39m - em um \033[1:33mIMC\033[1:39m entre: \n\033[1:34m25 à 30\033[1:39m.".format(nome, imc))
elif imc > 30 and imc <= 40:
    print(" {} têm um Índice de Massa Corporea de {:.2f}, constando na faixa de Obesidade - em um IMC entre: \n30 à 40.".format(nome, imc))
elif imc > 40:
    print(" {} têm um índice de Massa Corporea de {:.2f}, constando na faixa de Obesidade Mórbida - em um IMC acima \nde: 40.".format(nome, imc))
print(f" {nome} têm um \033[1:33mpeso \033[1:39mde \033[1:33m{peso}kg\033[1:39m, com uma \033[1:32maltura \033[1:39mde \033[1:32m{altura}cm.\033[1:39m")
print(" FIM.")


