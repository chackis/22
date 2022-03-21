import time
from colorama import Fore, Back, Style
import sys
import pickle
class Cats:
    def __init__(self, name, age, weight, happy):
        self.name = name
        self.age = age
        self.weight = weight
        self.happy = happy
    def info(self):
        print("Name of the cat: " + self.name + " Age: " + str(self.age) + " Weight: " + str(self.weight) + "Is he happy? " + str(self.happy))
        input()

    def pet(self):
        print("Do you want to pet the cat? (y/n)")
        yn = input()
        if yn == "y":
            print("You are petting the cat..")
            time.sleep(1)
            print("You have pet the cat! He is happy now.")
            self.happy = True
            return Cats
        else:
            print("You didn't want to pet the cat.. He is sad now.")
            self.happy = False
            return Cats
    def walk(self):
        print("Do you want to go out with your cat? (y/n)")
        yn1 = input()
        if yn1 == "y":
            if self.happy == True:
                print("You are walking with your cat..")
                time.sleep(5)
                print("You came back home, your cat is happy.")
                return Cats
            else:
                print("Your cat is sad! Pet him, and he will be happy!")
                return Cats
        else:
            print("You didn't want to walk with your cat..")
            print("He's sad now.")
            self.happy = False
            return Cats
    def play(self):
        print("Do you want to play with the cat? (y/n)")
        chss = input()
        if chss == "y":
            print("You took his favorite toy..")
            time.sleep(1)
            print("Do you want to throw it far away, or throw it right next to you?(far away/next to me)")
            chss1 = input()
            if chss1 == "far away":
                print("You grab all of your powers to throw it as far, as you can!")
                time.sleep(2)
                print("h..HERE IT GOES!!")
                time.sleep(2)
                print(Fore.BLACK + "        BHAAA!")
                time.sleep(3)
                print(Fore.YELLOW + "Cat: Meow!")
                time.sleep(0)
                print("Oh, he took it to me..")
            if chss1 == "next to me":
                print("You threw it to the wall behind you!")
                time.sleep(2)
                print("Cat understood your love to him, so he is sad now..")
                self.happy = False
        if chss == "n":
            print("Cat.." + Fore.RED + "NOW HATES YOU.")
            time.sleep(2)
            print(Fore.YELLOW + "Cat: Meow..")

    def secret():
        time.sleep(2)
        print(Fore.LIGHTRED_EX + "wh..What.. WHAT ARE YOU DOING HERE?!")
        time.sleep(1)
        print(Fore.YELLOW + "1. I was just discovering the game..")
        print("2. I will sure leave now..")
        sec = int(input())
        if sec == 1:
            print(Fore.LIGHTRED_EX + "LEAVE! LEAVE THIS PLACE! EVERYONE WHO IS SO DUMB LIKE YOU..")
            time.sleep(2.50)
            print(Fore.BLACK + "IS TRAPPED IN THIS HELLHOLE.")
            time.sleep(2)
            print(Fore.YELLOW + "Why are you screaming? What is this place? Just lets get out of here, i'm scared..")
            time.sleep(3)
            print(Fore.LIGHTRED_EX + "*silent laughing*")
            time.sleep(1.50)
            print("Try to.")
            time.sleep(2)
            print(Fore.YELLOW + "Heh, I'll sure do!")
            time.sleep(1)
            print(Fore.WHITE + "You try to get back in the menu..")
            time.sleep(2)
            print("But there's no door.")
            time.sleep(0.50)
            print(Fore.YELLOW + "WHAT? THERE WAS A DOOR HERE!")
            time.sleep(3)
            print(Fore.LIGHTRED_EX + "Not anymore.")
            time.sleep(1)
            print(Fore.BLUE + "JONHY, ARE YOU READY FOR YOUR DAILY THERAPY?")
            time.sleep(1.50)
            print(Fore.LIGHTRED_EX + "This is what I told you. Now, we'll suffer together.")
            time.sleep(2)
            print(Fore.YELLOW + "NO! I WILL FIGHT!")
            time.sleep(1.50)
            print(Fore.BLUE + "JONHY! WHERE ARE YOU?")
            time.sleep(2)
            print(Fore.BLUE + "Oh! We have guests..")
            time.sleep(1.50)
            print("I remember you. Well, this looks scary, you know.")
            time.sleep(1.50)
            print("But.. be sure, i will take care of you.")
            time.sleep(1)
            print(Fore.WHITE + "The cat is comming towards you.")
            time.sleep(2)
            print(Fore.YELLOW + "STAY BACK!")
            time.sleep(1)
            print(Fore.BLUE + "WHY ARE YOU SCREAMING?! DIDN'T I SAY THAT I'LL TAKE CARE OF YOU?")
            time.sleep(1)
            print(Fore.YELLOW + "no..NO, NO!")
            time.sleep(3)
            print(Fore.WHITE + "You fell on the floor. Is this.. The end?")
        if sec == 2:
            print(Fore.WHITE + "You just left..")
            print("...")
            data1 = "How could you?"
            file1 = open("how.txt", "wb")
            pickle.dump(data1, file1)
            file1.close()




jeffrey = Cats("Jeffrey the second", 4, 4.5, None)
ranger = Cats("Ranger", 3, 3.4, None)
print(Fore.YELLOW + "Welcome to the cat game! You have 2 cats: Jeffrey and Ranger. What do you want to do?")
time.sleep(0.10)
print("Here's a list of things that you want to do:")
time.sleep(0.10)
print("1. Pet the cat (ex. pet jeffrey)")
print("2. Walk out with him (ex. walk jeffrey)")
print("3. See his information (info jeffrey)")
print("4. Play with him (play jeffrey)")
print("5. Play with you. (secret)")
time.sleep(1)
print("What do you want to do?")
chs = input()
if chs == "pet jeffrey":
    jeffrey.pet()
if chs == "pet ranger":
    ranger.pet()
if chs == "walk jeffrey":
    jeffrey.walk()
if chs == "walk ranger":
    ranger.walk()
if chs == "info jeffrey":
    jeffrey.info()
if chs == "info ranger":
    ranger.info()
if chs == "play jeffrey":
    jeffrey.play()
if chs == "play ranger":
    ranger.play()
if chs == "secret":
    Cats.secret()











