
import random
count = int(input("Enter no of players :"))
loop = []
for z in range(1, count + 1):
    loop.append(z)
string = 'player_ '
players = []
for a in string:
    if a == ' ':
        for b in range(65, count + 65):
            string += chr(b)
            players.append(string)
            string = 'player_ '
length = len(players)
for c in range(0, length):
    players[c] = []
control = []
while True:
    for d in range(1, count + 1):
        if d == loop[d - 1]:
            r = random.randint(1, 6)
            players[d].append(r)
            pl = 0
            for s in range(len(players[d])):
                pl += players[d][s]
            if pl == 100:
                break
            else:
                continue
