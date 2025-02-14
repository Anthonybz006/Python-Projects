from random import randint

def conferir_num(computer_number, player_number, attempts_qtd, max_attempts):

    while True:
    

        if attempts_qtd > max_attempts -1:
            print("\nVocê Perdeu! Não conseguiu acertar o número com 10 tentativas :(")
            break

        elif player_number == computer_number:
            print(f"\nParabéns! Você conseguiu acertar o número com {attempts_qtd} tentetivas :)")
            attempts_qtd += 1
            break

        elif player_number < computer_number:
            print("O número correto é maior. Tente um valor mais alto!!")
            attempts_qtd += 1
            player_number = int(input(f"\nPalpite {attempts_qtd}: "))

        elif player_number > computer_number:
            print("O número correto é menor. Tente um valor mais baixo!!")
            attempts_qtd += 1
            player_number = int(input(f"\nPalpite {attempts_qtd}: "))


if __name__ == "__main__":

    while True:

        try:

            attempts = 1
            limit = 10

            random_number = randint(0, 100)
            user_number = int(input(f"\nDigite um número de 0 a 100 e tente acertar em 10 tentativas!\nPalpite {attempts}: "))

            conferir_num(random_number, user_number, attempts, limit)
        
        except ValueError:

            print("\nValor digitado inválido. Favor digite um número inteiro entre 0 e 100!!")
            continue