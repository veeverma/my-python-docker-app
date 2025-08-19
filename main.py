import pandas as pd 
def main(): 
    """
    Main function to load data a and print its head. 
    """ 
    try: 
        df = pd.read_csv('data.csv') 
        print("loaded data successfully. here are the first few rows:")
        print(df.head())
    except FileNotFoundError: 
        print("Error: data.csv not found.")
    except Exception as e: 
        print(f"An error occured: {e}")

if __name__== "__main__":
    main()