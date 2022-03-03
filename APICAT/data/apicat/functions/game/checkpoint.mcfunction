playsound block.note_block.bell block @a[distance=..4,] ~ ~ ~ 5 0 1
spawnpoint @a[distance=..4] ~ ~2 ~ -90
tellraw @a[distance=..4] ["", {"text": "Checkpoint set!"}]

