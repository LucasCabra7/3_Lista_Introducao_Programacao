nomes = input() # Input para os nomes.
nome_dupla = ''
lista_nomes = nomes.split('-') # Altera a string da variável nomes e forma em uma lista.
lista_modificada = lista_nomes[:] # Copiando os elementos da lista_nome em lista_modificada sem alterar os elementos da lista_nome.
teleporte = [] # Lista para quantidade de teleportes.

for i in range(len(lista_nomes)): # Loop para quantidade de elementos da lista nomes.
    teleporte.append(int(0)) # Adiciona a quantidade de teleportes para a quantidade de elementos da lista nomes.

while nome_dupla != 'Acabou!':
    nome_dupla = input()
    lista_p_dupla = nome_dupla.split('-')
    if(nome_dupla == 'Acabou!'):
        print('Fila do almoço:')
        for nome in lista_modificada: # Loop para nome na lista modificada de nomes.
            if(teleporte[lista_nomes.index(nome)] == 1):  # Condicional para verificar se o indice do nome da lista nomes que é igual no teleporte é igual a 1.
                print(f'{nome}: {teleporte[lista_nomes.index(nome)]} teleporte!')
            else:
                print(f'{nome}: {teleporte[lista_nomes.index(nome)]} teleportes!')
    else:
        if((lista_p_dupla[0] in lista_nomes) and (lista_p_dupla[1] in lista_nomes)):  # Condicional para verificar se o nome está na lista nomes e alterar os lugares.
            indice_1, indice_2 = lista_modificada.index(lista_p_dupla[0]), lista_modificada.index(lista_p_dupla[1])
            lista_modificada[indice_1], lista_modificada[indice_2] = lista_modificada[indice_2], lista_modificada[indice_1]
            # Armazenar o teleporte conforme o indice do nome na lista p dupla.
            teleporte_1 = lista_nomes.index(lista_p_dupla[0]) 
            teleporte_2 = lista_nomes.index(lista_p_dupla[1])
            # Incrementa a quantidade de teleporte.
            teleporte[teleporte_1] += 1
            teleporte[teleporte_2] += 1
        else:
            print('Essa dupla não esta na lista!')