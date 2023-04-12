#jogo da forca em Python3
#Desenvolvedor: Miguel.M
#Verção: 1.0

#Menu de Boas Vindas
print("***************************************")
print("*******Bem Vindo ao Jogo da Forca!*****")
print("***************************************")

palavra_secreta = "Teletransporte".upper()
letras_acertadas = ["_" for letra in palavra_secreta]

print(letras_acertadas)

#variaveis de validação e verifição do jogo
enforcou = False
acertou = False
erros = 0
#controle de fim de jogo "enquanto"
while(not enforcou and not acertou):
    chute = input("Qual a letra?")
    chute = chute.strip().upper()

    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
            index += 1
    else:
        erros += 1
    if erros == 6:
        enforcou = True
    if "_" not in letras_acertadas:
        acertou = True
    print(letras_acertadas)
    print('chutes errados',erros)
if acertou:
    print("Você ganhou!!")
else:
    print("Você Perdeu!!")
    print("Fim do Jogo")

input()