# Entrada para quantidade de monitores:
qnt_monitores = int(input())
# Lista para cada determinada categoria:
aprimoradores, emissores, transmutadores, manipuladores, conjuradores, especialistas = [], [], [], [], [], []
# Lista para armazenar as listas de cada categoria:
lista_de_categorias = [aprimoradores, emissores, transmutadores, manipuladores, conjuradores, especialistas]
# Lista de categorias em string:
str_listas_categorias = ['aprimoradores', 'emissores', 'transmutadores', 'manipuladores', 'conjuradores', 'especialistas']
# Loop for para quantidade de monitores:
for i in range(qnt_monitores):
    nome_do_monitor = input()
    alteracao = input()
    # Loop para lista de categorias
    for categoria in lista_de_categorias:
        if nome_do_monitor in categoria: # Condicional para verificar se o nome do monitor está na categoria e remove-lo da categoria.
            categoria.remove(nome_do_monitor)
    # Condicional para verificar cada alteração e adiciona-lo na categoria correspondente:
    if(alteracao == 'O volume da água foi alterado.'):
        aprimoradores.append(nome_do_monitor)
    elif(alteracao == 'A cor da água foi alterada.'):
        emissores.append(nome_do_monitor)
    elif(alteracao == 'O gosto da água foi alterado.'):
        transmutadores.append(nome_do_monitor)
    elif(alteracao == 'A folha se moveu.'):
        manipuladores.append(nome_do_monitor)
    elif(alteracao == 'Impurezas apareceram na água.'):
        conjuradores.append(nome_do_monitor)
    else:
        especialistas.append(nome_do_monitor)
# Loop para lista de categorias e imprimir:
for lista in lista_de_categorias:
    qtd = len(lista)
    categoria_str = str_listas_categorias[lista_de_categorias.index(lista)] #Obter o indíce da lista de categorias.
    incrementar_nomes = ', '.join(lista)
    if(qtd > 0):
        print(f'Temos um total de {qtd} {categoria_str} entre os monitores! Eles são: {incrementar_nomes}')

