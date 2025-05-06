sequencia_gojo = input().split('-')
sequencia_gojo_int = []
tamanho_sequencia_geto = int(input())
soma_sequencia_geto = int(input())

# Transformar a lista da sequencia de gojo em inteiro
for num in sequencia_gojo:
    sequencia_gojo_int.append(int(num)) # Adicionar na lista

resultado = [[sequencia_gojo_int[0]]] # Inicia resultado com o primeiro número dentro de uma sequencias.

# Percorre a lista a partir do segundo elemento com o índice i:
for i in range(1, len(sequencia_gojo_int)):
    if((sequencia_gojo_int[i] - sequencia_gojo_int[i - 1]) == 1): # Verifica se a diferença entre o elemento e seu antecessor é igual a 1, ou seja, possui sequencia de período 1.
        resultado[-1].append(sequencia_gojo_int[i]) # Adiciona ao ultimo grupo da lista resultado.
    else:
        resultado.append([sequencia_gojo_int[i]]) # Caso contrário, adiciona uma nova sequencias para o elemento.

maior_tamanho = resultado[0] # Inicia o maior tamanho com o primeiro número dentro da lista resultado.
maiores_sequencia = [] # Lista para acrescentar a(s) maior(es) sequencia(s) válida(s).

# PPercorre todos os elementos da lista resultado, onde cada elemento é uma sequência:
for sequencias in resultado:
    # Verifica se a sequência atual é uma SEQUÊNCIA VÁLIDA (i.e., tamanho maior que 1) e se possui o maior tamanho encontrado até agora:
    if((len(sequencias) > len(maior_tamanho)) and len(sequencias) > 1): 
        maior_tamanho = sequencias # Atualiza maior_tamanho com a nova sequência de maior tamanho
        maiores_sequencia = [sequencias] # Reinicia (atualiza) a lista com essa nova sequência como a única maior encontrada
    elif((len(sequencias) == len(maior_tamanho)) and len(sequencias) > 1): # Caso exista duas sequências válidas de tamanho iguais.
        maiores_sequencia.append(sequencias) # Adiciona na lista de maiores sequencias

# Verificar o tamanho da sequência:
if(len(maiores_sequencia) == 1):
    soma = sum(maiores_sequencia[0]) # Resultado da soma para a única sequência válida.
    melhor_sequencia = maiores_sequencia[0] # Resultado da melhor sequencia 
elif(len(maiores_sequencia) > 1): # Se há mais de uma sequencia.
    maior_soma = sum(maiores_sequencia[0]) # Assumir, incialmente, que a maior soma é a da primeira sequencia.
    melhor_sequencia = maiores_sequencia[0]  # Assumir que a primeira sequência é a maior inicialmente.

    for sequencia in maiores_sequencia[1:]: # Sequencia vai perecorrer todas os sequencias da lista de maiores sequencias exceto a 1ª sequencia.
        soma_atual = sum(sequencia) # Calcular a soma da sequencia atual. 
        
        # Verificar se a soma atual é maior que a soma registrada inicialmente:
        if(soma_atual > maior_soma):
            maior_soma = soma_atual # Atualizar quem é a maior soma.
            melhor_sequencia = sequencia # Atualizar quem é a melhor sequencia para GOJO
    soma = maior_soma # O resultado da soma da melhor sequencia para GOJO

# Condicional para verificar o vencedor entre GOJO e GETO ou se haverá um empate:
if(len(melhor_sequencia) > tamanho_sequencia_geto):
    print('Uma vitória avassaladora de Satoru Gojo. Nem mesmo o infinito pode pará-lo. Ele realmente é o melhor!')
elif(len(melhor_sequencia) < tamanho_sequencia_geto):
    print('Inesperado! Suguru Geto domina com maestria. Uma vitória indiscutível!')
else:
    if(soma > soma_sequencia_geto):
        print('Gojo vence por pouco. Mesmo com toda a pressão, ele continua no topo!')
    elif(soma < soma_sequencia_geto):
        print('Geto vence por pouco. Sua estratégia foi impecável nesta batalha!')
    else:
        print('Um empate absoluto! Quem diria que duas lendas podem ser tão iguais em poder?')