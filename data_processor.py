import pandas as pd

def clean_data(df):
    # Remove any rows with missing values
    df = df.dropna()
    
    # Reset index after dropping rows
    df.reset_index(drop=True, inplace=True)
    
    return df

def process_game_data(df):
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Create additional features if necessary
    df['home'] = df['home'].astype(int)
    df['won'] = df['total'] > df['total_opp']
    
    return df

def aggregate_team_stats(df):
    # Group by team and season to get average statistics
    team_stats = df.groupby(['team', 'season']).mean().reset_index()
    
    return team_stats

def prepare_data_for_prediction(df):
    # Select relevant features for prediction
    features = df[['team', 'team_opp', 'date', 'home', 'total', 'total_opp']]
    
    return features