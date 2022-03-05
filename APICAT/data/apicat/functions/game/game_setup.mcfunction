# Adds scoreboard Questions Correct
execute as @p run scoreboard objectives remove Quiz
execute as @p run scoreboard objectives add Quiz dummy {"text":"Questions Correct","bold":true}
execute as @p run scoreboard players set @a Quiz 0

# Display Questions Correct Scoreboard
execute as @p run scoreboard objectives setdisplay sidebar Quiz

# Adds scoreboard for Addiction level
execute as @p run scoreboard objectives remove AddictLevel
execute as @p run scoreboard objectives add AddictLevel dummy {"text":"Addiction Level","bold":true}
execute as @p run scoreboard players set @a AddictLevel 0