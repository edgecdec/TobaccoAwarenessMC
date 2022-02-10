
from Constants import *
import json
def generateFiles():
    with open(functionsdir + '/load.json', 'w') as file:
        file.write(json.dumps({'values': ['tobacco_awareness:load']}, indent=4))
    with open(functionsdir + '/tick.json', 'w') as file:
        file.write(json.dumps({'values': ['tobacco_awareness:tick']}, indent=4))
    with open(funcsdir + '/load.mcfunction', 'w') as file:
        pass
    with open(funcsdir + '/tick.mcfunction', 'w') as file:
        file.write('function tobacco_awareness:addiction/addiction_selection_timer')
    with open(rootdir + '/pack.mcmeta', 'w') as file:
        file.write(json.dumps({'pack': {'pack_format': 6, 'description': f'Tobacco Awareness Datapack by {", ".join(AUTHORS)}, et al.'}}, indent=4))