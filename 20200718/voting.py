votes = [{"name" : "Darius", "code" : 1, "votes": 0},
{"name" : "Jax", "code" : 2, "votes": 0},
{"name" : "Fiora", "code" : 3, "votes": 0},
{"name" : "Camille", "code" : 4, "votes": 0},
{"name" : "Garen", "code" : 5, "votes": 0},
{"name" : "Teemo", "code" : 6, "votes": 0},
{"name" : "Riven", "code" : 7, "votes": 0},
{"name" : "Invalid", "code" : 0, "votes": 0},
]
candidates = 7
votecount = 0
mode = "voting"
while mode != "finish":
    vote = int (input("please vote for a candidate :"))
    if vote == -1:
        mode = "finish"
    elif vote < 0 or vote > candidates:
        votes[candidates]["votes"] = votes[candidates]["votes"] + 1
    else:
        votes[vote-1]["votes"] = votes[vote-1]["votes"] + 1
    votecount = votecount + 1
    print(votes)

winner = 0
challenger = 0
while challenger < candidates:
    if votes[winner]["votes"] < votes[challenger]["votes"]:
        winner = challenger
    challenger = challenger + 1

print("========winner========")
print(votes[winner]["name"])
print(votes[winner]["votes"]/votecount)
