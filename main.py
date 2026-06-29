from database.db_manager import save_recommendation
from models.demand_forecasting_agent import DemandForecastingAgent
from models.supplier_agent import SupplierAgent
from models.logistics_agent import LogisticsAgent
from models.sustainability_agent import SustainabilityAgent
from models.green_score_agent import GreenScoreAgent

print("GreenAgent Main System Started")

# Demand Forecasting

demand_agent = DemandForecastingAgent()

accuracy = demand_agent.train()

predicted_demand = demand_agent.predict_future_demand()

print("\nPredicted Demand:", predicted_demand)

# Supplier Analysis

supplier_agent = SupplierAgent(predicted_demand)

best_suppliers = supplier_agent.analyze_suppliers()

print("\n===== BEST SUPPLIERS =====\n")

print(
    best_suppliers[
        [
            "Supplier_Name",
            "Available_Stock",
            "Cost_Per_Unit",
            "Sustainability_Rating",
            "Supplier_Score"
        ]
    ]
)

best_supplier = best_suppliers.iloc[0]

print("\nBest Supplier Selected:")
print(best_supplier["Supplier_Name"])

# Logistics Analysis

logistics_agent = LogisticsAgent()

routes = logistics_agent.analyze_routes()

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

best_route = routes.iloc[0]

print("\nBest Route Selected:")
print(best_route["Route_Name"])

# Sustainability Analysis

sustainability_agent = SustainabilityAgent()

sustainability_result = sustainability_agent.calculate_score()

print("\n===== SUSTAINABILITY SCORE =====\n")

print(sustainability_result)
# Green Score Analysis

green_agent = GreenScoreAgent()

green_score = green_agent.calculate_green_score(
    demand_satisfaction=100,
    cost_efficiency=85,
    fuel_efficiency=90,
    sustainability_score=float(
        sustainability_result["Sustainability_Score"]
    )
)

print("\n===== GREEN SCORE =====\n")
print("Green Score :", green_score)
print("\n===== FINAL GREENAGENT RECOMMENDATION =====\n")

expected_cost = (
    best_supplier["Cost_Per_Unit"]
    * predicted_demand
)

print(f"Predicted Demand : {predicted_demand} Units")

print(f"Recommended Supplier : {best_supplier['Supplier_Name']}")

print(f"Recommended Route : {best_route['Route_Name']}")

print(f"Expected Cost : ₹{expected_cost:.2f}")

print(f"Fuel Usage : {best_route['Fuel_Used']:.2f} L")

print(
    f"Sustainability Score : "
    f"{sustainability_result['Sustainability_Score']}"
)

print(f"Green Score : {green_score}")

print(
    "\nReason : Selected based on demand fulfillment, "
    "supplier ranking, fuel efficiency and sustainability."
)
save_recommendation(
    predicted_demand=predicted_demand,
    supplier=best_supplier["Supplier_Name"],
    route=best_route["Route_Name"],
    expected_cost=expected_cost,
    fuel_usage=float(best_route["Fuel_Used"]),
    sustainability_score=float(
        sustainability_result["Sustainability_Score"]
    ),
    green_score=float(green_score)
)

print("\nRecommendation Saved To Database Successfully")