import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavras = ["PYTHON", "PROGRAMACAO", "DESENVOLVIMENTO"]
    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        # --- INÍCIO DO TRATAMENTO DE ERROS ---
        try:
            chute = input("Qual letra? ").strip().upper()

            if not chute.isalpha():
                raise ValueError("Por favor, digite apenas letras.")
            if len(chute) != 1:
                raise ValueError("Digite apenas uma letra por vez.")
        except ValueError as e:
            print(f"Entrada Inválida: {e}")
            continue 
        # --- FIM DO TRATAMENTO DE ERROS ---

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {6 - erros} tentativas.")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(" ".join(letras_acertadas))

    if(acertou):
        print("Você ganhou!")
    else:
        print(f"Você perdeu! A palavra era {palavra_secreta}")

if(__name__ == "__main__"):
    jogar()
