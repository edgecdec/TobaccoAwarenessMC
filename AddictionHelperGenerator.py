from Constants import *
import random

def namingconvention(i):
    res = ''
    i += 1
    while i > 0:
        res = chr(int(ord("a")) + ((i-1)%26)) + res
        i = i//26
    return res
def addictionHelperGenerator():

    random.shuffle(DICTION_IS_DONE_WITH_THE_TIP_OF_THE_TONGUE_AND_THE_TEETH)

    for i in range(len(DICTION_IS_DONE_WITH_THE_TIP_OF_THE_TONGUE_AND_THE_TEETH)):
        with open(addiction_helperdir + f'/{namingconvention(i)}.mcfunction', 'w') as file:
            file.write("# Change addiction score\n")
            file.write(f'execute as @s run scoreboard players add @s Addiction {DICTION_IS_DONE_WITH_THE_TIP_OF_THE_TONGUE_AND_THE_TEETH[i]}\n')
            file.write(f'execute as @s run say "Addiction score increased by {DICTION_IS_DONE_WITH_THE_TIP_OF_THE_TONGUE_AND_THE_TEETH[i]}"')

    with open(addictiondir + '/addiction_setup.mcfunction', 'w') as file:
        file.write('# Create scoreboard for storing addiction of players\n')
        file.write('execute as @p run scoreboard objectives add Addiction dummy "Addiction"\n')
        file.write('\n')
        file.write('# Create scoreboard for addiction timer\n')
        file.write('execute as @p run scoreboard objectives add AddictTimer dummy "Addiction Timer"\n')

    with open(addictiondir + '/addiction_selection_timer.mcfunction', 'w') as file:
        file.write('# add 1 to the scoreboard timer\n')
        file.write('scoreboard players add addictTimer AddictTimer 1\n')
        file.write('\n')
        file.write('# Reset to start loop over\n')
        file.write(f'execute if score addictTimer AddictTimer matches {len(DICTION_IS_DONE_WITH_THE_TIP_OF_THE_TONGUE_AND_THE_TEETH)+1} run scoreboard players set addictTimer AddictTimer 1\n')

    with open(addictiondir + '/addiction_reset.mcfunction', 'w') as file:
        file.write('function tobacco_awareness:addiction/addiction_deletion\n')
        file.write('function tobacco_awareness:addiction/addiction_setup\n')

    with open(addictiondir + '/addiction_deletion.mcfunction', 'w') as file:
        file.write('# Delete scoreboard for storing addiction of players\n')
        file.write('execute as @p run scoreboard objectives remove Addiction\n')
        file.write('\n')
        file.write('# Delete scoreboard for addiction timer\n')
        file.write('execute as @p run scoreboard objectives remove AddictTimer\n')

    with open(addictiondir + '/addction_selection_chooser.mcfunction', 'w') as file:
        file.write('# Execute "random" function depending on time.\n')
        for i in range(len(DICTION_IS_DONE_WITH_THE_TIP_OF_THE_TONGUE_AND_THE_TEETH)):
            file.write(f'execute if score addictTimer AddictTimer matches {i+1} run execute as @p run function tobacco_awareness:addiction/addiction_helper/{namingconvention(i)}\n')
