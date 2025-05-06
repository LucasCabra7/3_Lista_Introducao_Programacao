limite_animes = int(input()) # Limite de animes.
qtd_animes = int(input()) # Quantidade de indicações de animes.

lista_animes_add = [] # Lista para quantidade de animes adicionados.

# Loop para percorrer todas as quantidade de indicações de animes por i.
for i in range(qtd_animes):
    info_anime = input()
    info_anime_split = info_anime.split(' - ')
    if(i >= limite_animes): # Condicional para validar se a quantidade de indicações de animes é maior do que ou igual ao limite de animes.
        print(f'A lista de animes está cheia. O {info_anime_split[0]} não foi adicionado.')
    else:
        if(info_anime_split[-1] == 'Walter'): # Condicional para validar se a pessoa que indicou é o Walter.
            lista_animes_add.append(info_anime_split[0]) # Adicionar o nome na lista de animes.
            print(f'O {info_anime_split[0]} foi adicionado à lista de animes para assistir.')
        elif(info_anime_split[-1] == 'Internet'): # Condicional para validar se quem indicou é a Internet.
            if(int(info_anime_split[1]) > 16): # E verificar se a quantidade de temporadas é maior que 16.
                print(f'O {info_anime_split[0]} é muito longo, fica para próxima.')
            else:
                lista_animes_add.append(info_anime_split[0])
                print(f'O {info_anime_split[0]} foi adicionado à lista de animes para assistir.')
print(f'Lista final para assistir:{lista_animes_add}')