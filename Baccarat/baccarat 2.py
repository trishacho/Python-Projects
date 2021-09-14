import cards, games
import sys

class bCard(cards.Card):
    @property
    def value(self):
        v = bCard.RANKS.index(self.rank) + 1
        if v > 10:
            v = 0
        return v

class bDeck(cards.Deck):
    def populate(self):
        for suit in bCard.SUITS: 
            for rank in bCard.RANKS: 
                self.cards.append(bCard(rank, suit))

class bHand(cards.Hand):
    def __init__(self, name):
        super(bHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(bHand, self).__str__()  
        rep += "(" + str(self.sum) + ")"        
        return rep
    
    @property     
    def sum(self):
        sum = 0
        for card in self.cards:
            sum = sum + card.value
        return sum
        
    def getThirdCard(self):
        thirdCard = 0
        if(len(self.cards) == 3):
            thirdCard = self.cards[2].value
        return thirdCard 
        
    def checkSameSuit(self):
        if(self.cards[0].suit == self.cards[1].suit):
            return True
        else:
            return False
        
class Bettor():
    def __init__(self, name, bet, betType, totalMoney, sameSuits, pandaEight):
      self.name = name
      self.bet = 0
      self.betType = ""
      self.totalMoney = 100
      self.sameSuits = False
      self.pandaEight = False
    @property
    def getBetType(self):
        return self.betType
    
    def setBetType(self, betType):
        self.betType = betType
        
    def getTotalMoney(self):
        return self.totalMoney
        
    def setTotalMoney(self, totalMoney):
        self.totalMoney = totalMoney
        
    def setBet(self, bet):
        self.bet = bet
        
    def getBet(self):
        return self.bet
    
    def getName(self):
        return self.name
        
    def setSameSuits(self, sameSuits):
        self.sameSuits = sameSuits
    
    def getSameSuits(self):
        return self.sameSuits
        
    def setPandaEight(self, pandaEight):
        self.pandaEight = pandaEight
        
    def getPandaEight(self):
        return self.pandaEight

def same_Suits(sameSuitBet, bet, player, banker):
    if(sameSuitBet == "Player"):
        if(player.checkSameSuit() == True):
            if(banker.checkSameSuit() == True):
                return bet*250
            else:
                return bet*25
        else:
            return 0
    elif(sameSuitBet == "Banker"):
        if(banker.checkSameSuit() == True):
            if(player.checkSameSuit() == True):
                return bet*250
            else:
                return bet*25
        else:
            return 0
            
def panda_Eight(bet, thirdCard, value):
    if(thirdCard == True):
        if(value == 8):
            return bet*25
        else:
            return 0
    else:
        return 0
                
class Round(object):
    def __init__(self, names):      
        self.player = bHand("Player")
        self.deck = bDeck()
        self.banker = bHand("Banker")
        self.deck.populate()
        self.deck.shuffle()
        self.names = names
        self.bettors = []
        for n in names:
            self.bettors.append(Bettor(n, 0, "", 100, False, False))
        
    def game(self):
        self.deck.deal([self.player] + [self.banker], per_hand = 2)
        for b in self.bettors:
            if(b.getTotalMoney() == 0):
                print(b.getName(), "does not have any money to bet.", b.getName(), "loses.")
                #self.bettors.remove(b)
                #if(len(self.bettors) == 0):
                sys.exit()
                    
            betOnWho = input(b.getName() + ", who would you like to bet on (Player, Banker, or Tie)? ")
            b.setBetType(betOnWho)
            bet = input(b.getName() +", how much money would you like to bet? ")
            bet = int(bet)
            b.setBet(bet)
            #playerTotalMoney = 100
            sameSuitTotalMoney = b.getTotalMoney() - bet
            pandaEightTotalMoney = sameSuitTotalMoney
            while(bet < 10 or bet > b.getTotalMoney()):
                if(bet < 10):
                    print("You need to bet $10 or more. Please bet again.")
                    bet = int(input())
                    b.setBet(bet)
                if(bet > b.getTotalMoney()):
                    print("You only have $", b.getTotalMoney(), ", please bet again.")
                    bet = int(input())
                    b.setBet(bet)
                        
            print("Would you like to place a Same Suit side bet? The Same Suit side bet can be placed based on the first two cards received by the Player or the Banker. If the one you place a bet on has the same suit, you’ll win 25:1. If the player and Banker BOTH have same EXACT suit, you'll win 250:1. (Y/N)")
            sameSuitAns = input()
            sameSuitMoney = 0
            sameSuitBet = ""
            if(sameSuitAns == "Y" or sameSuitAns == "y"):
                if(sameSuitTotalMoney < 10):
                    print("You don't have any more money to bet!")
                else:
                    b.setSameSuits(True)
                    print("Would you like to place a bet on the Player or Banker?")
                    sameSuitBet = input()
                    sameSuitMoney = input(b.getName() +", how much money would you like to bet? ")
                    sameSuitMoney = int(sameSuitMoney)
                    while(sameSuitMoney < 10 or sameSuitMoney > sameSuitTotalMoney):
                        if(sameSuitMoney < 10):
                            print("You need to bet $10 or more. Please bet again.")
                            sameSuitMoney = int(input())
                        if(sameSuitMoney > sameSuitTotalMoney):
                            print("You only have $", sameSuitTotalMoney, ", please bet again.")
                            sameSuitMoney = int(input())
                    pandaEightTotalMoney = sameSuitTotalMoney - sameSuitMoney
                
            print("Would you like to place a Panda Eight side bet? You will win 25:1 if the Player wins with a three-card hand worth eight. (Y/N)")
            pandaEightAns = input()
            pandaEightMoney = 0
            if(pandaEightAns == "Y" or pandaEightAns == "y"):
                if(pandaEightTotalMoney < 10):
                    print("You don't have any more money to bet!")
                else:
                    b.setPandaEight(True)
                    pandaEightMoney = input(b.getName() + ", how much money would you like to bet? ")
                    pandaEightMoney = int(pandaEightMoney)
                    while(pandaEightMoney < 10 or pandaEightMoney > pandaEightTotalMoney):
                        if(pandaEightMoney < 10):
                            print("You need to bet $10 or more. Please bet again.")
                            pandaEightMoney = int(input())
                        if(pandaEightMoney > pandaEightTotalMoney):
                            print("You only have $", pandaEightTotalMoney, ", please bet again.")
                            pandaEightMoney = int(input())
    
        winner = ""
        thirdCard = False
        #print(self.player)
        #print(self.banker)
        bankerVal = (self.banker.sum)%10
        playerVal = (self.player.sum)%10
        #print("Player Value: ", playerVal)
        #print("Banker Value: ", bankerVal)
            
        if(playerVal == 8 or playerVal == 9 or bankerVal == 8 or bankerVal == 9):
            if((playerVal == 8 or playerVal == 9) and (bankerVal == 8 or bankerVal == 9)):
                winner = ""
            elif(bankerVal == 8 or bankerVal == 9):
                winner = "Banker"
            elif(playerVal == 8 or playerVal == 9):
                winner = "Player"
                    
        #elif(playerVal == 6 or playerVal == 7 or playerVal == 8 or playerVal == 9):
            #continue
        elif(playerVal == 0 or playerVal == 1 or playerVal == 2 or playerVal == 3 or playerVal == 4 or playerVal == 5):
            self.deck.deal([self.player])
            #print(self.player)
            playerVal = (self.player.sum)%10
            #print("Player Value: ", playerVal)
            thirdCard = True
        
        if(thirdCard == False):
            #if(bankerVal == 6 or bankerVal == 7 or bankerVal == 8 or bankerVal == 9):
                #continue
            if(bankerVal == 0 or bankerVal == 1 or bankerVal == 2 or bankerVal == 3 or bankerVal == 4 or bankerVal == 5):
                self.deck.deal([self.banker])
                #print(self.banker)
                bankerVal = (self.banker.sum)%10
                #print("Banker Value: ", bankerVal)
        else:
            #if(bankerVal == 7 or bankerVal == 8 or bankerVal == 9):
                #continue
            if(bankerVal == 0 or bankerVal == 1 or bankerVal == 2):
                self.deck.deal([self.banker])
                #print(self.banker)
                bankerVal = (self.banker.sum)%10
                #print("Banker Value: ", bankerVal)
            elif(bankerVal == 3):
                #if(self.player.getThirdCard() == 8):
                    #continue
                #else:
                if(self.player.getThirdCard() != 8):
                    self.deck.deal([self.banker])
                    #print(self.banker)
                    bankerVal = (self.banker.sum)%10
                    #print("Banker Value: ", bankerVal)
            elif(bankerVal == 4):
                #if(self.player.getThirdCard() == 1 or self.player.getThirdCard() == 8 or self.player.getThirdCard() == 9 or self.player.getThirdCard() == 10):
                    #continue
                #else:
                if(self.player.getThirdCard() != 1 and self.player.getThirdCard() != 8 and self.player.getThirdCard() != 9 or self.player.getThirdCard() != 10):
                    self.deck.deal([self.banker])
                    #print(self.banker)
                    bankerVal = (self.banker.sum)%10
                    #print("Banker Value: ", bankerVal)
            elif(bankerVal == 5):
                if(self.player.getThirdCard() == 4 or self.player.getThirdCard() == 5 or self.player.getThirdCard() == 6 or self.player.getThirdCard() == 7):
                    self.deck.deal([self.banker])
                    #print(self.banker)
                    bankerVal = (self.banker.sum)%10
                    #print("Banker Value: ", bankerVal)
                #else:
                    #continue
            elif(bankerVal == 6):
                if(self.player.getThirdCard() == 6 or self.player.getThirdCard() == 7):
                    self.deck.deal([self.banker])
                    #print(self.banker)
                    bankerVal = (self.banker.sum)%10
                    #print("Banker Value: ", bankerVal)
                #else:
                    #continue
        
        print(self.player)
        print("Player Value: ", playerVal)
        print(self.banker)
        print("Banker Value: ", bankerVal)
          
        compareBankerVal = 9-bankerVal
        comparePlayerVal = 9-playerVal
        if(compareBankerVal < comparePlayerVal):
            winner = "Banker"
        elif(compareBankerVal > comparePlayerVal):
            winner = "Player"
        elif(compareBankerVal == comparePlayerVal):
            winner = "Tie"
        
        #for b in self.bettors:
        print(winner)
        for b in self.bettors:
            if(winner == b.getBetType):
                print(b.getName(), "won!")
                if(winner == "Player"):
                    b.setTotalMoney(b.getTotalMoney() + (b.getBet()*2))
                    print(b.getName(), "has $", b.getTotalMoney())
                elif(winner == "Banker"):
                    b.setTotalMoney(b.getTotalMoney() + (b.getBet()*1.95))
                    print(b.getName(), "has $", b.getTotalMoney())
                elif(winner == "Tie"):
                    b.setTotalMoney(b.getTotalMoney() + (b.getBet()*8))
                    print(b.getName(), "has $", b.getTotalMoney())
            else:
                if(winner == "Tie"):
                    b.setTotalMoney(b.getTotalMoney())
                    print("There was a tie, but you didn't bet on it.", b.getName(), "has $", b.getTotalMoney())
                else:
                    print(b.getName(), "lost.")
                    b.setTotalMoney(b.getTotalMoney() - b.getBet())
                    print(b.getName(), "has $", b.getTotalMoney())
                            
            if(b.getSameSuits() == True):
                sameSuitAmount = same_Suits(sameSuitBet, sameSuitMoney, self.player, self.banker)
                if(sameSuitAmount == sameSuitMoney*250 and sameSuitAmount != 0):
                    print("Congrats!", b.getName(), "wins the same suit side bet 250:1.")
                    b.setTotalMoney(b.getTotalMoney() + sameSuitAmount)
                    print(b.getName(), "has $", b.getTotalMoney())
                elif(sameSuitAmount == sameSuitMoney*25 and sameSuitAmount != 0):
                    print("Congrats!", b.getName(), "wins the same suit side bet 25:1.")
                    b.setTotalMoney(b.getTotalMoney() + sameSuitAmount)
                    print(b.getName(), "has $", b.getTotalMoney())
                else:
                    print(b.getName(), "did not win the same suit side bet.")
                    b.setTotalMoney(b.getTotalMoney() - sameSuitMoney)
                    print(b.getName(), "has $", b.getTotalMoney())
                    
            if(b.getPandaEight() == True):
                pandaEightAmount = panda_Eight(pandaEightMoney, thirdCard, playerVal)
                if(pandaEightAmount == pandaEightMoney*25 and pandaEightAmount != 0):
                    print("Congrats!", b.getName(), "wins the Panda Eight side bet 25:1.")
                    b.setTotalMoney(b.getTotalMoney() + pandaEightAmount)
                    print(b.getName(), "has $", b.getTotalMoney())
                else:
                    print(b.getName(), "did not win the Panda Eight side bet.")
                    b.setTotalMoney(b.getTotalMoney() - pandaEightMoney)
                    print(b.getName(), "has $", b.getTotalMoney())
        
        self.player.clear()
        self.banker.clear()

def main():
    print("Baccarat")
    bNames = []
    number = games.ask_number("How many bettors? (1 - 3): ", 1, 4)
    #number = 1
    for i in range(number):
        name = input("Enter bettor name: ")
        bNames.append(name)
    gameplay = Round(bNames)
    again = None
    while again != "n":
        gameplay.game()
        again = games.ask_yes_no("\nDo you want to play another round?: ")

main()
input("\n\nPress the enter key to exit.")
