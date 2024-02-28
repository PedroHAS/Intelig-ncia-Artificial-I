import random

def jogar_pedra_papel_tesoura(escolha_jogador):
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = random.choice(opcoes)

    print(f"Escolha do jogador: {escolha_jogador}")
    print(f"Escolha do computador: {escolha_computador}")

    if escolha_jogador == escolha_computador:
        return "Empate!"
    elif (
        (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
        (escolha_jogador == "papel" and escolha_computador == "pedra") or
        (escolha_jogador == "tesoura" and escolha_computador == "papel")
    ):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

def obter_escolha_jogador():
    while True:
        escolha = input("Escolha: pedra, papel ou tesoura? ").lower()
        if escolha in ["pedra", "papel", "tesoura"]:
            return escolha
        else:
            print("Escolha inválida. Tente novamente.")

def jogo_principal():
    print("Bem-vindo ao Jogo Pedra, Papel, Tesoura!")

    while True:
        escolha_jogador = obter_escolha_jogador()
        resultado = jogar_pedra_papel_tesoura(escolha_jogador)

        print(resultado)

        jogar_novamente = input("Quer jogar novamente? (sim/não): ").lower()
        if jogar_novamente != "sim":
            print("Obrigado por jogar! Até mais.")
            break

jogo_principal()
