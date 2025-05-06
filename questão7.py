num_amigos = int(input())

# Lista de animes favoritas do monitor césar:
animes_favoritos = [
    'Fullmetal Alchemist: Brotherhood', 
    'Attack On Titan', 
    'Death Note', 
    'Naruto', 
    'One Piece', 
    'Demon Slayer', 
    'Dragon Ball Z', 
    'Jujutsu Kaisen', 
    'Pokemon', 
    'Bleach'
]

pontuacao = [0] * len(animes_favoritos) # Lista da pontuação para quantidade de elementos da lista de animes favoritos.

print(f'{num_amigos} amigos participaram da votação!')

# Loop for para incrementar o input dos amigos que vão participar em função da quantidade de amigos:
for i in range(num_amigos):
    amigo = input()

    print(f'{amigo} é a {i + 1}ª pessoa à votar!')

    lista_animes = [] # Lista vazia para armazenar a lista de animes a cada interação do loop (ou seja, do amigo que vai votar).

    # Loop para verificar se a quantidade de elementos da lista de animes é menor que 3:
    while (len(lista_animes) < 3):
        animes = input().title()

        # Condicional para verificar se o anime está na lista de animes, ou seja, se os inputs (animes) são iguais:
        if(animes in lista_animes):
            print(f'{amigo}, você já votou neste anime! Escolha um outro anime para ocupar a sua {(len(lista_animes) + 1)}º posição!')

            novo_voto = ''

            # Loop para incrementar um novo input:
            while(novo_voto in lista_animes):
                novo_voto = input().title()

                # Condicional para verificar se o novo input não está na lista de animes, ou seja, se os novos inputs (animes) não são iguais:
                if(novo_voto not in lista_animes):
                    print(f'{amigo} colocou {novo_voto} em {(len(lista_animes) + 1)}º lugar do seu ranking!')
                    lista_animes.append(novo_voto)
                else:
                    print(f'{amigo}, você já votou neste anime! Escolha um outro anime para ocupar a sua {(len(lista_animes))}º posição!')

        # Condicional para verificar se o anime não está na lista de animes, ou seja, se os inputs (animes) não são iguais:
        elif(animes not in lista_animes):

            # Condicional para verificar se o anime não está na lista de animes favoritos do césar:
            if(animes not in animes_favoritos):
                print(f'O anime {animes} não está presente na votação!')
                novo_voto = ''
                
                # Loop para incrementar um novo input:
                while(animes not in animes_favoritos):
                    novo_voto = input().title()

                    # Condicional para verificar se o novo input (anime) está na lista de animes favoritos do césar:
                    if(novo_voto in animes_favoritos):
                        lista_animes.append(novo_voto)
                        print(f'{amigo} colocou {novo_voto} em {(len(lista_animes))}º lugar do seu ranking!')
                        animes = novo_voto
                    else:
                        print(f'O anime {novo_voto} não está presente na votação!')
            else:
                    print(f'{amigo} colocou {animes} em {(len(lista_animes) + 1)}º lugar do seu ranking!')
                    lista_animes.append(animes)
    
    # Incrementar a pontuação conforme a ordem dos inputs (animes) e armazena-lo na ordem correta da lista de animes favoritos do césar:
    if(lista_animes[0] in animes_favoritos):
        pontuacao[animes_favoritos.index(lista_animes[0])] += 3
    if(lista_animes[1] in animes_favoritos):
        pontuacao[animes_favoritos.index(lista_animes[1])] += 2
    if(lista_animes[2] in animes_favoritos):
        pontuacao[animes_favoritos.index(lista_animes[2])] += 1

# Obter a maior pontuação na lista de pontuação:
max_pontos = max(pontuacao)

anime_mais_votado = [] # Lista para armazenar o anime mais votado.

# Loop para verificar no todos os índices da lista de pontuação:
for i in range(len(pontuacao)):

    # Condicional para verificar qual é a pontuação, atráves do índice i, que seja igual a pontuação máxima:
    if(pontuacao[i] == max_pontos):
        anime_mais_votado.append(animes_favoritos[i]) # Obter o nome do anime correspondente ao índice i na lista de animes favoritos do césar e o adicionamos à lista do mais votado.

print(f'Com {max_pontos} pontos, {anime_mais_votado[0]} foi votado como o melhor anime!')

# Verificar se pokemon é o anime mais votado:
if('Pokemon' in anime_mais_votado):
    print('César - Pokémon é o melhor anime da história!!!')

print('Eita mandaram dúvida no discord, vou lá responder!')