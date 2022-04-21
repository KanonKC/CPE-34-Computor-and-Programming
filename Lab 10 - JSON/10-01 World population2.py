import json

with open('worldpopulation.json','r') as f:
    data = json.load(f)
    
class Country:
    def __init__(self,count):
        self.rank = int(count['Rank'])
        self.country = count['country']
        self.population = int(count['population'])
        self.world = float(count['World'])

    def __str__(self):
        return self.country

count = [Country(data[i]) for i in range(len(data))]

for i in range(len(count)):
    print(count[i])