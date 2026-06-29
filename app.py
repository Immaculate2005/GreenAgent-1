import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GreenAgent",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 GreenAgent")
st.subheader(
    "Sustainable Multi-Agent Coordination for Eco-Friendly Supply Chains"
)

sales = pd.read_csv("data/sales_data.csv")
supplier = pd.read_csv("data/supplier_data.csv")
route = pd.read_csv("data/route_data.csv")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Demand Forecast",
        "Supplier Analysis",
        "Route Analysis",
        "Final Recommendation"
    ]
)

# ---------------------------
# DEMAND FORECAST
# ---------------------------

with tab1:

    st.header("Demand Forecasting")

    user_demand = st.number_input(
        "Enter Required Demand",
        min_value=1,
        value=287
    )

    st.metric(
        "Predicted Demand",
        f"{user_demand} Units"
    )

    st.metric(
        "Model Accuracy (R²)",
        "0.53"
    )

    st.line_chart(
        sales["Sales_Quantity"]
    )

# ---------------------------
# SUPPLIER ANALYSIS
# ---------------------------

with tab2:

    st.header("Supplier Analysis")

    st.dataframe(supplier)

# ---------------------------
# ROUTE ANALYSIS
# ---------------------------

with tab3:

    st.header("Route Analysis")

    route_display = route.copy()

    route_display["Fuel_Used"] = (
        route_display["Distance_KM"]
        * route_display["Fuel_Consumption"]
        / 100
    )

    st.dataframe(route_display)

# ---------------------------
# FINAL RECOMMENDATION
# ---------------------------

with tab4:

    st.header("Final Recommendation")

    filtered_suppliers = supplier[
        supplier["Available_Stock"] >= user_demand
    ]

    if len(filtered_suppliers) > 0:

        best_supplier = filtered_suppliers.sort_values(
            by="Sustainability_Rating",
            ascending=False
        ).iloc[0]

        route["Fuel_Used"] = (
            route["Distance_KM"]
            * route["Fuel_Consumption"]
            / 100
        )

        best_route = route.sort_values(
            by="Fuel_Used",
            ascending=True
        ).iloc[0]

        expected_cost = (
            best_supplier["Cost_Per_Unit"]
            * user_demand
        )

        sustainability_score = (
            best_supplier["Sustainability_Rating"]
        )

        green_score = round(
            (
                0.30 * 100
                + 0.25 * 85
                + 0.20 * 90
                + 0.25 * sustainability_score
            ),
            2
        )

        st.success(
            f"Recommended Supplier : {best_supplier['Supplier_Name']}"
        )

        st.success(
            f"Recommended Route : {best_route['Route_Name']}"
        )

        st.metric(
            "Green Score",
            green_score
        )

        st.metric(
            "Sustainability Rating",
            sustainability_score
        )

        st.write(
            f"Expected Cost : ₹{expected_cost:.2f}"
        )

        st.write(
            f"Fuel Usage : {best_route['Fuel_Used']:.2f} L"
        )

        st.write(
            "Reason : Selected based on stock availability, sustainability and fuel efficiency."
        )

    else:

        st.error(
            "No supplier available for this demand."
        )