import pandas as pd
from pathlib import Path

def load_project_data(data_dir_name="data"):
    current_path = Path(__file__).resolve()
    root_path = current_path.parents[1] 
    data_path = root_path / data_dir_name
    
    dfs = []

    files = {
        "worldcities.csv": {"term": "name", "cat": "country"},
        "unigram_freq.csv": {"term": "word", "cat": "Genel Kelime"}
    }
    
    for f_name, cols in files.items():
        f_path = data_path / f_name
        if f_path.exists():
            tmp = pd.read_csv(f_path, low_memory=False)
            tmp = tmp.rename(columns={cols['term']: 'term'})
            tmp['category'] = tmp[cols['cat']] if cols['cat'] in tmp.columns else cols['cat']
            dfs.append(tmp[['term', 'category']])
            
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

def preprocess_queries(df):
    if df.empty: return df
    df = df.dropna(subset=['term'])
    df['query'] = df['term'].astype(str).str.lower().str.strip()
    df['query_length'] = df['query'].str.len()
    df['word_count'] = df['query'].str.split().str.len()
    df['clicks'] = 100
    df['ctr'] = 0.196
    df['tokens'] = df['query'].apply(lambda x: set(str(x).split()))
    return df.drop_duplicates(subset=['query'])