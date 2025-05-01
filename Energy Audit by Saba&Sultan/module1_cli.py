
import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully:\n", df.head())
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None

def validate_data(df):
    if df is None:
        print("No data to validate.")
        return

    print("\nValidation Summary:")
    if df.isnull().values.any():
        print("- Warning: Missing values detected.")
    else:
        print("- No missing values found.")
    print("\nData Types:")
    print(df.dtypes)
    print("\nBasic Statistics:")
    print(df.describe())

if __name__ == "__main__":
    file_path = "auxiliary_energy.csv"
    df = load_data(file_path)
    validate_data(df)
