import pandas as pd

def get_suggestions(user_input: str, df: pd.DataFrame, top_n: int = 5):
    user_input = user_input.lower().strip()
    if not user_input or df.empty: return pd.DataFrame()

    user_tokens = set(user_input.split())
    
    def calculate_score(row_query, row_tokens, row_clicks):
        match_score = 0
        
        
        if user_input in row_query:
            if row_query.startswith(user_input):
                match_score += 50  
            else:
                match_score += 20  
        
     
        common = user_tokens.intersection(row_tokens)
        if common:
            match_score += len(common) * 30

        
        if match_score == 0:
            return 0
            
        
        return match_score + (row_clicks * 0.1)

    df['final_score'] = df.apply(lambda x: calculate_score(x['query'], x['tokens'], x.get('clicks', 1)), axis=1)
    
    results = df[df['final_score'] > 0].copy()
    if results.empty: return pd.DataFrame()

    results = results.sort_values(by='final_score', ascending=False)
    results['display'] = results.apply(lambda x: f"{x['query'].title()} ({x['category']})", axis=1)
    
    return results.head(top_n)