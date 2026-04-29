import pandas as pd

def get_suggestions(user_input: str, df: pd.DataFrame, top_n: int = 5):
    user_input = user_input.lower().strip()
    if not user_input or df.empty: return pd.DataFrame()
    if len(user_input) < 2: return pd.DataFrame()

    user_tokens = set(user_input.split())
    is_short_query = len(user_input) < 3
    
    def calculate_score(row_query, row_tokens, row_clicks):
        match_score = 0
        
        if row_query == user_input:
            match_score += 120
        
        if user_input in row_query:
            if row_query.startswith(user_input):
                match_score += 70
            elif not is_short_query:
                match_score += 20
            else:
                return 0
        
        common = user_tokens.intersection(row_tokens)
        if common:
            overlap_ratio = len(common) / max(len(user_tokens), 1)
            match_score += int(overlap_ratio * 40)

        if match_score == 0:
            return 0
            
        final_score = match_score + (row_clicks * 0.1)

        min_score = 50 if is_short_query else 30
        return final_score if final_score >= min_score else 0

    df['final_score'] = df.apply(lambda x: calculate_score(x['query'], x['tokens'], x.get('clicks', 1)), axis=1)
    
    results = df[df['final_score'] > 0].copy()
    if results.empty: return pd.DataFrame()

    results = results.sort_values(by='final_score', ascending=False)
    results['display'] = results.apply(lambda x: f"{x['query'].title()} ({x['category']})", axis=1)
    
    return results.head(top_n)