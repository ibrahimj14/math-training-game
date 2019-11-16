import random

username = input('player name?') 

b = 1
while b < 6:
    
    print('hello ' + username + '!')

    level1 = '1'
    level2 = '2'
    level3 = '3'

    # Addition problems Functions section for each level 
    def additionrand1():
        points = 0
        a = random.randint(0,9)
        b = random.randint(0,9)
        question = input(str(a) + '+' + str(b) + '=')
        questionnub = int(question)
        answer = (a+b)
        if questionnub == answer:
            print('correct')
            points += 100
            print(str(points))
        elif questionnub != answer:
            print('incorrect')
            points -= 100
            print(str(points))

    def additionrand10():
        a = random.randint(10,99)
        b = random.randint(10,99)
        question = input(str(a) + '+' + str(b) + '=')
        questionnub = int(question)
        answer = (a+b)
        if questionnub == answer:
            print('correct')
        elif questionnub != answer:
            print('incorrect')

    def additionrand100():
        a = random.randint(100,999)
        b = random.randint(100,999)
        question = input(str(a) + '+' + str(b) + '=')
        questionnub = int(question)
        answer = (a+b)
        if questionnub == answer:
            print('correct')
        elif questionnub != answer:
            print('incorrect')



    
    levellist = ['easy' , 'moderate' , 'difficult']

    print(levellist)

    leveloption = input('What level would you like to try? [1,2,3]')

    x = 1

    while x < 6:
        if leveloption != level1 and leveloption != level2 and leveloption != level3:
            player_option = True
            print('sorry, choose again')
            leveloption = input('What level would you like to try? [1,2,3]')
            x += 1
        else:
            break


    a = 1
    while a < 6:
        if leveloption != True:
            if leveloption == level1:
                print(additionrand1())
                a += 1      
            elif leveloption == level2:
                print(additionrand10())
                a += 1
            elif leveloption == level3:
                print(additionrand100())
                a += 1
            else:
                print('nul')

    q = input(' would you like to quit [y/n]')
    if q == 'n' or q == 'N':
        pass
    elif q == "y" or q == "Y":
        break
    else:
        break





