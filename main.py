print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Hunt!!")

direction = input("You are at a cross road where do you go left or right? ").lower()

if direction == "left":
    action = input("You find a small river what do you do? wait or swim ?").lower()
    if action == "wait":
        print("You come across three doors 1) red 2) blue and 3) Yello which one will you choose")
        door = input(" 1, 2, or 3: ")
        if door == "3":
            print("You win!!")
            print("You found the treasure!")
            print(''' 
            
            ''')
        elif door == "1":
            print("Game over!!")
            print("A big fire burned you alive")
            print('''
                (  .      )
            )           (              )
                    .  '   .   '  .  '  .
            (    , )       (.   )  (   ',    )
            .' ) ( . )    ,  ( ,     )   ( .
        ). , ( .   (  ) ( , ')  .' (  ,    )
        (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
        elif door == "2":
            print("GAME OVER!")
            print("You are killed by witches making potions")
            print('''
                        
               _..--.._       _..--.      _..--..
             ,'      ,'`.   ,','.--.\   ,' \   `.`.
            /  /    /  /|  : : /  _ \:  |\  \    \ \
           /  :    :  /`.  | |:| ,'' _``. \
         | ,;,   .  `:\ _:   | `,/_\.   :`/;'  ,   .:\ )
         `'/'   _ \   \:\(  _|__`>_/`' /(:/   /     .\` 
          /:  .'  ,`.._|_\\'  ( _=`;._//_|_..'`      \\
          :: /   '|    (__=`, :`||| `,.__)     \      :
          | \           \`.\\__\;|| //`|/       :     |
          |  `.._____.-,`'| \\___||// /`-._           |
          :         | : ,<''_\\,.|//_`>.  :`._       ;:
          \         ; ; )`-..______..-'(  :\  `-.__.' /
          ;        / /|:                : | `.._____.':
         :      _.' / ||                | |   `.       :
         :  _.-'   /  ::                ; :     `-.____;
          \;     ,'   ( \              /  )\          /
         ,'    ,'____,' ,`-,.______..-') (__\        _`.
        (___..'>_>____`.`.'._)_\_>._)-' ,'___`._________) SSt

            ''')

    else:
        print("Game Over!")
        print("You got killed by sharks")
        print('''
        

                     ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\
        ''')
else:
    print("Game over!!")
    print("A head or elephants chase and kill you")
    print('''
          _.-- ,.--.
             .'   .'    /
             | @       |'..--------._
            /      \._/              '.
           /  .-.-                     \
          (  /    \                     \
           \\      '.                  | #
            \\       \   -.           /
             :\       |    )._____.'   \
              "       |   /  \  |  \    )
                      |   |./'  :__ \.-'
                      '--' ''')  