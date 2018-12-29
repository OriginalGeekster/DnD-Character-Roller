import random

#references for choosing
races = {'1':'Black Dragonborn', '2':'blue dragonborn', '3': 'brass dragonborn', '4':'bronze dragonborn', '5':'copper dragonborn', '6':'gold dragonborn', '7':'green dragonborn', '8': "red dragonborn", '9': 'silver dragonborn', '10':'white dragonborn', '11': 'dwarf','12':'hill_dwarf', '12':'elf', '13':'high elf', '14': 'drow', '15':'wood elf', '16':'gnome', '17':'rock gnome', '18':'half-elf', '19': 'half-orc', '20': 'halfling', '21':'lightfoot halfling', '22':'human', '23': 'tiefling'}
classes = {'1':'barbarian', '2':'bard', '3':'cleric','4': 'druid', '5': 'fighter', '6':'monk', '7': 'paladin', '8':'ranger','9':'rogue','10':"sorcerer",'11':'warlock','12':'wizard'}

print ("Welcome to the D&D Character Roller")

race_choice = races[str(random.randint(1,23))]
class_choice = classes[str(random.randint(1,12))]

ability_scores = []
for i in range (6):
    dice_rolls = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    dice_rolls.sort()
    del dice_rolls[3]
    final_roll = dice_rolls[0] + dice_rolls[1] + dice_rolls[2]
    ability_scores.append(final_roll)
    del dice_rolls
    del final_roll

print ("Throwing the dice...")
print ('...')
print ('...')
print ("Character Info: ")
print (race_choice + ' ' + class_choice)
print ("Ability Scores: ")
print (ability_scores)

    

        

