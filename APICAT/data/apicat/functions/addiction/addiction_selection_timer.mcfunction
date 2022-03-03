# add 1 to the scoreboard timer
scoreboard players add addictTimer AddictTimer 1

# Reset to start loop over
execute if score addictTimer AddictTimer matches 6 run scoreboard players set addictTimer AddictTimer 1
