# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random 
class Game(): 
  user_name ='' 
  category ='' 
  animals = '' 
 
  def __init__(self,user_name): 
    print (f" Welcome { user_name} ! Lets begin the game.") 
    self.user_name = user_name 
    self.initialize_dicts() 
    self.play() 
   
  def initialize_dicts(self): 
    self.animals = {'parrot': "I am a bird; I am green in color and have reddish beak",  'peacock': "I am a bird. I am colorful and known as the national bird of India",  'hen': "I am a domesƟc bird and give you eggs for omelette", 'crocodile': "I am a reptile; I am brownish green in colour, big in size and live in water.", 'snake': "I am a repƟle. I make a hiss sound and can move without any legs", 'lizard': "I am a repƟle; I live in most houses and I can easily crawl on the walls", 'bee': "I am an insect and I help with pollinaƟon and collect honey",'mosquito': "I am an insect and I drink blood and spread disease",'butterfly': "I am an insect and I have beauƟful wings and I love nectar"} 
 
  def play(self): 
    print("Guess who I am from the below hints") 
    randomanimal = random.choice(list(self.animals.keys()))
    hints = self.animals.get(randomanimal) 
    print (hints) 
    print ( "your guess : ") 
    guess = input().lower()
    #get input from user here 
    #convert guess to all lowercase and remove any whitespaces from the beginning or end. 
    if guess == randomanimal: 
      print("You are right!") 
    else: 
      print("Wrong guess!") 
    play_again=input("Would you like to continue the game (Y/N) ?")
    if play_again == 'y':# get user input and if "Y" 
        self.play() 
    else:
        print("thank you")
if __name__ == "__main__": 
  user_name = input(" Welcome to animal guessing game. Please enter your name: ") 
  
  #get user name and store it in the variable user_name. IT will be passed to the constructor of Game class 
  game = Game(user_name); 
   
   
 
 
 
 
 
 
 
 
 
 
 
 
 
