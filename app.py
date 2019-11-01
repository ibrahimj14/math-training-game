import random


username = input('player name?') 
print('hello' + username + '!')

level1 = '1'
level2 = '2'
level3 = '3'
 
levellist = ['easy' , 'moderate' , 'difficult']

print(levellist)

leveloption = input('What level would you like to try? [1,2,3]')

level1 = str('1')
level2 = str('2')
level3 = str('3')

if leveloption != level1:
    print('sorry, choose again')
elif leveloption != level2:
    print('sorry, choose again')
elif leveloption != level3:
    print('sorry, choose again')

def additionrand1():
    a = random.randint(0,9)
    b = random.randint(0,9)
    question = input(str(a) + '+' + str(b) + '=')
    questionnub = int(question)
    answer = (a+b)
    if questionnub == answer:
        print('correct')
    if questionnub != answer:
        print('incorrect')





a = 1
while a < 6:
    if leveloption == level1:
        print(additionrand1())
        a += 1
    else:
        break


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


b = 1 
while b < 6:        
    if leveloption == level2:
        print(additionrand10())
        b += 1
    else:
        break

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

c = 1 
while c < 6:
    if leveloption == level3:
        print(additionrand100())
        c += 1
    else:
        break

  #leaving the while loop in the if statment on line 52 will run all if statments after loop is done exicuting. add another set of conditional statments at the bottom aloung with the loop. 

