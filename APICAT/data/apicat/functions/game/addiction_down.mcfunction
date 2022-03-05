# Subtract from addiction score
execute if score @s AddictLevel matches 1.. run scoreboard players remove @s AddictLevel 1

# Update their addiction modifier
execute as @s run function apicat:game/addiction_modifier