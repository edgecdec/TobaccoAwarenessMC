playsound entity.villager.no block @a[distance=..20] ~ ~ ~
teleport @a[distance=..20] ~8 ~ ~ -90 0
spawnpoint @a[distance=..20] ~8 ~ ~ -90 
tellraw @a[distance=..20] ["", {"text": "Incorrect!"}]