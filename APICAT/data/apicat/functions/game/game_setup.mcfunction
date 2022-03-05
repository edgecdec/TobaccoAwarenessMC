# adds scoreboard Questions Correct
scoreboard objectives add Quiz dummy {"text":"Questions Correct","bold":true}

scoreboard players set @a Quiz 0

# Display objective for users in scavenger hunt
scoreboard objectives setdisplay sidebar Quiz