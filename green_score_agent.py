class GreenScoreAgent:

    def calculate_green_score(
        self,
        demand_satisfaction,
        cost_efficiency,
        fuel_efficiency,
        sustainability_score
    ):

        green_score = (
            0.30 * demand_satisfaction
            + 0.25 * cost_efficiency
            + 0.20 * fuel_efficiency
            + 0.25 * sustainability_score
        )

        return round(green_score, 2)


if __name__ == "__main__":

    demand_satisfaction = 100

    cost_efficiency = 85

    fuel_efficiency = 90

    sustainability_score = 93.97

    agent = GreenScoreAgent()

    score = agent.calculate_green_score(
        demand_satisfaction,
        cost_efficiency,
        fuel_efficiency,
        sustainability_score
    )

    print("\n===== GREEN SCORE =====\n")
    print("Green Score =", score)