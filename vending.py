def vending_machine():
    coins=0
    totcoins=0
    finshed= False
    allowedcoins=[1,2,5,10,50,100,1000]
    while finshed==False:
        try:
            coins=int(input("PLease enter coins that you would like the machine to process\n"))
            while coins not in allowedcoins:
                print("sorry this is not allowed\n")
                print("you are only allowed to add 1,2,5,10,50,100,1000 paise coins\n")
                coins=int(input("PLease enter coins that you would like the machine to process\n"))
            done=input("are you done?")
            if done in ['Y','Yes']:
                finshed=True
            totcoins= coins+totcoins
        except ValueError:
            print("You are trying to enter invalid coins")
            print("you are only allowed to add 1,2,5,10,50,100,1000 paise coins\n")
            coins=int(input("PLease enter coins that you would like the machine to process\n"))
            while coins not in allowedcoins:
                print("sorry this is not allowed\n")
                print("you are only allowed to add 1,2,5,10,50,100,1000 paise coins\n")
                coins=int(input("PLease enter coins that you would like the machine to process\n"))
            done=input("are you done?")
            if done in ['Y','Yes']:
                finshed=True    
            totcoins= coins+totcoins
        if coins==0:
            finshed== True

    print("Your inpout has been added to your total You have %d",totcoins)
    print("What would you like to purchase today?")
    print("1 $50\n")
    print("2 $40\n")
    print("3 $45\n")
    print("4 $55\n")
    print("5 $70\n")
    print("6 $54\n")
    print("7 $34\n")
    print("8 $50\n")
    stop=False
    while stop==False:
        choice=int(input("PLease enter your choice\n"))
        if choice==1:
            totcoins-50
            print("dispensing item 1 which costs $50\n")
            more=input("are you done?")
            if more in ['Y','Yes']:
                stop=True
        elif choice==2:
            totcoins-40
            print("dispensing item 2 which costs $50\n")
            more=input("are you done?")
            if more in ['Y','Yes']:
                stop=True
        elif choice==3:
            totcoins-45
            print("dispensing item 3 which costs $50\n")
            more=input("are you done?")
            if more in ['Y','Yes']:
                stop=True
        elif choice==4:
            totcoins-55
            print("dispensing item 4 which costs $50\n")
            more=input("are you done?")
            if more in ['Y','Yes']:
                stop=True
        elif choice==5:
            totcoins-70
            print("dispensing item 5 which costs $50\n")
            more=input("are you done?")
            if more in ['Y','Yes']:
                stop=True
        elif choice==6:
            totcoins-34
            print("dispensing item 6 which costs $50\n")
            more=input("are you done?")
            if more in ['Y','Yes']:
                stop=True
        elif choice==7:
            totcoins-54
            print("dispensing item 7 which costs $50\n")
            more=input("are you done?")
            if more in ['Y','Yes']:
                stop=True
        elif choice==8:
            totcoins-50
            print("dispensing item 8 which costs $50\n")
            more=input("are you done?")
            if more in ['Y','Yes']:
                stop=True
        else:
            print("please enter a suitable option\n")
    print("Thank you")

vending_machine()  
