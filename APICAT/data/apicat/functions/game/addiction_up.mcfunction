# Add to addiction score
execute if score @s AddictLevel matches 2.. run scoreboard players set @s AddictLevel 4
execute if score @s AddictLevel matches ..1 run scoreboard players add @s AddictLevel 2

# Update their addiction modifier
execute as @s run function apicat:game/addiction_modifier