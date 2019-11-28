import  random

username = input('player name?') 

points = 0

b = 0
while b < 6:
    
    print('hello ' + username + '!')

    level1 = '1'
    level2 = '2'
    level3 = '3'

# Addition problems Functions section for each level 
    def additionrand1():
        a = random.randint(0,9)
        b = random.randint(0,9)
        global points
        question = input(str(a) + '+' + str(b) + '=')
        questionnub = int(question)
        answer = (a+b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')

    def additionrand10():
        a = random.randint(10,99)
        b = random.randint(10,99)
        global points
        question = input(str(a) + '+' + str(b) + '=')
        questionnub = int(question)
        answer = (a+b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')

    def additionrand100():
        a = random.randint(100,999)
        b = random.randint(100,999)
        global points
        question = input(str(a) + '+' + str(b) + '=')
        questionnub = int(question)
        answer = (a+b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')

 # Subtraction problems Functions section for each level 
    def Subtractionrand1():
        a = random.randint(0,9)
        b = random.randint(0,9)
        global points
        question = input(str(a) + '-' + str(b) + '=')
        questionnub = int(question)
        answer = (a-b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')

    def Subtractionrand10():
        a = random.randint(10,90)
        b = random.randint(10,99)
        global points
        question = input(str(a) + '-' + str(b) + '=')
        questionnub = int(question)
        answer = (a-b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')

    def Subtractionrand100():
        a = random.randint(100,999)
        b = random.randint(100,999)
        global points
        question = input(str(a) + '-' + str(b) + '=')
        questionnub = int(question)
        answer = (a-b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')

# multiplacation......................................................
    def multiplacationrand1():
        a = random.randint(0,9)
        b = random.randint(0,9)
        global points
        question = input(str(a) + '*' + str(b) + '=')
        questionnub = int(question)
        answer = (a*b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')

    def multiplacationrand10():
        a = random.randint(10,99)
        b = random.randint(10,99)
        global points
        question = input(str(a) + '*' + str(b) + '=')
        questionnub = int(question)
        answer = (a*b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')

    def multiplacationrand100():
        a = random.randint(100,999)
        b = random.randint(100,999)
        global points
        question = input(str(a) + '*' + str(b) + '=')
        questionnub = int(question)
        answer = (a*b)
        if questionnub == answer:
            print('correct')
            points = points + 100
            return(str(points) + 'pt')
        elif questionnub != answer:
            print('incorrect')
            points = points - 100
            return(str(points) + 'pt')
#...........................................

    subject1 = '1'
    subject2 = '2'
    subject3 = '3'

    subjectlist = ['Addition' , 'Subtraction' , 'Multiplacation']
    print(subjectlist)

    subjectoption = input('what subject would you like to try [1,2,3]')


        

    x = 1

    while x < 6:
        if subjectoption != subject1 and subjectoption != subject2 and subjectoption != subject3:
            print('sorry, choose again')
            subjectoption = input('what subject would you like to try [1,2,3]')
            x += 1
        else:
            break


# functions................................................................................
    def test_add():
        levellist = ['easy' , 'moderate' , 'difficult']
        print(levellist)
        leveloption_add = input('What level would you like to try? [1,2,3]')
        x = 1
        while x < 6:
            if leveloption_add != level1 and leveloption_add != level2 and leveloption_add != level3:
                print('sorry, choose again')
                leveloption_add = input('What level would you like to try? [1,2,3]')
                x += 1
            else:
                break
        a = 1
        while a < 6:
            if leveloption_add != True:
                if leveloption_add == level1:
                    print(additionrand1())
                    a += 1      
                elif leveloption_add == level2:
                    print(additionrand10())
                    a += 1
                elif leveloption_add == level3:
                    print(additionrand100())
                    a += 1
                else:
                    print('nul')

#.......................................................................................
    def test_sub():
        levellist = ['easy' , 'moderate' , 'difficult']
        print(levellist)
        leveloption_sub = input('What level would you like to try? [1,2,3]')
        x = 1
        while x < 6:
            if leveloption_sub != level1 and leveloption_sub != level2 and leveloption_sub != level3:
                print('sorry, choose again')
                leveloption_sub = input('What level would you like to try? [1,2,3]')
                x += 1
            else:
                break
        a = 1
        while a < 6:
            if leveloption_sub != True:
                if leveloption_sub == level1:
                    print(Subtractionrand1())
                    a += 1      
                elif leveloption_sub == level2:
                    print(Subtractionrand10())
                    a += 1
                elif leveloption_sub == level3:
                    print(Subtractionrand100())
                    a += 1
                else:
                    print('nul')

    def test_mult():
        levellist = ['easy' , 'moderate' , 'difficult']
        print(levellist)
        leveloption_mult = input('What level would you like to try? [1,2,3]')
        x = 1
        while x < 6:
            if leveloption_mult != level1 and leveloption_mult != level2 and leveloption_mult != level3:
                print('sorry, choose again')
                leveloption_mult = input('What level would you like to try? [1,2,3]')
                x += 1
            else:
                break
        a = 1
        while a < 6:
            if leveloption_mult != True:
                if leveloption_mult == level1:
                    print(multiplacationrand1())
                    a += 1      
                elif leveloption_mult == level2:
                    print(multiplacationrand10())
                    a += 1
                elif leveloption_mult == level3:
                    print(multiplacationrand100())
                    a += 1
                else:
                    print('nul')




    if subjectoption == subject1:
        print(test_add())
    elif subjectoption == subject2:
        print(test_sub())
    elif subjectoption == subject3:
        print(test_mult())




    print('You have a total of ' + str(points) + ' points!')
    q = input('Would you like to keep going? [y/n]')
    
if q == 'y' or q == 'Y':
    pass
elif q != 'y' and q != 'Y' and q != 'n' and q != 'N':
    print('sorry, choose again')
    q = input('Would you like to keep going? [y/n]')
    b += 1
    pass
else q == "n" or q == "N":
    break

    

   





