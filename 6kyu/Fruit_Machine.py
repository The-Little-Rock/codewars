# Task
# Slot machine (American English), informally fruit machine (British English), puggy 
# (Scottish English slang), the slots (Canadian and American English), poker machine (or pokies in slang) 
# (Australian English and New Zealand English) or simply slot (American English), is a casino gambling 
# machine with three or more reels which spin when a button is pushed. Slot machines are also known as 
# one-armed bandits because they were originally operated by one lever on the side of the machine as 
# distinct from a button on the front panel, and because of their ability to leave the player in debt and 
# impoverished. Many modern machines are still equipped with a legacy lever in addition to the button. 
# (Source Wikipedia)

# Task
# You will be given three reels of different images and told at which index the reels stop. From this 
# information your job is to return the score of the resulted reels.

# Rules
# 1. There are always exactly three reels
# 2. Each reel has 10 different items.
# 3. The three reel inputs may be different.
# 4. The spin array represents the index of where the reels finish.
# 5. The three spin inputs may be different
# 6. Three of the same is worth more than two of the same
# 7. Two of the same plus one "Wild" is double the score.
# 8. No matching items returns 0.

# Scoring
# Item, Three of the same, Two of the same, Two of the same plus one Wild
# Wild        100                10                   N/A
# Star         90                 9                   18
# Bell         80                 8                   16
# Shell        70                 7                   14
# Seven        60                 6                   12
# Cherry       50                 5                   10
# Bar          40                 4                    8
# King         30                 3                    6
# Queen        20                 2                    4
# Jack         10                 1                    2

# Return an integer of the score.

def fruit(reels, spins):
  valueArray = ["doesn't matter what goes here", "Jack", "Queen", "King", "Bar", "Cherry", "Seven", "Shell", "Bell", "Star","Wild"]
  rolls = {}

  # Count the unique spins
  for i, spin in enumerate(spins):
    valOfSpin = reels[i][spin]
    if valOfSpin not in rolls:
      rolls[valOfSpin] = 1
    else:
      rolls[valOfSpin] += 1
  print(rolls)

  # Return the values
  for k,v in rolls.items():
    if(v == 2 and "Wild" in rolls and k != "Wild"):
      return valueArray.index(k) * 2
    if(v == 2):
      return valueArray.index(k)
    if(v == 3):
      return 10 * valueArray.index(k)
    
  return 0


reel = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [0,0,0]
print("Should return: '100'")
print(fruit([reel,reel,reel],spin), 100, "Should return: '100'")

reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Bar", "Wild", "Queen", "Bell", "King", "Seven", "Cherry", "Jack", "Star", "Shell"]
reel3 = ["Bell", "King", "Wild", "Bar", "Seven", "Jack", "Shell", "Cherry", "Queen", "Star"]
spin = [5,4,3]
print("Should return: '0'")
print(fruit([reel1,reel2,reel3],spin), 0, "Should return: '0'")

reel1 = ["King", "Cherry", "Bar", "Jack", "Seven", "Queen", "Star", "Shell", "Bell", "Wild"]
reel2 = ["Bell", "Seven", "Jack", "Queen", "Bar", "Star", "Shell", "Wild", "Cherry", "King"]
reel3 = ["Wild", "King", "Queen", "Seven", "Star", "Bar", "Shell", "Cherry", "Jack", "Bell"]
spin = [0,0,1]
print("Should return: '3'")
print(fruit([reel1,reel2,reel3],spin), 3, "Should return: '3'")

reel1 = ["King", "Jack", "Wild", "Bell", "Star", "Seven", "Queen", "Cherry", "Shell", "Bar"]
reel2 = ["Star", "Bar", "Jack", "Seven", "Queen", "Wild", "King", "Bell", "Cherry", "Shell"]
reel3 = ["King", "Bell", "Jack", "Shell", "Star", "Cherry", "Queen", "Bar", "Wild", "Seven"]
spin = [0,5,0]
print("Should return: '6'")
print(fruit([reel1,reel2,reel3],spin), 6, "Should return: '6'")