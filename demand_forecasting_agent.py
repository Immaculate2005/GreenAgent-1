import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


class DemandForecastingAgent:

    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

    def load_data(self):

        df = pd.read_csv("data/sales_data.csv")

        df["Date"] = pd.to_datetime(df["Date"])

        df["Day"] = df["Date"].dt.day
        df["Month"] = df["Date"].dt.month
        df["Year"] = df["Date"].dt.year
        df["DayOfWeek"] = df["Date"].dt.dayofweek

        return df

    def train(self):

        df = self.load_data()

        X = df[
            [
                "Day",
                "Month",
                "Year",
                "DayOfWeek"
            ]
        ]

        y = df["Sales_Quantity"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        # Actual vs Predicted Graph
        plt.figure(figsize=(10, 5))
        plt.plot(
            y_test.values[:50],
            label="Actual Demand"
        )

        plt.plot(
            predictions[:50],
            label="Predicted Demand"
        )

        plt.title("Actual vs Predicted Demand")
        plt.xlabel("Samples")
        plt.ylabel("Demand")
        plt.legend()
        plt.show()

        # Evaluation Metrics
        r2 = r2_score(y_test, predictions)
        mae = mean_absolute_error(y_test, predictions)
        mse = mean_squared_error(y_test, predictions)
        rmse = np.sqrt(mse)

        print("\n===== MODEL EVALUATION =====")
        print(f"R2 Score : {r2:.2f}")
        print(f"MAE : {mae:.2f}")
        print(f"MSE : {mse:.2f}")
        print(f"RMSE : {rmse:.2f}")

        return r2

    def predict_future_demand(self):

        future = pd.DataFrame({
            "Day": [1],
            "Month": [1],
            "Year": [2027],
            "DayOfWeek": [0]
        })

        prediction = self.model.predict(future)

        return int(prediction[0])


if __name__ == "__main__":

    agent = DemandForecastingAgent()

    accuracy = agent.train()

    demand = agent.predict_future_demand()

    print("\n========== DEMAND FORECAST ==========")
    print(f"Model Accuracy : {accuracy:.2f}")
    print(f"Predicted Demand : {demand} Units")