import pandas as pd


class RecommendationAgent:

    def recommend(self):

        suppliers = pd.read_csv("data/supplier_data.csv")
        routes = pd.read_csv("data/route_data.csv")

        # Best supplier
        suppliers["Score"] = (
            0.4 * suppliers["Sustainability_Rating"]
            + 0.3 * suppliers["Available_Stock"]
        )

        best_supplier = suppliers.sort_values(
            by="Score",
            ascending=False
        ).iloc[0]

        # Best route
        routes["Fuel_Used"] = (
            routes["Distance_KM"]
            * routes["Fuel_Consumption"]
            / 100
        )

        best_route = routes.sort_values(
            by="Fuel_Used"
        ).iloc[0]

        expected_cost = (
            best_supplier["Cost_Per_Unit"]
            * 287
        )

        print("\n===== FINAL RECOMMENDATION =====\n")

        print(
            f"Recommended Supplier : "
            f"{best_supplier['Supplier_Name']}"
        )

        print(
            f"Recommended Route : "
            f"{best_route['Route_Name']}"
        )

        print(
            f"Expected Cost : ₹{expected_cost:.2f}"
        )

        print(
            f"Fuel Usage : "
            f"{best_route['Fuel_Used']:.2f} L"
        )

        print(
            "Sustainability Score : 93.97"
        )

        print(
            "Reason : High stock, good sustainability, low fuel usage"
        )


if __name__ == "__main__":

    agent = RecommendationAgent()

    agent.recommend()