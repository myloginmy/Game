import math
import random
import sys
army=50
gold=5000
food=1000
ground=100
revolution=0
people=100
year=0
while revolution<100 and people>=20:
    year += 1
    food = food-people
    print("Идет год №", year)
    print("Хотите купить зерно?")
    a = input()
    if a == "yes":
        print("Сколько зерна хотите купить?")
        b = int(input())
        if 7*b > gold:
            print("Не хватает денег, милорд")
        food = food + b
        gold=gold-7*b
    else:
        break
    print("Хотите продать зерно?")
    c = input()
    if c = "yes":
        print("сколько зерна хотите продать?")
        d = int(input())
        if d > food:
            print("Не хватает зерна, милорд")
        else:
            food = food - d
            gold = gold + d*5
    else:
        break
    print("Хотите посеять зерно?")
    e = input()
    if e == "yes":
        print("Сколько зерна хотите посеять?")
        f = int(input())
        if f > food and f > ground:
            print("Не хватает зерна/земли, милорд")
        else:
            food = food*3
    else:
        break
    print("хотите купить землю милорд?")
    g = input()
    if g == "yes":
        print("Сколько земли хотите купить?")
        u = int(input())
        if u*200 > gold:
            print("Не хватает денег, милорд")
        else:
            gold=gold-u*200
            ground = ground + u
    else:
        break
#война/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    big_army_k=200+random.randint(1,200)
    mid_army_k=100+random.randint(1,100)
    small_army_k=50+random.randint(1,50)
    big_army_k2=big_army_k
    mid_army_k2=mid_army_k
    small_army_k2=small_army_k
    win=0
    big_war='Господин, на вас напали мертвецы Сильвании, у них',big_army_k,'войнов. нужно готовиться к страшной войне'
    mid_war='Милорд, через шахты на поверхность вышел отряд гномов из заснеженного Кордара, мы должны защитить народ. Их',mid_army_k,', ни одна деревня не сможет отразить такое нападение самостоятельно '
    small_war='О, величайший из правителей живших на этой земле, наши границы грабят пиратские банды Островов Свободы их всего-то',small_army_k,'собирайте людей, время покарать нахалов'
    def enemy_army():
        k=random.randint(1,90)
        if k>60:
            return big_war
        elif 30<k<=60:
            return mid_war
        else:
            return small_war
    war_k = random.randint(1, 100)
    war = war_k
    if war <= 20:
        transition=enemy_army()
        print(transition)
        if transition==big_war:
            print('для того, чтобы противостоять угрозе с запада, нам нужно нанять',(big_army_k2-army),'людей, на это нужно,на их содержание потребуется',((big_army_k2-army)*25),'золота')
            if gold<((big_army_k2-army)*25):
                print('О, мой король, похоже  это конец, мне жаль, но ваш отец так и не будет отмщен. Ну а вы, вы скорее всего, будете поданы, как еда для графов древних родов вампиров ')
                win=0
                break
            else:
                gold-=((big_army_k2-army)*25)
                print('ПОБЕЕЕДА!!!!!! Мой господин,мы одержали победу, эти крысы вновь забились в свои могилы ')
                win=1
                army=0
        if transition==mid_war:
            print('для того, чтобы противостоять угрозе c севера, нам нужо нанять',(mid_army_k2-army),'людей, на это нужно,на их содержание потребуется',((mid_army_k2-army)*25),'золота')
            if gold<((mid_army_k2-army)*25):
                print('Какой позор, голова правителя величайшей державы людей украсит стены столицы коротышек!!!')
                win=0
                break
            else:
                gold-=((mid_army_k2-army)*25)
                print('Ваше Величество, это была решительная победа, проклятые карлики не скоро к нам сунутся')
                win=1
                army=0
        else:
            print('для того, чтобы противостоять угрозе c юга, нам нужо нанять', (small_army_k2-army),'людей, на это нужно,на их содержание потребуется', ((small_army_k2-army) * 25), 'золота')
            if gold<((small_army_k2-army)*25):
                print('Повелитель, это неслыханно, вы опозорили себя и свой род, проиграв ничтожную стычку с шайкой бандитов, возомнивших себя выше законов империи')
                win=0
                break
            else:
                gold-=((small_army_k2-army)*25)
                print('предсказуемая, но от этого не менее блестящая победа, господин')
                win=1
                army=0
#события...........................................................................................................................................................................................
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    hurricane_k=random.randint(1,100)
    hurricane=hurricane_k
    plugue_k=random.randint(1,100)
    plugue=plugue_k
    ban_k=random.randint(1,1000)
    ban=ban_k
    riot_k=random.randint(1,100)
    riot=riot_k
    if hurricane<=10:
        print('по вашим землям прошел ураган и уничтожил часть амбаров с зерном')
        food-=random.randint(1,food*0.4)
        revolution+=1
    if plugue<=10:
        print('на ваших землях свирепствует неизвестная болезнь: с людей заживо сползает кожа и вытекают глаза')
        revolution+=5
        people-=random.randint(1,people*0.35)
    if ban<=50:
        print('Спасайся кто может!!! Милорд, Вы прогневали древних богов хаоса и они...аааааааааааа *на ваших глазах в окно влетел огромный ворон и разорвал советника на части, забрызгав вас кишками и кровью, а потом,'
            'облизываясь раздвоенным языком уставил на ваc 6 пар кровожадных глаз...')
        print('------------------------:+##@==========++******=++++*:***:::---------.-.-:*=%=%:....................')
        print('---------------------:::::@@%====%%===++++++****+**++*:**::::-:-------..-:+===:.....................')
        print('-----------------:::::::::@@======++======++=+**+**=**:*:::::::::-----..--*=+=-.....................')
        print('--------------::::**+*:::*@==+=%==============+++*:=+++***::*++=+*++:---..:=++......................')
        print('-------------::=%@@%%==%%%%==%@@%%%%%@@@%===%==%=+:*%+==+===%%%%%+++++:----+=*..:++*::-.............')
        print('-----------:-*%@@@@@@#@%%@%=%%@@@@@@@@##@@@#@@@@%=+*+%%%%%@@@@@%%%%=+++*-.-*%=======@@@%*-..........')
        print('-----------:-=%%%%%%%=@#@@==%@@@@##############=+::::*=%%@#%@@%===#%=+*:---:+*++%%==+=%@#%-.........')
        print('--------:::::=%%%%%=%%@#@@===%@@@@@%%@@%%@###@=**::::**=%%%=+%%=*+:*++::-..-+**%@=++++%@@@*.........')
        print('--------:::::+=%%%%%@@@##%========%==%====%@@%++*::--::+++=++++**:-------..-+*++=++**+%@@@*.........')
        print('---::::::::::+==@%%@@####%%===+++=+=+====%%%%%+**:------:*****::--------.--:+=#@%==+*+==%=..........')
        print('--:::::::::::*==@%%@@#@##%%%%%=====++====%%%%=+**:--------:::**::-----.----::+%@%%==*+=%%-..........')
        print(':-::::::::::::+=%@%@@@@@@@%%%%%%%========@@%%==+*:----:-----::::::--------::-++=@%%+*+==-...........')
        print(':-:::::::::::::+=@@%%%%@@@@@@@%%%%======%@%%%=++*:::::*+::--::::::::::::::::***+%%=+*++-............')
        print('::::::::::::::::*=%@@@%%%%@%@@%%%======%@@@@@%%+**:::-:++::::::::::::::::*::++++*+*++*..............')
        print(':::::::::::::::::*+%=%%@@@@@@%%%%%%%==%@@#####%===##%+:+=+*:::::::-::::::::++*::+++*-...............')
        print('::::::::::::*********=%%%@#@%@%%%%%%%=%%%######%+++%@=+*+++*::::::::::::=+::==:-:*-.................')
        print(':::::::::::*************+**%%%%%%%%%%%%%%@##@%===+*+**:::***:::::::::::*++=++*-.....................')
        print(':::::::::::**************::%%@%%%%%%@@@@@@@#@@=%===+=+*+**::::::::::::::::-.........................')
        print('::::::::::::**************:=%%%%%@@@%%%%%%@@@%=+==+*+*******::::--::::::::-.........................')
        print(':::::::::::*************:::=@%%%%@@@@@#######@@%%==%%%+**+**:::::-::::::::..........................')
        print(':::::::::::***************:+@%%%%@##@@@@%%=+=+==++++++++=%=+**::::::*:::::..........................')
        print('::::::::::::**************:*@@@@@@@@##@#@@@=++=++**::::+**++++***::::::::-..........................')
        print(':::::::::::::**:*********::*@@@@@@@@#######@@@@%@%%%==%%===+++***:::::*::-..........................')
        print('::::::::::::::*::********:::%@@#@@@@@@@@@@###@@%=+*:::-:*++++**++**:::**:-..........................')
        print('::::::::::::::::*::*****::::=@@###@#@@@@@%@@@%%===+*+*+=++=+=++**:::**:*:-..........................')
        print('::::::::::::::::::*******:::+@@#####@####@@@@@%%%%=%=====+=+++**:::****::*-.........................')
        print(':-:::::::::::::*::*:*****:::*@@@####@########@@@@@@%%%+*+***:::::::***:::@@=-.......................')
        print(':::::::::::::::::*********:*=@@@@@##@########@@@@@%%===++*:::::-::****:::=#%=:......................')
        break
    if  riot<=10:
        print('Ииииииииииииииизменаааа! Заговорщики подняли бунт. КАЗНИТЬ! ВСЕХ! ВСЕХ КАЗНИТЬ!! И СЖЕЧЬ ДОТЛА ИХ ДОМА И СЕМЬИ!!!')
        print('после расправы над предателями вас назвали кровавым тираном')
        revolution+=10
    repressions='df'
    print('Не кажется ли вашей милости, что пора бы поунять недовольных в империи?')
    while repressions!='да' and repressions!='нет':
        repressions = input()
        if repressions=='да':
            gold*=0.5
            revolution=0
        elif repressions=='нет':
            print('ваша воля, хозяин судеб')
        else:
            print('говорите яснее, о, синее пламя, пляшущее на курганах врагов')
    sys.stdout.flush()
    print('еда-',food)
    print('население-',people)
    print('казна-',gold)
    print('бунт-',revolution)
    print('год-',year)
print('Потрачено')


