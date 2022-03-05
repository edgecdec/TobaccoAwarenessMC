execute as @a[distance=..20] run playsound block.note_block.bell block @s ~ ~ ~ 5 0 1
execute as @a[distance=..20] run function apicat:game/addiction_down
execute as @a[distance=..20] run teleport @s ~8 ~ ~ -90 0
execute as @a[distance=..20] run spawnpoint @s ~8 ~ ~ -90
execute as @a[distance=..20] run tellraw @s ["", {"text": "Correct!"}]
execute as @a[distance=..20] run give @p emerald 3
