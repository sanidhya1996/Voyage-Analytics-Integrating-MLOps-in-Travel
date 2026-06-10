import pandas as pd
import os
import pickle  # Imported pickle to serialize and save the model object

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

class RandomForestModel:
    def __init__(self, data=None):
        # Fallback to avoid errors if data is not provided during initialization
        self.data = data if data is not None else pd.DataFrame()

    def random_forest(self, data=None):
        """
        Splits data, trains a Random Forest model, and prints evaluation metrics.
        """
        df = data if data is not None else self.data

        if df.empty or 'price' not in df.columns:
            print("Error: Empty dataset or target column 'price' is missing.")
            return None

        print("Preparing datasets for model training...")
        
        # Split target column (price) from features (X)
        X = df.drop(columns=['price'])
        y = df['price']
        
        # FIXED: test_test_split changed to test_size
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print(f"Training features shape: {X_train.shape}")
        print("Initializing and fitting Random Forest Regressor...")
        
        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate model performance
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        print("\n================ MODEL PERFORMANCE ================")
        print(f"Mean Squared Error (MSE) : {mse:.4f}")
        print(f"R-squared (R2) Score     : {r2:.4f}")
        print("===================================================\n")
        
        # === ADDED: SAVE THE TRAINED MODEL ===
        output_dir = '/opt/airflow/dags/utils'
        model_path = os.path.join(output_dir, 'flight_price_rf_model.pkl')
        
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        print(f"Successfully saved trained model to: {model_path}")
        # =====================================
        
        return model