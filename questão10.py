# Entradas dos dados do Feiticeiro:
nome_feiticeiro, hp_feiticeiro, atq_feiticeiro, defesa_feiticeiro, reversao_feitiço, expansao_dominio  = input(), int(input()), int(input()), int(input()), input(), input() 

# Converter para booleano a Reversão:
if(reversao_feitiço == 'True'):
    reversao_feitiço = True
    print('Mesmo com a regeneração, ainda não vai ser fácil! Vamos nessa!')
else:
    reversao_feitiço = False
    print('Exorcizar o Mahoraga sem conseguir me curar vai ser bem difícil, mas eu não tenho escolha!')

# Converter para booleano a Expansão:
if(expansao_dominio == 'True'):
    expansao_dominio = True
else:
    expansao_dominio = False

# Entradas dos dados de Moharaga:
hp_mahoraga, atq_mahoraga, def_mahoraga  = int(input()), int(input()), int(input())

# Golpes que serão utilizados:
golpes = input().split(', ')

# Contar a quantidade de Golpes utilizados de acordo com a quantidade de golpes:
ataques_utilizados = ([0] * len(golpes))

# Loop para batalha:
while (hp_feiticeiro > 0) and (hp_mahoraga > 0):
    movimento_feiticeiro = input()
    # Condicional para saber quais são os movimentos do feiticeiro:
    if(movimento_feiticeiro == 'expansão de domínio'): 
        if(expansao_dominio == True): # Se o Golpe fatallity acontecer, etão Moharaga é derrotado.
            if(nome_feiticeiro != 'Satoru Gojo'): 
                hp_mahoraga = 0  # Moharaga é derrotado.
                print(f'Nem mesmo a sua adaptação pode derrotar isto!')
            else:
                print(f'Como assim o Mahoraga já se adaptou ao infinito de {nome_feiticeiro}!?')
        else:
            print('Droga. Eu não aprendi a expandir meu domínio ainda!')
    elif(movimento_feiticeiro == 'black flash'):
        print('As faíscas negras ignoram qualquer tipo de defesa! Toma essa Mahoraga!')
        hp_mahoraga -= ((atq_feiticeiro + 25)* 2)
    elif(movimento_feiticeiro == 'reversão de feitiço'):
        if(reversao_feitiço == True):
            hp_feiticeiro += 25
            print('Eu posso continuar lutando mais um pouco...')
    # Condicional para verificar se o golpe está na lista de golpes utilizados pelo feiticeiro e aplica-los em Mahoraga:
    elif(movimento_feiticeiro in golpes):
        if(ataques_utilizados[golpes.index(movimento_feiticeiro)]) == 0:
            hp_mahoraga -= ((atq_feiticeiro - def_mahoraga) + 25)
            print(f'A roda do Mahoraga girou uma vez! {movimento_feiticeiro} só vai funcionar mais duas vezes')
        elif(ataques_utilizados[golpes.index(movimento_feiticeiro)]) == 1:
            hp_mahoraga -= (((atq_feiticeiro - def_mahoraga) / 2) + 25)
            print(f'A roda do Mahoraga girou pela segunda vez! {movimento_feiticeiro} só vai funcionar mais uma vez')
        elif(ataques_utilizados[golpes.index(movimento_feiticeiro)]) == 2:
            hp_mahoraga -= (((atq_feiticeiro - def_mahoraga) / 4) + 25)
            print(f'A roda do Mahoraga girou pela terceira vez! {movimento_feiticeiro} não vai funcionar mais')
        elif(ataques_utilizados[golpes.index(movimento_feiticeiro)]) > 3:
            print(f'Esse ataque é inútil! Melhor tentar outra coisa.')
        ataques_utilizados[golpes.index(movimento_feiticeiro)] += 1
    else:
        print('Eu não sei que ideia é essa de tentar usar um golpe que eu não domino!')

    # Contra Ataque do Moharaga:
    if(hp_mahoraga > 0):
        movimento_mahoraga = input()
        if(movimento_mahoraga == 'ataque'):
            hp_feiticeiro -= ((atq_mahoraga - defesa_feiticeiro) + 25)
        elif(movimento_mahoraga == 'regeneração'):
            hp_mahoraga += 25
            print('Ele está se regenerando.')
        else:
            if(movimento_feiticeiro != 'black flash'):
                if(ataques_utilizados[golpes.index(movimento_feiticeiro)]) == 1:
                    print(f'A roda do Mahoraga girou pela segunda vez! {movimento_feiticeiro} só vai funcionar mais uma vez')
                elif(ataques_utilizados[golpes.index(movimento_feiticeiro)]) == 2:
                    print(f'A roda do Mahoraga girou pela terceira vez! {movimento_feiticeiro} não vai funcionar mais')
                ataques_utilizados[golpes.index(movimento_feiticeiro)] += 1
            else:
                print('Nem você vai conseguir se adaptar a isso, mahoraga!')
    if(min(ataques_utilizados) == 3): # Se houver apenas 3 ataques utilizados pelos feiticeiros entçao o Mahoraga se adaptou.
        print('Droga... Eu não tenho mais nada pra usar contra o Mahoraga... Essa luta acabou.')
        hp_feiticeiro = 0 # Moharaga ganhará.

# Finalizando as batalhas e mostrando o vencedor: 
if(hp_feiticeiro > 0):
    print(f'{nome_feiticeiro} conseguiu!')
    if(nome_feiticeiro == 'Megumi Fushiguro'):
        print('Depois de muito tempo, finalmente o Mahoraga foi exorcizado. Fushiguro é o primeiro usuário das dez sombras a conseguir esse feito!')
    elif(nome_feiticeiro == 'Sukuna') :
        print('Você me mostrou o caminho, Megumi Fushiguro, e por isso eu sou grato!')
    elif(nome_feiticeiro == 'Satoru Gojo'):
        print('Nem você sua adaptação é páreo para o infinito, queridinho.')
    else:
        print('Depois de muito tempo, finalmente o Mahoraga foi exorcizado, mas Fushiguro não participou da luta, logo o ritual foi anulado.')
else:
    if(nome_feiticeiro == 'Satoru Gojo'):
        print('Magnífico, Satoru Gojo. Lembrarei de você enquanto eu durar nesta vida.')
    else:
        print(f'Parece que nem mesmo {nome_feiticeiro} foi pareo contra o Mahoraga...')
