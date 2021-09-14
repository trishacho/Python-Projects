import random
import sys

class DigiPoke():
    def __init__(self, name, type, health, record):
        self.name = name
        self.type = type
        self.health = 100
        self.record = 0
        
    def getHealth(self):
        return self.health
    
    def getRecord(self):
        return self.record

    def getName(self):
        return self.name
        
    def fight(self):
        win = random.randint(0, 1)
        if(win == 1):
            self.health = self.health - 10
            self.record = self.record + 1
        else:
            self.health = self.health - 25
    
    def heal(self):
        if(self.health != 100):
            self.health = self.health + 10
            self.record = self.record - 0.5
        else:
            print(self.name, "is already at full health!")

    def evolve(self):
        if(self.record >= 5):
            print("Please select a name for your evolved DigiPoke.")
            newName = input()
            newDigiPoke = Evolve(newName, self.type, 50, 1, 'Earth')
            print(self.name, "has evolved to", newDigiPoke.name)
        return newDigiPoke
    
    def status(self):
        print(self.name, "of type", self.type, "has health", self.health, "and a record of", self.record)

    def menu(self):
        print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Evolve")
        option = int(input())
        while(option != 5):
            if(option == 1):
                self.fight()
                self.status()
                if(self.getHealth() <= 0):
                    print(self.getName(), "has no health. You lose.")
                    sys.exit()
                print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Evolve")
                option = int(input())
            elif(option == 2):
                self.heal()
                self.status()
                print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Evolve")
                option = int(input())
            elif(option == 3):
                self.status()
                print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Evolve")
                option = int(input())
            elif(option == 4):
                if(self.getRecord() >= 5):
                    evolveDigiPoke = self.evolve()
                    evolveDigiPoke.menu()
                else:
                    print(self.name, "has not won 5 battles yet.")
                    self.status()
                    print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Evolve")
                    option = int(input())

class Evolve(DigiPoke):
    def __init__(self, name, type, health, record, type2):
        super().__init__(name, type, health, record)
        if(type == 'Earth'):
            types = ('Fire', 'Air', 'Water')
            type2 = random.choice(types)
            self.type2 = type2
        elif(type == 'Fire'):
            types = ('Earth', 'Air', 'Water')
            type2 = random.choice(types)
            self.type2 = type2
        elif(type == 'Air'):
            types = ('Earth', 'Fire', 'Water')
            type2 = random.choice(types)
            self.type2 = type2
        else:
            types = ('Earth', 'Fire', 'Air')
            type2 = random.choice(types)
            self.type2 = type2

    def retire(self):
        print(self.name, "has retired.")

    def status(self):
        print(self.name, "of type", self.type, "and", self.type2, "has health", self.health, "and a record of", self.record)

    def menu(self):
         self.status()
         print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Retire")
         option = int(input())
         while(option != 5):
            if(option == 1):
                self.fight()
                self.status()
                if(self.getHealth() <= 0):
                    print(self.getName(), "has no health. You lose.")
                    sys.exit()
                print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Retire")
                option = int(input())
            elif(option == 2):
                self.heal()
                self.status()
                print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Retire")
                option = int(input())
            elif(option == 3):
                self.status()
                print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Retire")
                option = int(input())
            elif(option == 4):
                if(self.getRecord() >= 5):
                    self.retire()
                    sys.exit()
                else:
                    print(self.getName(), "has not won 5 battles yet.")
                    self.status()
                    print("Menu: 1 = Fight, 2 = Heal, 3 = Status, 4 = Retire")
                    option = int(input())
        

print("Please enter name and type.")
n = input()
t = input()
userDigiPoke = DigiPoke(n, t, 100, 0)
userDigiPoke.status()
userDigiPoke.menu()

