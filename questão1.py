status_vilao = '' # Variável para avaliar qual é a condição do vilão.
lista_de_viloes = [] # Lista com os nomes dos vilões.

# Loop While para verificar se a condição do vilão for diferente de:
while status_vilao != 'Já temos nossa lista de vilões':
    status_vilao = input()
    # Estrutura da condicional para verificar a condição do vilão:
    if(status_vilao == 'Já temos nossa lista de vilões'):
        # Imprimir os nomes de todos os suspeitos separados por uma virgula e um espaço em branco.
        print('O resultado final ficou assim:')
        print(', '.join(lista_de_viloes))
    else:
        if(status_vilao == 'Novo vilão - Muito Perigoso'):
            nome_vilao = input()
            lista_de_viloes.insert(0, nome_vilao) # Adicionar o vilão no começo da lista.
        elif(status_vilao == 'Novo vilão - Meio perigoso'):
            nome_vilao = input()
            lista_de_viloes.append(nome_vilao) # Adicionar o nome do vilão no final da lista.
        elif(status_vilao == 'O que ele está fazendo aqui?'):
            nome_vilao = input()
            if(nome_vilao in lista_de_viloes): # Condicional para verificar se o nome do vilão estava na lista e remover.
                lista_de_viloes.remove(nome_vilao)
        elif(status_vilao == 'Vilão mais perigoso do que pensávamos'):
            indice_atual_vilao = int(input())
            indice_novo_vilao = int(input())
            # Trocar os lugares do atual vilão pelo novo vilão utilizando o índice:
            lista_de_viloes[indice_atual_vilao], lista_de_viloes[indice_novo_vilao] = lista_de_viloes[indice_novo_vilao], lista_de_viloes[indice_atual_vilao]
        elif(status_vilao == 'Que estranho, esses dois vilões… troque-os de lugar'):
            nome_vilao_1 = input()
            nome_vilao_2 = input()
            # Trocar os lugares do atual vilão pelo novo vilão utilizando os nomes, mas transfomando em índice:
            indice_vilao_1, indice_vilao_2 = lista_de_viloes.index(nome_vilao_1), lista_de_viloes.index(nome_vilao_2)
            lista_de_viloes[indice_vilao_1], lista_de_viloes[indice_vilao_2] = lista_de_viloes[indice_vilao_2], lista_de_viloes[indice_vilao_1]
        elif(status_vilao == 'Essa posição não está de acordo, ele nem odeia carecas'):
            nome_vilao = input()
            if(nome_vilao in lista_de_viloes): # Condicional para verificar se o vilão está na lista, remove-lo e adiciona-lo no final da lista.
                lista_de_viloes.remove(nome_vilao)
                lista_de_viloes.append(nome_vilao)
        elif(status_vilao == 'Como a lista está ficando?'):
            print(', '.join(lista_de_viloes)) # Imprimir os nomes de todos os suspeitos separados por uma virgula e um espaço em branco.