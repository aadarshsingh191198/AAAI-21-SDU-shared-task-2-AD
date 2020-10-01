import json
from collections import Counter 

with open('dataset\diction.json') as file:
    data = json.load(file)
    print(f'Number of Acronyms = {len(data.keys())}')
    print(f'Number of subacronyms = {sum([len(val) for val in data.values()])}')


def analyse_file(filename):
    with open(f'dataset\\{filename}.json') as file:
        data = json.load(file)
        print(f'Number of {filename} points = {len(data)}')
        classes = []
        for sample in data:
            classes.append(sample['tokens'][sample['acronym']])
        subclasses = []
        for sample in data:
            subclasses.append(sample['expansion'])
        print(Counter(subclasses))
        # print(Counter(classes))

analyse_file('dev')
# analyse_file('train')
