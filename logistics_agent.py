import pandas as pd


class LogisticsAgent:

    def analyze_routes(self):

        routes = pd.read_csv("data/route_data.csv")

        routes["Fuel_Used"] = (
            routes["Distance_KM"]
            * routes["Fuel_Consumption"]
            / 100
        )

        routes["Fuel_Efficiency"] = (
            100 / routes["Fuel_Consumption"]
        )

        routes = routes.sort_values(
            by="Fuel_Used",
            ascending=True
        )

        return routes


if __name__ == "__main__":

    agent = LogisticsAgent()

    routes = agent.analyze_routes()

    print("\n===== ROUTE ANALYSIS =====\n")

    print(
        routes[
            [
                "Route_Name",
                "Distance_KM",
                "Fuel_Consumption",
                "Fuel_Used",
                "Fuel_Efficiency"
            ]
        ]
    )