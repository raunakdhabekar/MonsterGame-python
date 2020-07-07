
from random import randint
gameRun= True
def playerAttack():
        return randint(player['attack_min'],player['attack_max'])
def gameEnd(winner):
        print(f'{winner} won')
result_history =[]

while gameRun== True :
    monster = {'name': 'gandu', 'attack': 20, 'heal':30, 'health':100}
    player= {'name': 'raunak','attack_min': 12,'attack_max': 22,'heal':16,'health':100}
    newGame=  True
    counter = 0
    print('player name:')
    player['name']= input()
    print(player)
    
    while newGame== True:

        playerwins = False
        monsterwins = False
        counter = counter +1
        print('please select one of the options :')
        print('1)attack')
        print('2)heal')
        print('3)Exit')
        print('4)Show all results')

        choice= input()

        if choice =='1':
            monster['health']= monster['health']-playerAttack()
            print('monster-',monster['health'])
            if monster['health'] <= 0:
                    playerwins = True
                    print('player won')  
            else:
                    player['health']= player['health']-monster['attack']
                    print('player-',player['health'])  
                    if player['health'] <= 0:
                        monsterwins = True
                        print('monster won') 
                    
        elif choice=='2':
            player['health']= player['health'] + player['heal']
            print('The player is healing')
            print('your health is restored   health:',player['health'])

        elif choice=='3':
            newGame=False
            gameRun=False
        
        elif choice=='4':
            for item in result_history:
                print(item)
           

        else :
            print('invalid choice')

        if playerwins == False and monsterwins == False:
            newGame=True
            print('het')
 
        elif playerwins==True:
                gameEnd(player['name'])
                result= {'rounds':counter}
                result_history.append(result)
                newGame=False
                print(result_history)
        elif monsterwins==True:
                gameEnd(monster['name'])
                result= {'rounds':counter}
                result_history.append(result)
                newGame=False
                print(result_history)
            
        print('player:',player['health'] ,'monster health:',monster['health'])
        
print('thanks for playing the game')


