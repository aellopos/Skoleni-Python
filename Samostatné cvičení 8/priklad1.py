import json

with open("zavod.json", encoding='utf-8') as f:
    runners = json.load(f)

print(runners[1]['casy']['oficialni'])

finishers = [] 
for runner in runners:
    if runner['casy']['oficialni'] != 'DNF': 
        finishers.append(runner['jmeno'])   

for finisher in finishers:
    print(finisher)