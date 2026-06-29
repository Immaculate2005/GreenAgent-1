import pandas as pd


class SustainabilityAgent:

    def calculate_score(self):

        suppliers = pd.read_csv("data/supplier_data.csv")
        routes = pd.read_csv("data/route_data.csv")

        # Best supplier from previous ranking
        best_supplier = suppliers.loc[
            suppliers["Sustainability_Rating"].idxmax()
        ]

        # Calculate route fuel efficiency
        routes["Fuel_Efficiency"] = (
            100 / routes["Fuel_Consumption"]
        )

        best_route = routes.loc[
            routes["Fuel_Efficiency"].idxmax()
        ]

        supplier_score = best_supplier[
            "Sustainability_Rating"
        ]

        fuel_efficiency = (
            best_route["Fuel_Efficiency"] * 8
        )

        resource_efficiency = 85

        sustainability_score = (
            0.4 * supplier_score
            + 0.3 * fuel_efficiency
            + 0.3 * resource_efficiency
        )

        return {
            "Supplier": best_supplier["Supplier_Name"],
            "Route": best_route["Route_Name"],
            "Sustainability_Score":
                round(sustainability_score, 2)
        }


if __name__ == "__main__":

    agent = SustainabilityAgent()

    result = agent.calculate_score()

    print("\n===== SUSTAINABILITY SCORE =====\n")

    print(result)