
import random
print("YOU HAVE ONLY 3 GUESSES TO GUESS A NUMBER BETWEEN 1 AND 100")
num = random.randint(1, 100)
count = 0
while count < 3:
    guess = int(input("enter the guess :"))
    if guess == num:
        count += 1
        print("YOU WON!!!!!")
        break
    elif guess > 100 or guess < 1:
        print("enter within range")
    else:
        count += 1
        print("TRY AGAIN")
print("thanks for playing")
print("the number was ", num)
