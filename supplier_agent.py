import pandas as pd


class SupplierAgent:

    def __init__(self, predicted_demand):
        self.predicted_demand = predicted_demand

    def analyze_suppliers(self):

        suppliers = pd.read_csv("data/supplier_data.csv")

        suppliers = suppliers[
            suppliers["Available_Stock"] >= self.predicted_demand
        ]

        suppliers["Cost_Efficiency"] = (
            suppliers["Cost_Per_Unit"].max()
            - suppliers["Cost_Per_Unit"]
        )

        suppliers["Supplier_Score"] = (
            0.4 * suppliers["Sustainability_Rating"]
            + 0.3 * suppliers["Available_Stock"]
            + 0.3 * suppliers["Cost_Efficiency"]
        )

        suppliers = suppliers.sort_values(
            by="Supplier_Score",
            ascending=False
        )

        return suppliers


if __name__ == "__main__":

    predicted_demand = 287

    agent = SupplierAgent(predicted_demand)

    result = agent.analyze_suppliers()

    print("\n===== SUPPLIER RANKING =====\n")

    print(
        result[
            [
                "Supplier_Name",
                "Available_Stock",
                "Cost_Per_Unit",
                "Sustainability_Rating",
                "Supplier_Score"
            ]
        ]
    )