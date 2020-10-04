import pandas as pd
import os

def filter_latex(fname):
    df = pd.read_csv(fname)
    df['len'] = df['text'].apply(lambda x: len(x.split()))
    df = df[df['len']>100]
    del df['len']
    save_name = fname.split('/')[-1].split('.')[0]
    save_name = os.path.join('csv_files', f'latex_{save_name}.csv')
    df.to_csv(save_name, index=False)


if __name__ == '__main__':
    filter_latex('./csv_files/train.csv')
    filter_latex('./csv_files/dev.csv')
