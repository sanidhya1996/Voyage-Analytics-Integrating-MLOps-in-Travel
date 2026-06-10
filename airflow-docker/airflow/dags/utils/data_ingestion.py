import pandas as pd
import os

class DataLoader:
    def __init__(self, file_path, on_bad_lines='skip'):
        self.file_path = file_path
        self.on_bad_lines = on_bad_lines

    def load_data(self, file_path=None):
        """
        Loads the data from the CSV file path.
        Accepts an optional file_path argument to match the op_args in the DAG.
        """
        target_path = file_path if file_path else self.file_path
        
        print(f"Starting data ingestion from: {target_path}")
        if not os.path.exists(target_path):
            # For testing purposes, create a dummy dataframe if file is missing
            print(f"Warning: {target_path} not found. Generating dummy dataset.")
            dummy_data = {
                'destination': ['Paris', 'New York', 'Tokyo', 'London', 'Delhi'],
                'duration': [5, 7, 10, 4, 6],
                'accommodation_type': ['Hotel', 'Hostel', 'Hotel', 'Apartment', 'Hotel'],
                'price': [1200, 1500, 2400, 1100, 800]
            }
            return pd.DataFrame(dummy_data)
            
        df = pd.read_csv(target_path, on_bad_lines=self.on_bad_lines)
        print(f"Successfully ingested {len(df)} rows.")
        return df