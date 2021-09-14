import random

wordbank = ('grape', 'banana', 'strawberry', 'blueberry', 'mango')

jumble = random.choice(wordbank)
jumbleCopy = jumble
newJumble = ''

while len(jumble) > 0:
    n = random.randint(0, len(jumble)-1)
    newJumble = newJumble + jumble[n]
    jumble = jumble[0 : n] + jumble[n+1 : ]

print("Jumble= " + newJumble)

for x in range(5):
    print("Please unscramble the word.")
    guess = input()
    if(guess == jumbleCopy):
        print("You win!")
        break;
    else:
        print("Incorrect.")
        if(x==4): print("You lose!")
