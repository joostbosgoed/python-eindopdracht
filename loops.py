#dit programa is een spelcaracter die monsters aanvalt

#hier word de health van de monsters gedefinieerd en de damage van de speler
monster_healths = {int(150), int(300), int(190)}
player_damage = 25


#hier valt de speler de monsters aan
for i in range (3):
    monster_health = list(monster_healths)[i]
    player_attacks =0
    while monster_health > 0:
        monster_health -= player_damage
        player_attacks += 1
        if monster_health < 0:
            monster_health = 0
        print(f"The monster's health is now {monster_health}")
    print(f"The player defeated the monster in {player_attacks} attacks!")
    

