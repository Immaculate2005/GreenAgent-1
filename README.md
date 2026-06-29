# Sustainable-Multi-Agent-Coordination-for-Eco-Friendly-Supply-Chains
GreenAgent is an AI-powered Multi-Agent System for sustainable supply chain management. It forecasts demand using Machine Learning, selects the best supplier, identifies the most fuel-efficient route, calculates sustainability and Green Scores, stores results in SQLite, and displays recommendations through a Streamlit dashboard.
📌 Overview

GreenAgent is an AI-powered Multi-Agent System (MAS) designed to optimize supply chain operations while promoting sustainability. The project integrates Machine Learning, Supplier Evaluation, Logistics Optimization, and Sustainability Analysis to provide intelligent recommendations for eco-friendly supply chain management.

The system predicts future demand, selects the most suitable supplier, identifies the most fuel-efficient transportation route, calculates sustainability and Green Scores, and presents the results through an interactive Streamlit dashboard.

🚀 Features
📈 Demand Forecasting using Machine Learning
🤖 Multi-Agent System Architecture
🏭 Intelligent Supplier Selection
🚚 Logistics Route Optimization
🌿 Sustainability Score Calculation
💚 Green Score Evaluation
💾 SQLite Database Integration
📊 Interactive Streamlit Dashboard
📋 Final Recommendation Generation
🏗️ Project Architecture
Sales Data
      │
      ▼
Demand Forecasting Agent
      │
      ▼
Predicted Demand
      │
      ▼
Supplier Agent
      │
      ▼
Best Supplier
      │
      ▼
Logistics Agent
      │
      ▼
Best Route
      │
      ▼
Sustainability Agent
      │
      ▼
Green Score Agent
      │
      ▼
Recommendation Agent
      │
      ▼
SQLite Database + Streamlit Dashboard
🧠 Technologies Used
Python
Pandas
NumPy
Scikit-Learn
Random Forest Regressor
SQLite
Streamlit
Matplotlib
🤖 Agents Used
1. Demand Forecasting Agent
Predicts future product demand.
Uses Random Forest Regressor.
Evaluates model performance using R² Score, MAE, MSE, and RMSE.
2. Supplier Agent
Analyzes supplier stock availability.
Considers cost efficiency.
Evaluates sustainability ratings.
Selects the most suitable supplier.
3. Logistics Agent
Calculates fuel consumption.
Determines fuel efficiency.
Recommends the best transportation route.
4. Sustainability Agent
Computes sustainability score.
Considers supplier sustainability and fuel efficiency.
5. Green Score Agent
Calculates the overall Green Score based on operational and sustainability metrics.
6. Recommendation Agent
Generates the final recommendation including:
Best Supplier
Best Route
Expected Cost
Fuel Usage
Sustainability Score
Green Score
GreenAgent/
│
├── app.py
├── main.py
├── README.md
│
├── data/
│   ├── sales_data.csv
│   ├── supplier_data.csv
│   └── route_data.csv
│
├── database/
│   ├── database.db
│   └── db_manager.py
│
├── models/
│   ├── demand_forecasting_agent.py
│   ├── supplier_agent.py
│   ├── logistics_agent.py
│   ├── sustainability_agent.py
│   ├── green_score_agent.py
│   └── recommendation_agent.py
│
└── requirements.txt
| Metric   |   Value |
| -------- | ------: |
| R² Score |    0.53 |
| MAE      |   28.63 |
| MSE      | 1248.83 |
| RMSE     |   35.34 |
Predicted Demand : 287 Units

Best Supplier : Supplier_C

Best Route : Route_E

Expected Cost : ₹23909.97

Fuel Usage : 12.38 L

Sustainability Score : 93.97

Green Score : 92.74
💾 Database

The project stores recommendations in an SQLite database.

Stored information includes:

Predicted Demand
Supplier
Route
Expected Cost
Fuel Usage
Sustainability Score
Green Score
📊 Dashboard

The Streamlit dashboard provides:

Demand Forecast Visualization
Supplier Analysis
Route Analysis
Dynamic Demand Input
Final Recommendation
Green Score Display
▶️ Installation

Clone the repository:

git clone https://github.com/your-username/GreenAgent.git

Navigate to the project folder:

cd GreenAgent

Install the required packages:

pip install -r requirements.txt

Or install manually:

pip install pandas numpy scikit-learn matplotlib streamlit
▶️ How to Run
Step 1: Create the Database
python database/db_manager.py
Step 2: Run the Main System
python main.py
Step 3: Launch the Dashboard
streamlit run app.py
🎯 Future Enhancements
Real-time IoT integration
Live GPS route optimization
Carbon footprint analysis
Deep Learning-based demand forecasting
Cloud deployment
Mobile application support
