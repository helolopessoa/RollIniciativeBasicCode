# RPG Dragonlance Option 1
# RPG Elden Ring Option 2
# RPG Generic Option 3

import random

def adicionaPlayers(quantidade, players):
    for i in range(quantidade):
        player = input("Digite o nome do combatente: ")
        inciativa = int(input("Digite o bônus de iniciativa deste combatente: "))
        vantagem = int(input("Vantagem? 0: Não // 1: Sim // 2: Desvantagem-> "))
        players.append([player, inciativa, vantagem])
    return players

def removePlayers(quantidade, players):
    print('Digite o nome dos mortos!')
    for i in range(quantidade):
        nome = input("Nome: ")
        players = [player for player in players if player[0] != nome]
    return players

def rollIniciativa(bonus, vantagem):
    roll = random.randint(1,20) + bonus
    if(not vantagem):
        return roll
    else:
        roll2 = random.randint(1,20) + bonus
        return max(roll, roll2) if vantagem == 1 else min(roll, roll2)

def rollsEmpatados(empates, players):
    if len(empates) <= 1:
        return empates
    bonus = {p[0]: p[1] for p in players}
    vantagem = {p[0]: p[2] for p in players}
    desempatados = []
    for p in empates:
        roll = rollIniciativa(bonus[p[0]], vantagem[p[0]])
        desempatados.append([p[0], roll])
    desempatados.sort(key=lambda x: x[1], reverse=True)
    return desempatados


def selectPlayers(quantidade, option):
    if type(option) != int:
        print('Opção inválida')
        combate()
    if option==1:
        players = [['Wick', 0, 0], ['Istudius', 0, 0], ['Torrbryn', 3, 0], ['Bardorc', 0, 0]]
        players = adicionaPlayers(quantidade, players)
    elif option==2:
        players = [['Lorelai', 5, 0], ['Lupita', 0, 0], ['Syg', 0, 1], ['Python', 4, 0], ['Izard', 2, 0]]
        players = adicionaPlayers(quantidade, players)
    else:
        players = []
        players = adicionaPlayers(quantidade, players)
    return players


def criaTurno(players):
    ordem = []
    for player in players:
        roll = rollIniciativa(player[1], player[2])
        ordem.append([player[0], roll])
    ordem = sorted(ordem, key=lambda x: x[1], reverse=True)
    rolls = [player[1] for player in ordem]
    duplicados = set(x for x in rolls if rolls.count(x) > 1)
    if duplicados:
        for player in ordem:
            print(player[0], player[1])
        print('Empate!')
        ordem_final = []
        i = 0
        while i < len(ordem):
            grupo_empatados = [ordem[i]]
            j = i + 1
            while j < len(ordem) and ordem[j][1] == ordem[i][1]:
                grupo_empatados.append(ordem[j])
                j += 1            
            if len(grupo_empatados) == 1:
                ordem_final.append(grupo_empatados[0])
            else:
                desempates = rollsEmpatados(grupo_empatados, players)
                ordem_final.extend(desempates)            
            i = j
        return ordem_final
    else:
        return ordem
    
def combate():
    print()
    print('RPG Dragonlance: 1')
    print('players = [[Wick, 0], [Istudius, 0], [Torrbryn, 0], [Bardorc, 0]]')
    print('RPG Elden Ring: 2')
    print('players = [[Lorelai, 0], [Lupita, 0], [Syg, 0], [Python, 4], [Izard, 2]]')
    print('RPG Generic: 3')
    option = int(input('Opção 1, 2 ou 3?: '))
    print()
    quantidade = int(input('Digite quantos combatentes (adicione e contabilize apenas NPCs se você escolheu opção 1 ou 2): '))    
    players = selectPlayers(quantidade, option)
    lutando = 1
    turno = 0
    while(lutando == 1):
        turno+=1
        ordem = criaTurno(players)
        print()
        print('Turno:', turno)
        print()
        for player in ordem:
            print(player[0], player[1])
        print()
        print('Digite:')
        print('0 para Combate Encerrado')
        print('1 para Próximo turno')
        print('2 para Alterar players (mortes ou novos players)')
        lutando = int(input('R: '))
        print()
        if(lutando == 0):
            break
        if(lutando == 2):
            print('Alterando o combate! Digite:')
            print('0 para mortes')
            print('1 para adicionar players')
            print('2 para ambos')
            novosPlayer = int(input('R: '))
            if(novosPlayer == 1):
                qntd = int(input('Quantos entraram no combate? '))
                players = adicionaPlayers(qntd, players)
            elif(novosPlayer == 0):
                qntd = int(input('Quantos morreram/saíram do combate? '))
                players = removePlayers(qntd, players)
            elif(novosPlayer == 2):
                qntd = int(input('Quantos entraram no combate? '))
                players = adicionaPlayers(qntd, players)
                qntd = int(input('Quantos morreram/saíram do combate? '))
                players = removePlayers(qntd, players)
            print()
            lutando = 1
            novosPlayer = -1


combate()