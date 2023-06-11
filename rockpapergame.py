import random , sys
win=0
losses=0
tie=0
computermovelist=["r","s","p"]
while True:
     print(f"wins {win} loss {losses} ties {tie}")
     while True:
      print('Enter your move rock(r) paper(p) scissors or quit(q)')
      playermove=input() 
      if playermove == 'q':
            sys.exit()
      if playermove == 'r' or playermove == 'p'or playermove == 's' :
         break
     print('type only r,p s, or q')
        #displaying the player moves 
     if playermove=='r':
       print("rock versus ",end='')
     elif playermove=='p':
       print("paper versus ",end='')
     elif playermove=='s':
        print("scissors versus ",end='')
        #displaying the computer choice
     computermove = random.choice(computermovelist) 
     if computermove == 'r':
        print("rock")
     elif computermove == 'p':
       print("paper")
     elif computermove == 's':
      print("scissors")
     #compareing both inputs and deciding the points 
     if computermove == playermove:
         print("its a tie ")
         tie=+1
     elif playermove == 'r' and computermove=='s':
         print("you win")
         win=+1
     elif playermove == 'r' and computermove=='p':
         print("YOU LOSE ")
         losses=+1
     elif playermove == 'p' and computermove=='r':
         print("you win ")
         win=+1
     elif playermove == 'p' and computermove=='s':
         print("you lose")
         losses=+1
     elif playermove == 's' and computermove=='p':
         print("you win")
         win=+1
     elif playermove == 's' and computermove=='r':
         print("you lose")
         losses=+1