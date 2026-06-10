import pandas as pd
import os

class DataTransformer:
    def __init__(self, data=None):
        self.data = data if data is not None else pd.DataFrame()

    def transform_data(self, data=None):
        df = data if data is not None else self.data
        
        if df.empty:
            print("No data provided for transformation.")
            return df

        print("Starting data transformation pipeline...")
        
        # 1. Drop exact duplicates
        df = df.drop_duplicates()
        
        # 2. Handle missing values
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown')
            else:
                df[col] = df[col].fillna(df[col].median())

        # === FIXED FOR OOM: DROP HIGH-UNIQUE TEXT COLUMNS ===
        # Dropping columns that have too many unique text values (like flight IDs, raw dates) 
        # which cause memory explosion during one-hot encoding.
        cols_to_drop = []
        for col in df.select_dtypes(include=['object']).columns:
            # If a text column has more than 20 unique items, it's too heavy for get_dummies
            if df[col].nunique() > 20: 
                print(f"Dropping high-cardinality column to save memory: {col}")
                cols_to_drop.append(col)
        
        if cols_to_drop:
            df = df.drop(columns=cols_to_drop)
        # ====================================================

        # 3. Feature Engineering / Encoding categorical features
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        if categorical_cols:
            print(f"One-hot encoding categorical variables: {categorical_cols}")
            df = pd.get_dummies(df, columns=categorical_cols, drop_first=True, dtype=int)
            
        # Save the cleaned data
        output_dir = '/opt/airflow/dags/utils'
        output_path = os.path.join(output_dir, 'cleaned_flights_data.csv')
        
        df.to_csv(output_path, index=False)
        print(f"Successfully saved cleaned data to: {output_path}")

        print("Data transformation complete.")
        return df