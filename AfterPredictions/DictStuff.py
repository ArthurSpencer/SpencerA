leaderboard = dict()
gameover = False 
while not gameover:
    name = input("Enter Name:")
    score = input("Enter Score:")
    leaderboard[name]=score 
    answer = input("Continue Y/N:")
    answer = answer.lower()
    if answer == "n":
        gameover = True
print(leaderboard)
#Sort by Score
l = list()
for i in leaderboard:
    key = leaderboard[i]
    actualkey = i
    value = key
    l.append(actualkey)
    l.append(value)
    

