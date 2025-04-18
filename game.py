rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#importaciónd de la libreria random
import random

#Se genera una lista con las elecciones que en el juego de piedra, papel o tijera
z = ['rock', 'paper', 'scissors']
#Creación del menú de entrada de elección del jugador 
x = int(input(" 1. rock\n 2. paper\n 3. scissors\n "))
x2 = ''
if x > 3:
  x = 3
  print("input a correct value")
else:
  x2 = z[x-1]
#Generación de resultado aleatorio por parte de la máquina
  y = random.choice(z)
  
  if y == x2:
    
    if x2 == 'rock':
      print(f"Draws\n{rock}\nrock\n{x2}\nrock")
    elif x2 == 'paper':
      print(f"Draws\n{paper}\npaper\n{paper}\npaper")
    else:
      print(f"Draws\n{scissors}\nscissors\n{scissors}\nscissors")
  elif x2 == 'rock':
    if y == 'scissors':
      print(f"{rock}\nrock\n{scissors}\n scissors\n You Win!!")
    else:
      print(f"{rock}\nrock\n{paper}\n paper\nYou Loose!!")
  elif x2 == 'paper':
    if y == 'rock':
      print(f"{paper}\npaper\n{rock}\nrock\nYou Win!!")
    else:
      print(f"{paper}\npaper\n{scissors}\nscissors\nYou Loose!!")
  elif x2 == 'scissors':
    if y == 'rock':
      print(f"{scissors}\nscissors\n{rock}\n rock\nYou Loose!!")
    else:
      print(f"{scissors}\nscissors\n{paper}\n paper\nYou Win!!")
  else:
    print("You type invalid option")
