'''

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MdddddddddddddddddddddddddddNMMh++++++++++++++++++yMMm+++++hMMMMMMMs++++oMMd++++++++++++++++++yMMy++++++++++++++++++dM
MhssssssssssssssssssssssssssmMMo                  /MMd     oMMMMMMM:    .MMh                  /MM+                  sM
MhssssssssssymmmmmdsssssssssmMMo                  /MMd     oMMMMMMM:    .MMh                  /MM+                  sM
MhsssssssssssmMMMMhsssssssssmMMo     yddddddd     /MMd     oMMMMMMM:    .MMh     oddddddddddddmMMmdddddd`    -ddddddmM
MhssssssssssshNNNmysssssssssmMMo     mMMMMMMN     /MMd     oMMMMMMM:    .MMh     yMMMMMMMMMMMMMMMMMMMMMM.    :MMMMMMMM
MhsssssssssssymmmdssssssssssmMMo     mMMMMMMN     /MMd     oMMMMMMM:    .MMh     -////////////sMMMMMMMMM.    :MMMMMMMM
MhssymmddhyhhyyhyyssssssssssmMMo     mMMMMMMN     /MMd     oMMMMMMM:    .MMh                  /MMMMMMMMM.    :MMMMMMMM
MhssyMMMMMhMmsdNhyhyssssssssmMMo     ````````     /MMd     oMMMMMMM:    .MMh                  /MMMMMMMMM.    :MMMMMMMM
MhssyMNNmmyddssymNmddyssssssmMMo                  /MMd     oMMMMMMM:    .MMNmmmmmmmmmmmmm     /MMMMMMMMM.    :MMMMMMMM
MhssyysssssssssyhhNMMMNdysssmMMo     .-`     .----oMMd     oMMMMMMM:    .MMMMMMMMMMMMMMMN`    /MMMMMMMMM.    :MMMMMMMM
MhsssssssssssssssydMMMNhysssmMMo     mMo     hmmmmNMMd     ommmmmmm-    .MMNmmmmmmmmmmmmm     /MMMMMMMMM.    :MMMMMMMM
MhssssssssssssssssshNhysssssmMMo     mMo          +MMd                  .MMd                  /MMMMMMMMM.    :MMMMMMMM
MhssssssssssssssssssssssssssmMMo     mMo          +MMd                  .MMd                  /MMMMMMMMM.    :MMMMMMMM
MMdhhhhhhhhhhhhhhhhhhhhhhhhhhNMMy/////mMy//////////yMMm///////////////////MMm//////////////////sMMMMMMMMM+////oMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM  RAID CALCULATOR  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
'''
#Rust Calculator
''' Using Functions for looping multiple Menus and different applications within the calculator'''

#Calculator function from 1. of menu
import time
import sys




    
def Mat_Calculator():
    print("[.................]")
    print("[1.Satchel Charges]")
    print("[2.Explosive ammo ]")
    print("[3.C4             ]")
    print("[4.Rockets        ]")
    print("[.................]")
    calc_dec1 = int(input(" "))
    
    if calc_dec1 >4:
        print("Number entered was not recognised, please enter 1-4")
        Mat_Calculator()
    if calc_dec1 <1:
        print("Number entered was not recognised, please enter 1-4")
        Mat_Calculator()
    
    if calc_dec1 == 1:
        print("\n\n[.................]")    
        scharge_amount = int(input("how many satchel\n charges do you \n need to make? \n[.................]\n"))
        print("[.................]") 
        print("you will need:\n","Satchel Charges;\n",4*scharge_amount,"Beancan grenades\n",1*scharge_amount,"Small stash/es\n",1*scharge_amount,"Rope","\n\n","Beancan Grenades;\n",240*scharge_amount,"Gunpowder\n",80*scharge_amount,"metal fragments\n\n","Small Stash;\n","cloth\n",10*scharge_amount,"\n\n","Gunpowder;\n",480*scharge_amount,"sulfer\n",270*scharge_amount,"charcoal")
        Menu()
    
    if calc_dec1 == 2:
        print("\n\n[.................]")
        Eammo_amount = int(input("how much explosive \nammo do you\nneed to make?\n[.................]\n"))
        print("[.................]")
        print("you will need:\n","Explosive Ammo;\n",20*Eammo_amount,"Gunpowder\n",10*Eammo_amount,"Metal fragments\n",10*Eammo_amount,"Sulfer\n"+"Gunpowder;"+"\n\n",60*Eammo_amount,"charcoal\n",40*Eammo_amount,"Sulfer")
        Menu()
    
    if calc_dec1 == 3:
        print("\n\n[.................]")
        C4_amount = int(input("how much C4\ndo u want\nto make?\n[.................]\n"))
        print("[.................]")
        print("you will need:\n", "C4;\n" ,20*C4_amount, "Explosives\n", 5*C4_amount, "Cloth\n", 2*C4_amount,"Tech trash\n\n", "Explosives;\n" ,1000*C4_amount ,"Gunpowder\n" ,60*C4_amount,"Low grade\n" ,200*C4_amount ,"Sulfer\n" ,200*C4_amount ,"Metal fragments\n\n","Gun Powder;\n" ,2000*C4_amount ,"Sulfer\n" ,3000*C4_amount ,"charcoal")
        Menu()
    
    if calc_dec1 == 4:
        print("\n\n[.................]")
        Roc_amount = int(input("how many Rockets\n do you\n want to make\n[.................]\n"))
        print("[.................]")
        print("you will need:\n" ,"Rockets;\n" , 10*Roc_amount ,"Explosives\n" ,150*Roc_amount ,"Gunpowder\n" ,2*Roc_amount ,"Pipes\n\n" ,"Explosves;\n" ,500*Roc_amount ,"Gun Powder\n" , 100*Roc_amount ,"Sulfer\n" ,100*Roc_amount ,"Metal fragments\n" ,30*Roc_amount ,"Low grade\n\n" ,"Gun Powder;\n" ,1000*Roc_amount ,"Sulfer\n" ,1500*Roc_amount ,"Charcoal")
        Menu()
    
    
        
def Amount_Calculator():
    print("Coming soon...")
    time.sleep(1)
    Menu()
    x = 0 
    counter = 0
    Health_Points = 0
    while x ==0:
        counter = counter + 1
        print("[........................]")
        print("[-  Obstruction type",counter," -]")
        print("[1. Wall/Floor/Foundation]")
        print("[2. Doors                ]")
        print("[3. Other                ]")
        print("[........................]")
        Am_calc_dec1 = int(input(" "))
        if Am_calc_dec1 == 1:
            print("[...........]")
            print("[1. Wood    ]")
            print("[2. Stone   ]")
            print("[3. Metal   ]")
            print("[4. HQ Metal]")
            print("[...........]")
            Am_calc_dec2 = int(input(" "))
            if Am_calc_dec2 == 1:
                Health_Points = Health_Points + 250
            if Am_calc_dec2 == 2:
                Health_Points = Health_Points + 500
            if Am_calc_dec2 == 3:
                Health_Points = Health_Points + 1000
            if Am_calc_dec2 == 4:
                Health_Points = Health_Points + 2000
            else:
                print("Incorrect Value please try again")
            print("Damage required to do:",Health_Points,"HP")
            Am_calc_dec3 = input("Are there more obsticles? [y/n]\n")
            if Am_calc_dec3 == "n":
                Menu()
            if Am_calc_dec3 != "n" or "y":
                print("Incorrect Value please try again")
        
        if Am_calc_dec1 ==2:
            print("[...................]")
            print("[1. Sheet Metal Door]")
            print("[2. Armoured Door   ]")
            print("[3. Garage Door     ]")
            print("[...................]")
            Am_calc_dec4 = int(input(" "))
            if Am_calc_dec4 == 1:
                Health_Points = Health_Points + 250
            if Am_calc_dec4 == 2:
                Health_Points = Health_Points + 800
            if Am_calc_dec4 == 3:
                Health_Points = Health_Points + 600
            if Am_calc_dec4 == 4:
                Health_Points = Health_Points + 250
            print("Damage required to do:",Health_Points,"HP")
            Am_calc_dec3 = input("Are there more obsticles? [y/n]\n")
            if Am_calc_dec3 == "n":
                Menu()
        
        if Am_calc_dec1 ==3:
            Health_Points_add = int(input("[-Enter the amount of hp this item has-]\n"))
            Health_Points = Health_Points + Health_Points_add
            print("Damage required to do:",Health_Points,"HP")
            Am_calc_dec3 = input("Are there more obsticles? [y/n]\n")
            if Am_calc_dec3 == "n":
                Menu()
        else:
            counter = counter - 1
            print("Incorrect value please try again")

'''def HP_to_explosive_calc():
    print("[...................]")
    print("[ - Exlosive Type - ]")
    print("[1. Satchel Charge  ]")
    print("[2. Explosive ammo  ]")
    print("[3. C4              ]")
    print("[4. Rockets         ]")
    print("[...................]")
    HP_to_explosive_calc_Dec1 = int(input(""))
    if HP_to_explosive_calc_Dec1 = 1:'''
        

        
            
            
            
            

            
            
            
            
    #calculating        
                
            

def Close():
    print("Goodbye",end="")
    print(".",end="")
    time.sleep(0.5)
    print(".",end="")
    time.sleep(0.5)
    print(".")
    time.sleep(1)
    sys.exit()


        
        


#Menu function

def Menu():
    print("[......RUST RAID CALCULATOR......]")
    print("[1. Explosive Material Calculator]")
    print("[2. Explosives Needed Calculator ]")
    print("[3. Close                        ]")
    print("[................................]")
    menu_dec1 = input(" ")
    if menu_dec1 == "1":
        Mat_Calculator()
    if menu_dec1 == "2":
        print("Coming Soon...")
        time.sleep(0.5)
        Menu()
    if menu_dec1 == "3":
        Close()
    else:
        print("Incorrect input, Please enter 1-3")
        Menu()

Menu()

