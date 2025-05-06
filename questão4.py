tipo_item = ''
# Lista para tipo do item com o nível:
arma_especial, arma_nivel_1, arma_nivel_2, arma_nivel_3, arma_nivel_4 = [], [], [], [], []
objeto_especial, objeto_nivel_1, objeto_nivel_2, objeto_nivel_3, objeto_nivel_4 = [], [], [], [], []

# Lista para objeto e arma:
objeto = [objeto_especial, objeto_nivel_1, objeto_nivel_2, objeto_nivel_3, objeto_nivel_4]
arma = [arma_especial, arma_nivel_1, arma_nivel_2, arma_nivel_3, arma_nivel_4]

# Lista com os níveis em string:
str_categorias = ['Categoria Especial', 'Nível 1', 'Nível 2', 'Nível 3', 'Nível 4']

# Loop para validar se o tipo do item é diferente de Catalogação encerrada:
while tipo_item != 'Catalogação encerrada!':
    tipo_item = input()
    if(tipo_item == 'Catalogação encerrada!'): # Condicional para finalizar o loop.
        print('Processando lista de itens…')
        print('')
        print('ITENS AMALDIÇOADOS DA TOKYO JUJUTSU HIGH')
        print('')
        print('Objetos')
        for i in range(len(objeto)): # Loop para percorrer todas as 5 categorias da lista objeto pelo indice i.
            qtd = len(objeto[i]) # Contar quantos itens estão nessa sublista dessa categoria utilizando o indice i.
            nomes_objetos = ', '.join(objeto[i]) # Transformar a lista de de itens em uma única string utilizando o indice i.
            if(qtd > 0): # Condicional para verificar qual dessas sublistas dessa categoria possui quantidade maior que 0.
                print(f'{str_categorias[i]}: {nomes_objetos}')
        print('')
        print('Armas')
        for i in range(len(arma)): # De maneira analoga para arma.
            qtd = len(arma[i])
            nomes_objetos = ', '.join(arma[i])
            if(qtd > 0):
                print(f'{str_categorias[i]}: {nomes_objetos}')
    else: # Condicional para verificar o nome do item, se é arma ou obejeto e seu nível para adiciona-lo a lista correspondente.
        nome_item = input()
        nome_item_separado = nome_item.split(' - ')
        if(tipo_item == 'objeto'):
            if(int(nome_item_separado[-1]) == 0):
                objeto_especial.append(nome_item_separado[0])
            elif(int(nome_item_separado[-1]) == 1):
                objeto_nivel_1.append(nome_item_separado[0])
            elif(int(nome_item_separado[-1]) == 2):
                objeto_nivel_2.append(nome_item_separado[0])
            elif(int(nome_item_separado[-1]) == 3):
                objeto_nivel_3.append(nome_item_separado[0])
            elif(int(nome_item_separado[-1]) == 4):
                objeto_nivel_4.append(nome_item_separado[0])
            print(f'O objeto {nome_item_separado[0]} foi catalogado com sucesso!')
        else:
            if (int(nome_item_separado[-1]) == 0):
                arma_especial.append(nome_item_separado[0])
            elif (int(nome_item_separado[-1]) == 1):
                arma_nivel_1.append(nome_item_separado[0])
            elif (int(nome_item_separado[-1]) == 2):
                arma_nivel_2.append(nome_item_separado[0])
            elif (int(nome_item_separado[-1]) == 3):
                arma_nivel_3.append(nome_item_separado[0])
            elif (int(nome_item_separado[-1]) == 4):
                arma_nivel_4.append(nome_item_separado[0])
            print(f'A arma {nome_item_separado[0]} foi catalogada com sucesso!')