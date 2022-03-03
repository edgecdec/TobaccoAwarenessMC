playsound block.note_block.bell block @a[distance=..20] ~ ~ ~ 5 0 1
teleport @a[distance=..20] ~8 ~ ~ -90 0
spawnpoint @a[distance=..20] ~8 ~ ~ -90 
tellraw @a[distance=..20] ["", {"text": "Correct!"}]
