import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    file_path = '../data/data.csv'  
    data = load_data(file_path)
    print(data.head())  