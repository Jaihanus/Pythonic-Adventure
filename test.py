import time


total_hp = 10
ko = False

victory = 3

both_guild = 3
choice = 3275872368946
punch = 3429532
negative = "nuh uh what shut up silence idiot of course not no way you're bald deez nuts get rekt non i do not"
positive = "affirmative yes of course yeah :) do it oui oui i do confirm"
insult = "screw you suck on deez nuts you're bald you are bald head l + ratio die loser"
reply_1 = "Get strapped or get clapped they say. (Punch him)"
reply_2 = "My Good Sire I have come to the realization after much rumination that you intended no great ill to befall me and were just 'trolling'."
reply_3 = "Give me all you have or you die."
reply_4 = "*cry*"
def fight (sword = 1, money = 1, armor = 1, enemy = "joe biden" , enemyhp = 2, enemy_attack = 1):
    '''
    Does the fight scenes with the inputs of current gear
    Requires info on the current enemy
    '''
    global total_hp
    option = input("Will you attack, defend, or bribe your enemy?").lower()
    if option[0] == "a":
        enemyhp = enemyhp - sword
    if option[0] == "d":
        damage = enemy_attack - armor
        if damage < 0:
            print("no damage taken!  Nice block bro")
        else:
            total_hp = total_hp - damage
            print("you took", damage, "hitpoints of damage. You have", total_hp, "left")
    if option[0] == "b":
        print('They saw you open your money bag, shouted, "he has a grenade!", then ran for their life.')
        global victory 
        victory = True
        f = ""
        return f
    if enemyhp <= 0:
        print("The robber tries running at you with his knife, but you punch him in the head and he goes down.")
        victory = True
        f = ""
        return f
    if total_hp <= 0:
        victory = False
        f = ""
        return f
    else:
        fight(sword, money, armor, enemy, enemyhp, enemy_attack)

def bread ():
    '''
    Repeats the question if the user inputs an invalid answer
    '''
    response = input("Do you accept this offer?")
    if response.lower() in positive:
        print('"'+"You are a wise wanderer.  The kit will arrive tomorrow.  In the meantime, let's continue, eh?"+'"')
        global kit
        kit = True

    elif response.lower() in negative:
        print('"'+"bruh fr? ok anyway, let's continue"+'"')
        kit = False
    elif response.lower() in insult:
        print('"'+"say that again. I dare you."+'"')
        bread()
    else:
        print('"'+"can you speak up?"+'"')
        bread()

def response ():      
    reply = input()
    if reply == "1":
        print("The weird wizard guide guy got knocked out cold and hit the ground. Good riddance you think to yourself.")
        global ko
        ko = True
    elif reply == "2":
        print('"'+"Well uh... Yeah I was just trolling. Let's uh... continue."+'"')
        global both_guild
        both_guild = True
    elif reply == "3":
        print('"'+ f"O-of course {first_name} {last_name}.  Right away."+'"')
    elif reply == "4":
        print('"'+"cry harder lol"+'"')
        print("The wizard runs away but trips on a rock.")
    else:
        print("What is blud yapping about? (write just the number of the reply)")
        time.sleep(1)
        response()
        
def walking():
    print("Walking", end = "")
    for i in range(10):
        time.sleep(1)
        print(".", end ="")
    print(" ")
print("A Wizard greets you.") 
first_name = input('"'+"What is your first name wanderer?"+'"').capitalize()
last_name = input('"'+"And what is the name of your family?"+'"').capitalize()
print('"'+f"Welcome to the world of Cardia {first_name} {last_name}.  Before we continue, I would like to plug our sponsor fail better legends, where you can get a free raid kit including 100 gold coins."+'"')

#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
bread()
time.sleep(2)
print('"'+"Let's go walk to the adventurer's guild.  Let's hope that we don't get attacked along the way."+'"')

if kit == False:  #Depends on if user said yes, False = no, True = yes
    time.sleep(3)
    print('"'+"Wow you got attacked.  Wish you had that kit, don't you? Toodles, LOL"+'"')
    print("begin fight!")
    foe = "Sus guy"
    foehp = 3
    foe_attack = 1
    weapon = 10
    money = 12
    armor = 0
    fight(weapon, money, armor, foe, foehp, foe_attack)
elif kit == True:
    weapon = 1
    money = 112
    armor = 6
    foe = "Sus guy"
    foehp = 3
    foe_attack = 1
    both_guild = True
else:
    weapon = 1
    money = 1
    armor = 1
    foe = "Sus guy"
    foehp = 3
    foe_attack = 1
    fight(weapon, money, armor, foe, foehp, foe_attack)
    

        
    
if victory == True:  #Only fires if user chose the no path
    time.sleep(3)
    print("You catch up to the Wizard.")
    time.sleep(3)
    print('"'+"uhh..... you aren't.... weren't...."+'"')
    time.sleep(3)
    print("*sigh*",'"'+ "fine, here's 400 coins."+'"')
    time.sleep(3)
    print("What do you reply with? \n 1. Get strapped or get clapped they say.  (Punch him) \n 2. My Good Sire I have come to the realization after much rumination that you intended no great ill to befall me and were just 'trolling'. \n 3. Give me all you have or you die. \n 4. *cry* ")
    response()
elif victory == False:
    print("The robber beats you up and you cry all the while. The robber goes through your stuff, but finding nothing the robber leaves.  You vow to yourself to follow the thief and get vengeance.")

if both_guild == True: #
    walking()
    print('"'+"Wow! We made it. How fortunate! Let's get you registered."+'"')
    time.sleep(1)
    print('"'+"They need you to answer a couple questions before they accept you. Practice them by talking to me."+'"')
    time.sleep(1)
    input("Where do you live?")
    time.sleep(1)
    input("How many people are in your family?")
    time.sleep(1)
    input("How strong are you?")
    time.sleep(3)
    print("The Wizard looks at you, and suddenly you feel wobbly. \n"+'"'+"Thank you for putting on the kit LOSER! HA! It only means that I can put you to sleep. All I NEEDED to do was distract you for long enough. Farewell loser!"+'"')
    choice = input("Punch him?").lower()
    if choice in positive:
        print("You punch him.  Your sight goes back to normal as he falls.")
        punch = True
    elif choice in negative:
        print("Your face turns into that of despair.  The Wizard's smug countenance shifts into that of guilt as the world turns black.") 
        punch = False

if ko == True:
    print("You rummage through the Wizard's things and find the kit he offered, alongside 1000 coins. Do you take it?")
    loot = input().lower()
    if loot in positive:
        print("You take the gear and start walking to the adventurer's guild.")
        walking()
        print("When you get there, you start feeling ill, and the world goes dark.")
        punch = False
    elif loot in negative:
        print("you decide to leave the gear behind and continue on to the adventurer's guild.")
        walking()
        print("you arrive at the adventurer's guild without further incident.  You happily decide
    else:
        print("Confused as to what to do, you choose to knock yourself out. (invalid input)")

if punch == False:
    time.sleep(5)
    wake_up = "\"Are you okay?\" \n" 
    for char in wake_up:
        print(char, end="")
        time.sleep(.25)
print("This is the end of the game.")
