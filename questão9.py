qtd_ash_gary = input().split() # Quantidade de pokemons na mochila de Ash e Gary respectivamente.

qtd_ash = int(qtd_ash_gary[0]) # Separa o valor escolhido em inteiro para Ash
qtd_gary = int(qtd_ash_gary[1]) # Separa o valor escolhido em inteiro para Gary

historico_batalhas = [] # Lista para o historico de cada batalha.

pokemons_ash = [] # Lista de pokemons do Ash.
for ash in range(qtd_ash): # Loop para incrementar a quantidade de Pokemons de Ash e quais serão.
    pokemons = input().split(', ')
    nome = pokemons[0]
    tipo = pokemons[1]
    hp_inicial = int(pokemons[2])
    level = int(pokemons[3])
    pokemons_ash.append([nome, tipo, hp_inicial, level])

pokemons_gary = [] # Lista de pokemons do Gary.
for gary in range(qtd_gary): # Loop para incrementar a quantidade de Pokemons de Gary e quais serão.
    pokemons = input().split(', ')
    nome = pokemons[0]
    tipo = pokemons[1]
    hp_inicial = int(pokemons[2])
    level = int(pokemons[3])
    pokemons_gary.append([nome, tipo, hp_inicial, level])

print('QUE COMECEM AS BATALHAS')

if((qtd_ash == 0) and (qtd_gary == 0)): # Condicional para verificar se a quantidade de pokemons de Ash e Gary são iguais a 0.
    print('=============== ===============')
    print('Nenhuma batalha foi concluída.')
    decisao_ash = 'FIM DAS BATALHAS'
elif((qtd_ash == 0) and (qtd_gary > 0)): # Condicional para verificar se a quantidade de pokemons apenas do Ash é 0.
    print('=============== ===============')
    print('Ash deixou seus pokemons descansando!')
    print('Gary é o grande vencedor!')
    decisao_ash = 'FIM DAS BATALHAS'
elif((qtd_ash > 0) and (qtd_gary == 0)): # Condicional para verificar se a quantidade de pokemons apenas do Gary é 0.
    print('=============== ===============')
    print('Gary deixou seus pokemons descansando!')
    print('Ash é o grande vencedor!')
    decisao_ash = 'FIM DAS BATALHAS'
else: # Caso nenhuma das condições acima é satisfeita, entraremos no Loop While para possíveis batalhas.
    decisao_ash = ''

while decisao_ash != 'FIM DAS BATALHAS': # Loop While para verificar se a decisão do Ash for o FIN DAS BATLHAS.

    decisao_ash = input()

    if(decisao_ash == 'FIM DAS BATALHAS'): # Condicional caso a decisão do Ash seja o FIM DAS BATALHAS e finalizar o Loop:
        print('=============== ===============')
        for i in historico_batalhas:
            print(i)
        if(len(pokemons_ash) > len(pokemons_gary)):
            print('Ash é o grande vencedor!')
        elif(len(pokemons_ash) < len(pokemons_gary)):
            print('Gary é o grande vencedor!')
        elif(len(pokemons_ash) == len(pokemons_gary)):
            print('Depois de todas as batalhas, ainda terminou em empate!')

    else: # Caso contrário:
        numero_ash_gary = input().split() # Número de Ash e Gary para rodada de par ou ímpar.

        num_ash = int(numero_ash_gary[0]) # Separa o valor escolhido em inteiro para Ash.
        num_gary = int(numero_ash_gary[1]) # Separa o valor escolhido em inteiro para Gary.

        soma = (num_ash + num_gary) # Soma para saber o resultado de par ou ímpar.

        # Condição para o primeiro ataque iniciar pelo Pokemon do Ahs:
        primeiro_atq_ash = ((soma % 2 == 0) and (decisao_ash == 'par')) or ((soma % 2 == 1) and (decisao_ash == 'ímpar')) 

        nome_pokemon_ash = input().split()[0] # Escolha do pokemon de Ash (em lista)
        nome_pokemon_gary = input().split()[0] # Escolha do pokemon de Gary (em lista)

        for i in pokemons_ash: # Pecorrer todos os elementos da lista de pokemons do Ash.
            if(nome_pokemon_ash == i[0]): # Encontrar a escolha atual de Ash na lista de pokemons.
                nome_pokemon_ash = i # Alterar para a escolha atual do Ash com as informações do Pokemon juntas (pois é uma lista)
        
        for j in pokemons_gary: # Pecorrer todos os elementos da lista de pokemons do Gary.
            if(nome_pokemon_gary == j[0]): # Encontrar a escolha atual de Gary na lista de pokemons.
                nome_pokemon_gary = j # Alterar para a escolha atual do Gary com as informações do Pokemon juntas (pois é uma lista)

        # Loop para verificar se o HP das escolhas atuais de Ash e Gary são maiores que zero (i.e, não desmaiaram):
        while(nome_pokemon_ash[2] > 0 and nome_pokemon_gary[2] > 0):

            if(primeiro_atq_ash == True): # Condicional para verificar se a condição do primeiro ataque inicia com o pokemon do Ash:
                atacante, defensor = nome_pokemon_ash, nome_pokemon_gary
            else: # Caso contrário, será iniciado pelo pokemon do Gary:
                atacante, defensor = nome_pokemon_gary, nome_pokemon_ash

            # Verificando se o HP do Atacante é maior que zero para atacar o defensor:
            if(atacante[2] > 0):
                ataque = (atacante[3] * 2) # O ataque é calculado como o nível do atacante multiplicado por 2
                defensor[2] -= ataque # O HP do defensor é reduzido pelo valor do ataque

            # Verificando se o HP do defensor é maior que zero para contra-atacar:
            if(defensor[2] > 0):
                ataque = (defensor[3] * 2) # O defensor agora contra-ataca com seu nível multiplicado por 2
                atacante[2] -= ataque # O HP do atacante é reduzido pelo valor do contra-ataque
            else: # Caso o HP do defensor seja igual a zero (ele desmaia):
                print(f'{defensor[0]} desmaiou e {atacante[0]} venceu esta luta')

            # Caso o HP do Atacante seja igual a zero (ele desmaia):
            if(atacante[2] <= 0):
                print(f'{atacante[0]} desmaiou e {defensor[0]} venceu esta luta')
        
        # Incrementar o Round da batalha:
        batalha = len(historico_batalhas) + 1
        if(nome_pokemon_ash[2] > 0): # Se o pokemon de Ash for o campeão da batalha:
            vencedor, perdedor = nome_pokemon_ash[0].upper(), nome_pokemon_gary[0].lower() # Adicionar o nome do pokemon vencedor e perdedor.
            historico_batalhas.append(f'{batalha}° Batalha: {vencedor} vs {perdedor}') # Adicionar a F-string na lista do historico da batalha.
        else:
            vencedor, perdedor = nome_pokemon_gary[0].upper(), nome_pokemon_ash[0].lower()
            historico_batalhas.append(f'{batalha}° Batalha: {perdedor} vs {vencedor}') # Adicionar o nome do pokemon vencedor e perdedor.

    # Verificar os pokemons vivos para continuar na mochila (ou seja, não desmaiaram):
        pokemons_ash_vivos = []
        # Para os pokemons de Ash:
        for p in pokemons_ash:
            if (p[2] > 0):
                pokemons_ash_vivos.append(p)
        pokemons_ash = pokemons_ash_vivos

        # Para os pokemons de Gary:
        pokemons_gary_vivos = []
        for p in pokemons_gary:
            if (p[2] > 0):
                pokemons_gary_vivos.append(p)
        pokemons_gary = pokemons_gary_vivos