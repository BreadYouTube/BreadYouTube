import random
import time

value = random.randint(1, 50)

CashierMenu = ["cheeseburger?", "drink?", "fries?", "pickle burger?", "burger?"]
ChefMenu = ["cheeseburger", "drink", "fries", "pickle burger", "burger"]
ManagerName = ["Mike", "Rick", "Sam", "Tommy", "Harvey", "Jack"]
OneChoiceFromManager = ["Hire and fire", "Bonuses", "Promotion"]
Crimes = ["Murder", "Robbery", "None"]
Reason = ["Money", "Rather not say", "Help", "Trolling"]
ManagerJobFirst = ["Chef", "Cashier", "Finance Rep."]
ManagerJobSecond = ["Chef", "Cashier"]
FirstQuestionThing = ["'Because I would love to help out others and make the business more recognisable.'",
                      "'Trolling lol.'",
                      "'I need money to pay my rent.'"]
SecondQuestionThing = ["Yes! Yes I am!", "Uhh... no?", "I have no idea."]
ThirdQuestionThing = ["I would go the manager and let him take care of you.", "Argue back.", "Do nothing."]

print("Welcome to Job Simulator!")
time.sleep(2)
print("Just wanted to say thank you for trying out my game! You can check out my other programs on my GitHub!")
time.sleep(4)
print("Please report any bugs and you can send solutions to fix the bugs, thanks!")
print("My YouTube channel: https://www.youtube.com/channel/UCCl8SfFGp-ChbIvQI9ke6lQ")
time.sleep(3)
print("Which job do you want first?")
time.sleep(3)
print("1. Cashier\n2. Helpline (In Coding)")
PlayerJobChoice = input("")
print("Great! Let's begin!")
time.sleep(2)
if PlayerJobChoice == "1":
    print("Would you like to see a tutorial?\n1. Yes\n2. No\nOr just press any other key and then press enter")
    print("If you would like to see a tutorial you would have to restart.")
    YON = input("")
    if YON == "1":
        print("This is a game where you have to become the manager of the store! By starting from the lowest...")
        time.sleep(3)
        print("Here is your first customer!")
        time.sleep(1)
        print("'Hi can I get a cheeseburger?'")
        time.sleep(2)
        input("Look at the menu to see what number is the cheeseburger! (press enter to look at it)")
        print("1. Cheeseburger\n2.Fries\n3.Drink\n4.Pickle burger\n5. Burger ")
        input("Memorise this because you will not see this again! Press enter when you are ready.")
        print("'Can I have a cheeseburger?'")
        time.sleep(1)
        PlayerGivesCustomer = None
        while PlayerGivesCustomer != "1":
            print("Press 1 then press enter to give her the cheeseburger!")
            PlayerGivesCustomer = input("")
            if PlayerGivesCustomer == "1":
                print("'Thank you!'")
                time.sleep(1)
                print("You have completed the tutorial! You may now play.")
            else:
                continue
    else:
        print("Let's start!")
        print("Help 10 customers get their order to be promoted!")
        promo = 0
        while promo != 1:
            CustomersNumber = "0"
            CashierMenuRandom = random.choice(CashierMenu)
            print("'Can I get the " + CashierMenuRandom + "'")
            if CashierMenuRandom == "cheeseburger?":
                CustomersNumber = "1"
            elif CashierMenuRandom == "drink?":
                CustomersNumber = "3"
            elif CashierMenuRandom == "fries?":
                CustomersNumber = "2"
            elif CashierMenuRandom == "pickle burger?":
                CustomersNumber = "4"
            else:
                CustomersNumber = "5"
            input("1. Cheeseburger\n2.Fries\n3.Drink\n4.Pickle burger\n5. Burger (Press enter when you are ready.)")
            print("Please can I get the " + CashierMenuRandom)
            PlayerGivesCustomer = input("")
            if PlayerGivesCustomer != CustomersNumber:
                print("'Wow what a joke.'")
            elif PlayerGivesCustomer == CustomersNumber:
                print("'You are the best!'")
                promo += 1
            CashierMenuRandom = random.choice(CashierMenu)
            print(" ")
        print(" ")
        print("Good job! You got promoted to...")
        time.sleep(3)
        print("Chef!")
        print("Would you like to see a tutorial?\n1. Yes\n2. No\nOr just press any other key and then press enter")
        YON = input("")
        if YON == "1":
            print("Ok let's start!")
            time.sleep(2)
            print("First order is here!")
            time.sleep(2)
            print("'We need the... cheeseburger!'")
            print("This is the ingredients list! Type the numbers in order to make the order!")
            print("1. Bun\n2. Cheese\n3. Patty\n4. Pickle\n5. Fries\n6. Drink")
            time.sleep(2)
            input("Press enter to go to the next part.")
            print("1. Cheeseburger = Bun, Patty, Cheese, Bun\n2. Fries = Fries\n3. Drink = Drink")
            print("4. Pickle burger = Bun, Patty, Pickle, Pickle, Bun\n5. Burger = Bun, Patty, Cheese, Pickle, Bun")
            input("Press enter when you are ready.")
            print("'I said we need the cheeseburger!'")
            time.sleep(2)
            TutorialCheese = "0"
            while TutorialCheese != "1321":
                print("Type in: 1321! 1 = Bun, 3 = Patty, 2 = Cheese, 1 = Bun.")
                TutorialCheese = input("")
                if TutorialCheese == "1321":
                    print("Great! You have completed the tutorial!")
                else:
                    continue
        else:
            print("Ok let's start!")
            time.sleep(3)
            print("Get 25 customers their order!")
            promo = 0
            CustomersNumber = "0"
            while promo != 1:
                ChefMenuRandom = random.choice(ChefMenu)
                if ChefMenuRandom == "cheeseburger":
                    CustomersNumber = "1321"
                elif ChefMenuRandom == "drink":
                    CustomersNumber = "6"
                elif ChefMenuRandom == "fries":
                    CustomersNumber = "5"
                elif ChefMenuRandom == "pickle burger":
                    CustomersNumber = "13441"
                else:
                    CustomersNumber = "13241"
                print("'We need the... " + ChefMenuRandom + "!'")
                print("1. Bun\n2. Cheese\n3. Patty\n4. Pickle\n5. Fries\n6. Drink")
                print("1. Cheeseburger = Bun, Patty, Cheese, Bun\n2. Fries = Fries\n3. Drink = Drink")
                print("4. Pickle burger = Bun, Patty, Pickle, Pickle, Bun\n5. Burger = Bun, Patty, Cheese, Pickle, Bun")
                input("Press enter to continue.")
                print("'I said, we need the " + ChefMenuRandom + "!'")
                time.sleep(1)
                ChefsResponse = input("")
                if ChefsResponse != CustomersNumber:
                    print("THIS IS THE WRONG ORDER!")
                elif ChefsResponse == CustomersNumber:
                    print("'Good job...'")
                    promo += 1
                ChefMenuRandom = random.choice(ChefMenu)
                print(" ")
            print(" ")
            print(" ")
            print("Great job! You have been promoted to...\nManager!")
            time.sleep(2)
            print("The manager retired and decided to choose you and that is how you became manager!")
            time.sleep(5)
            print("Would you like to see a tutorial?\n1. Yes\n2. No\nOr just press any other key and then press enter")
            YON = input("")
            if YON == "1":
                print("Ok let's start!")
                time.sleep(2)
                print("For this, you must hire, fire, and decide to give bonuses.")
                time.sleep(2)
                print("You can also decide other stuff like raise how much promo you need to be promoted.")
                time.sleep(3)
                print("First employee coming!")
                time.sleep(3)
                print("'Can I get promoted?'")
                input("Press enter to check his status.")
                print("Name is: Tommy")
                print("Promo is: 24")
                print("Job is: Cashier")
                input("Press enter when you are ready.")
                print("'So uhh, can I get promoted?'")
                ManagerYON = None
                while ManagerYON != "2":
                    print("You need to say no because he does not have enough promo to be promoted.")
                    print("1 is yes and 2 is no.")
                    ManagerYON = input("")
                    if ManagerYON == "1":
                        continue
                    elif ManagerYON == "2":
                        print("Aww man.")
                        print("Good job!")
                    else:
                        print("That is not an option!")
                        continue
                print("Now on to the bonuses part.")
                time.sleep(2)
                print("When you became manager you got $500,000!")
                time.sleep(3)
                print("If you give someone a bonus, you lose money!")
                time.sleep(1)
                print("Oh here comes another employee.")
                time.sleep(1)
                print("'Can I get a bonus??'")
                input("Press enter to check his status.")
                print("Name is: Rick")
                print("Promo is: 48")
                print("Job is: Chef")
                input("Press enter when you are ready.")
                print("'So uhh, can I get a bonus?'")
                ManagerYONBonus = "0"
                while ManagerYONBonus != "1":
                    print("It seems like he has good promo and he has a good job... give him a bonus.")
                    print("1 for yes and 2 for no.")
                    ManagerYONBonus = input("")
                    if ManagerYONBonus == "2":
                        continue
                    elif ManagerYONBonus == "1":
                        print("'Thanks so much!'")
                        time.sleep(2)
                        print("Now let's see your money...")
                        time.sleep(5)
                        print("$499,952 dollars!")
                        time.sleep(2)
                        print("Whatever, at least... oh never mind, we have the hire and fire part.")
                        time.sleep(5)
                    else:
                        print("That is not a option!")
                        continue
                print("Ok last part is the hire and fire.The fire is actually reject but I think fire is better.")
                time.sleep(6)
                print("So here is a person who really wants to get hired is here.")
                time.sleep(3)
                print("'Hi! Can I get hired? Here's my resume.'")
                print("Name: Mike\nAge: 21\nCrimes: None\nReason (In one word): Help")
                time.sleep(3)
                print("He actually seems good. Before we hire or fire him, we need to ask him questions.")
                time.sleep(3)
                ManagerQuestions = False
                ManagerYONForQuestionsNumbers = 0
                FirstQuestion = False
                SecondQuestion = False
                ThirdQuestion = False
                while not ManagerQuestions:
                    print("1. Why do you want to work here?\n2. Are you dumb?")
                    print("3. If I was a customer and argued with you, what would you do?")
                    ThreeManagerQuestions = input("")
                    if ThreeManagerQuestions == "1":
                        if FirstQuestion:
                            print("You already asked this question!")
                            continue
                        else:
                            print("'Because I would love to help out others and make the business more recognisable.'")
                            ManagerYONForQuestionsNumbers += 1
                            time.sleep(5)
                            print("Ok pretty good, would you like to ask him another question?")
                            ManagerYONForQuestions = input("")
                            FirstQuestion = True
                            if ManagerYONForQuestions == "1":
                                if ManagerYONForQuestionsNumbers == 3:
                                    print("You already asked all the questions!")
                                    time.sleep(2)
                                    print("Ok, it's now time to HIRE OR FIRE!")
                                    ManagerQuestions = True
                                elif ManagerYONForQuestionsNumbers >= 3:
                                    print("You broke the game?! Wow. Also you still already asked all the questions!")
                                    time.sleep(2)
                                    print("Ok, it's now time to HIRE OR FIRE!")
                                    ManagerQuestions = True
                                else:
                                    continue
                            elif ManagerYONForQuestions == "2":
                                print("Ok, it's now time to HIRE OR FIRE!")
                                ManagerQuestions = True
                    elif ThreeManagerQuestions == "2":
                        if SecondQuestion:
                            print("You already asked this question!")
                            continue
                        else:
                            print("Uhh... no?")
                            ManagerYONForQuestionsNumbers += 1
                            time.sleep(2)
                            print("Mhm seems good... so, would you like to ask him another question?")
                            SecondQuestion = True
                            ManagerYONForQuestions = input("")
                            if ManagerYONForQuestions == "1":
                                if ManagerYONForQuestionsNumbers == 3:
                                    print("You already asked all the questions!")
                                    ManagerQuestions = True
                                elif ManagerYONForQuestionsNumbers >= 3:
                                    print("You broke the game?! Wow. Also you still already asked all the questions!")
                                    ManagerQuestions = True
                                else:
                                    continue
                            elif ManagerYONForQuestions == "2":
                                print("Ok, it's now time to HIRE OR FIRE!")
                                ManagerQuestions = True
                    elif ThreeManagerQuestions == "3":
                        if ThirdQuestion:
                            print("You already asked this question.")
                        else:
                            print("I would go the manager and let him take care of you.")
                            ManagerYONForQuestionsNumbers += 1
                            time.sleep(2)
                            print("Nice, nice.")
                            ThirdQuestion = True
                            ManagerYONForQuestions = input("")
                            if ManagerYONForQuestions == "1":
                                if ManagerYONForQuestionsNumbers == 3:
                                    print("You already asked all the questions!")
                                    ManagerQuestions = True
                                elif ManagerYONForQuestionsNumbers >= 3:
                                    print("You broke the game?! Wow. Also you still already asked all the questions!")
                                    ManagerQuestions = True
                                else:
                                    continue
                            elif ManagerYONForQuestions == "2":
                                print("Ok, it's now time to HIRE OR FIRE!")
                                ManagerQuestions = True
                time.sleep(3)
                LastThing = False
                while not LastThing:
                    print("Hire him!")
                    print("1. YOU'RE HIRED!\n2. YOU'RE FIRED, I meant, REJECTED!")
                    YONManagerTutorial = input("")
                    if YONManagerTutorial == "1":
                        print("'Thank you! I will try my best!'")
                        LastThing = True
                    elif YONManagerTutorial == "2":
                        continue
                    else:
                        print("That is not an option!")
                        continue
                time.sleep(2)
                print("YOU have finished the tutorial once and for ALL!")
                print("You can now play manager now or choose one of the other jobs.")
            else:
                exited = False
                print("Ok let's start!")
                ManagerMoney = 500000
                FirstQuestion = False
                SecondQuestion = False
                ThirdQuestion = False
                Karma = 50
                while not exited or ManagerMoney <= 0 or Karma == 0:
                    OneChoiceIGuess = random.choice(OneChoiceFromManager)
                    if FirstQuestion:
                        FirstQuestion = False
                    elif SecondQuestion:
                        SecondQuestion = False
                    elif ThirdQuestion:
                        ThirdQuestion = False
                    if exited:
                        exit("Exited because you said yes.")
                    elif ManagerMoney <= 0:
                        exit("Exited because you went bankrupt.")
                    if OneChoiceIGuess == "Hire and fire":
                        print("'Can I be hired? Here is my resume!'")
                        ManagerNameRandom = random.choice(ManagerName)
                        value = random.randint(1, 50)
                        CrimesRandom = random.choice(Crimes)
                        ReasonRandom = random.choice(Reason)
                        time.sleep(2)
                        print("Name: " + ManagerNameRandom)
                        print("Age: ")
                        print(value)
                        print("Crimes: " + CrimesRandom)
                        print("Reason (One word): " + ReasonRandom)
                        ManagerQuestions = False
                        ManagerYONForQuestionsNumbers = 0
                        FirstQuestion = False
                        SecondQuestion = False
                        ThirdQuestion = False
                        input("Press enter when you are ready.")
                        while not ManagerQuestions:
                            FirstQuestionThingRandom = random.choice(FirstQuestionThing)
                            SecondQuestionThingRandom = random.choice(SecondQuestionThing)
                            ThirdQuestionThingRandom = random.choice(ThirdQuestionThing)
                            print("1. Why do you want to work here?\n2. Are you dumb?")
                            print("3. If I was a customer and argued with you, what would you do?")
                            ThreeManagerQuestions = input("")
                            if ThreeManagerQuestions == "1":
                                if FirstQuestion:
                                    print("You already asked this question!")
                                    continue
                                elif not FirstQuestion:
                                    print(FirstQuestionThingRandom)
                                    ManagerYONForQuestionsNumbers += 1
                                    time.sleep(5)
                                    print("Are you going to ask him another question?")
                                    ManagerYONForQuestions = input("")
                                    FirstQuestion = True
                                    if ManagerYONForQuestions == "1":
                                        if ManagerYONForQuestionsNumbers == 3:
                                            print("You already asked all the questions!")
                                            time.sleep(2)
                                            print("Ok, it's now time to HIRE OR FIRE!")
                                            ManagerQuestions = True
                                        elif ManagerYONForQuestionsNumbers >= 3:
                                            print("You broke the game?!")
                                            print("Wow. Also you still already asked all the questions!")
                                            time.sleep(2)
                                            print("Ok, it's now time to HIRE OR FIRE!")
                                            ManagerQuestions = True
                                        else:
                                            continue
                                    elif ManagerYONForQuestions == "2":
                                        print("Ok, it's now time to HIRE OR FIRE!")
                                        ManagerQuestions = True
                            elif ThreeManagerQuestions == "2":
                                if SecondQuestion:
                                    print("You already asked this question!")
                                    continue
                                elif not SecondQuestion:
                                    print(SecondQuestionThingRandom)
                                    ManagerYONForQuestionsNumbers += 1
                                    time.sleep(2)
                                    print("So, would you like to ask him another question?")
                                    SecondQuestion = True
                                    ManagerYONForQuestions = input("")
                                    if ManagerYONForQuestions == "1":
                                        if ManagerYONForQuestionsNumbers == 3:
                                            print("You already asked all the questions!")
                                            ManagerQuestions = True
                                        elif ManagerYONForQuestionsNumbers >= 3:
                                            print("You broke the game?!")
                                            print("Wow. Also you still already asked all the questions!")
                                            ManagerQuestions = True
                                        else:
                                            continue
                                    elif ManagerYONForQuestions == "2":
                                        print("Ok, it's now time to HIRE OR FIRE!")
                                        ManagerQuestions = True
                            elif ThreeManagerQuestions == "3":
                                if ThirdQuestion:
                                    print("You already asked this question.")
                                elif not ThirdQuestion:
                                    print(ThirdQuestionThingRandom)
                                    ManagerYONForQuestionsNumbers += 1
                                    time.sleep(2)
                                    print("Would you like to ask another question?")
                                    ThirdQuestion = True
                                    ManagerYONForQuestions = input("")
                                    if ManagerYONForQuestions == "1":
                                        if ManagerYONForQuestionsNumbers == 3:
                                            print("You already asked all the questions!")
                                            ManagerQuestions = True
                                        elif ManagerYONForQuestionsNumbers >= 3:
                                            print("You broke the game?!")
                                            print("Wow. Also you still already asked all the questions!")
                                            ManagerQuestions = True
                                        else:
                                            continue
                            time.sleep(3)
                            LastThing = False
                            while not LastThing:
                                print("1. YOU'RE HIRED!\n2. YOU'RE FIRED, I meant, REJECTED!")
                                YONManagerTutorial = input("")
                                if YONManagerTutorial == "1":
                                    print("'Thank you! I will try my best!'")
                                    LastThing = True
                                elif YONManagerTutorial == "2":
                                    print("Aww come on...")
                                    LastThing = True
                                else:
                                    print("That is not an option!")
                                    continue
                    elif OneChoiceIGuess == "Bonuses":
                        ManagerNameRandom = random.choice(ManagerName)
                        value = random.randint(1, 50)
                        ManagerJobFirstRandom = random.choice(ManagerJobFirst)
                        print("'Can I get a bonus?'")
                        input("Press enter to check his status")
                        print("Name: " + ManagerNameRandom)
                        print("Promo: ")
                        print(value)
                        print("Job: " + ManagerJobFirstRandom)
                        input("Press enter when you are ready.")
                        print("Will you give him a bonus?")
                        print("1. Yes\n2. No")
                        ManagerYONBonus = input("")
                        ManagerYONThing = False
                        while not ManagerYONThing:
                            if ManagerYONBonus == "1":
                                print("'Thanks!'")
                                ManagerMoney -= value
                                Karma += 1
                                ManagerYONThing = True
                            elif ManagerYONBonus == "2":
                                print("'Aww man...'")
                                ManagerMoney += value
                                Karma -= 1
                                ManagerYONThing = True
                            else:
                                print("That isn't an option!")
                                input("")
                    else:
                        print("")
                    if ManagerMoney <= 0:
                        ManagerMoney = 0
                    print("Would you like to exit? Type in Y for yes and N for no or just press any other key.")
                    exits = input("")
                    if exits == "Y":
                        print("Exiting...")
                        exited = True
                    else:
                        continue
