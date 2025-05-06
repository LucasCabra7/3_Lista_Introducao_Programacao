num_feiticeiros = int(input()) # Quantidade de feiticeiros.

# Lista para os nomes e níveis dos respectivos feiticeiros:
lista_nomes = []
lista_niveis = []

# Loop para incrementar os inputs pedidos para nomes e níveis de acordo com a quantidade de feiticeiros:
for i in range(num_feiticeiros):
    nome_do_feiticeiro = input()
    nivel_de_magia = int(input())

    lista_nomes.append(nome_do_feiticeiro)
    lista_niveis.append(nivel_de_magia)

k = 1 # Inicio da minha rodada.

# Loop para verificar se a quantidade de elementos da lista de nomes é diferente de 1:
while (len(lista_nomes) != 1):
    print(f'\n--- Rodada {k} ---')

# Nova lista vazia para os vencedores e os níveis de cada vencedor, respectivamente:
    vencendores = []
    nivel_vencedores = []

    # Loop for para incrementar as rodadas em PARES de feiticeiros, pela quantidade de nomes na lista de nomes.
    for j in range(0, len(lista_nomes) - 1, 2):
        print(f'Confronto: {lista_nomes[j]} vs {lista_nomes[j + 1]}')
        
        # Condicional para verificar o maior nível do feiticeiro atráves do indíce j, determinar o vencedor, e armazenar seu nome e nível:
        if(lista_niveis[j] > lista_niveis[j + 1]):
            vencedor = lista_nomes[j]
            nivel_vencedor = lista_niveis[j]
        elif(lista_niveis[j] < lista_niveis[j + 1]):
            vencedor = lista_nomes[j + 1]
            nivel_vencedor = lista_niveis[j + 1]
        else:
            vencedor = lista_nomes[j]
            nivel_vencedor = lista_niveis[j]
        
        # Imprimir o vencedor e adicionar o nome e nível na lista de vencedores:
        print(f'{vencedor} vence!')
        vencendores.append(vencedor)
        nivel_vencedores.append(nivel_vencedor)

    # Condicional para verificar, após o loop For, se a quantidade a lista de nomes é ímpar.
    if (len(lista_nomes) % 2 != 0):
        ultimo_feiticeiro = lista_nomes[-1] # Armazenar o nome do último feiticeiro. 
        nivel_ultimo = lista_niveis[-1]
        print(f'{ultimo_feiticeiro} avança automaticamente!')
        vencendores.append(ultimo_feiticeiro) # Adicionar o último feiticeiro da lista, na lista de vencedores.
        nivel_vencedores.append(nivel_ultimo)

    # Atualizar listas para a próxima rodada:
    lista_nomes = vencendores
    lista_niveis = nivel_vencedores

    k += 1  # Incremento da rodada

print(f'\nO campeão do torneio é {lista_nomes[0]} com nível de energia amaldiçoada {lista_niveis[0]}!')

# Verificar, se depois de todas as rodadas, o último jogador (vencedor) é o Itadori:
if(lista_nomes[0] == 'Itadori'):
    if(lista_niveis[0] > 90):
        print('\n### Nas sombras da alma de Itadori, Sukuna desperta e toma o controle! ###')
        print('Uma aura de destruição toma conta, não há escapatória.')
        print('Com um riso diabólico, ele manifesta sua Expansão de Domínio: Fukuma Mizushi!')
    else:
        print('\nItadori vence com honra e bravura!')