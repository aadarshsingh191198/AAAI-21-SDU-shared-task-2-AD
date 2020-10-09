import pandas as pd
import json
import os
from tqdm import tqdm

def process_file(fname):
    json_list = json.load(open(fname))
    
    for i in tqdm(range(len(json_list))):
        json_list[i]['text'] = ' '.join(json_list[i]['tokens'])
        json_list[i]['acronym_'] = json_list[i]['tokens'][json_list[i]['acronym']]

        del json_list[i]['tokens']
        del json_list[i]['acronym']
    
    df = pd.DataFrame(json_list)
    save_name = fname.split('/')[-1].split('.')[0]
    save_name = os.path.join('csv_files', f'{save_name}.csv')
    df.to_csv(save_name, index=False)

if __name__ == '__main__':
    os.makedirs('dataset', exist_ok=True)    
    process_file('./dataset/train.json')
    process_file('./dataset/dev.json')
