Financial Pricing Model Analysis: Malawi 2024

🎯 Project Overview

This project demonstrates the development of a data-driven financial pricing model for agricultural product bundles in Malawi. The core challenge was to update the 2024 pricing strategy in response to a significant currency devaluation, ensuring product margins remain within target while maintaining farmer affordability and program sustainability.

The entire model was built and updated programmatically using Python and the Pandas library, showcasing strong technical and financial modeling skills.

🛠️ Skills Demonstrated

Category
Skills
Financial Modeling
Pricing Strategy, Cost of Goods Sold (COGS) Calculation, Margin Analysis, Revenue Forecasting, Transaction Size Calculation.
Data Analysis
Python (Pandas), Data Wrangling, Excel Automation, Assumption-Based Modeling.
Strategic Analysis
Risk Assessment (FX Volatility), Price Elasticity, Competitive Analysis, Executive Communication (Memo Drafting).





💡 The Challenge

The original 2024 budget was based on an outdated FX rate. New market conditions required an immediate update to the pricing model to prevent margin erosion.

•
New FX Rate: Update from a budget rate of 1242 MWK/USD to the confirmed 1700 MWK/USD (a 44% devaluation).

•
Pricing Goals: Maintain a product margin between 20% - 30% while ensuring the new price is competitive and affordable.

•
Program Metrics: Incorporate a strong projected 98% repayment rate and a 0.5% inventory shrink.

•
Forecasting: Use the 2023 bundle adoption rates to forecast 2024 farmer unit demand.




💻 Technical Solution: Programmatic Pricing Model

The financial model was implemented in a Python script (pricing_model_update.py) to ensure transparency, auditability, and scalability—a key requirement of the exercise.

🐍 Python Script Functionality (pricing_model_update.py)
The pricing_model_update.py script serves as the engine for the entire financial model update. It performs the following key functions:
Data Ingestion: Reads all relevant tabs (Pricing Model, Input Sheet, Bundle Configuration, 2023 Adoption) from the Excel workbook into Pandas DataFrames.
COGS Calculation: Programmatically calculates the total Cost of Goods Sold (COGS) for each product bundle by summing the COGS of its individual components, sourcing data from the Bundle Configuration tab.
Selling Price Determination: Applies the core financial formula to calculate the new Selling Price (MWK) for every product, ensuring the 25% target margin is met after factoring in the 98% repayment rate and 0.5% inventory shrink.
Adoption Forecasting: Calculates the 2024 adoption units for each region by applying the derived 2023 adoption percentages to the projected 2024 farmer base.
Model Update: Calculates all final metrics (Total Revenue, COGS, Margin, Margin %) in both the Input Sheet (per product) and the Pricing Model (aggregate) tabs, using the new 1700 MWK/USD FX rate.
Output Generation: Writes the updated DataFrames back into a new, completed Excel file, preserving the original structure of all sheets.
This script ensures that the model is dynamic, auditable, and free from hard-coded calculations, demonstrating a robust approach to financial data management.


Key Assumptions

1.
Target Margin: A target margin of 25% (the midpoint of the 20-30% range) was used for all calculations.

2.
FX Rate: The confirmed 1700 MWK/USD rate was used for all USD conversions.

3.
Adoption: 2024 unit demand was forecasted by applying 2023 adoption percentages to the projected 2024 farmer base.

Core Financial Formulas

The selling price was calculated to achieve the 25% target margin after accounting for non-repayment and inventory shrink:

1. Required Revenue (MWK)

\text{Required Revenue} = \frac{\text{COGS (MWK)}}{1 - \text{Target Margin \%}}

2. Selling Price (MWK)

\text{Selling Price} = \frac{\text{Required Revenue}}{\text{Repayment Rate} \times (1 - \text{Inventory Shrink})}




📈 Strategic Analysis: Memo to Leadership

A memo was drafted for the CFO and Country Director (CD) to highlight critical factors beyond the model's assumptions, demonstrating a holistic understanding of financial risk and operational impact.

Key Strategic Recommendations

Factor
Risk/Impact
Recommendation
FX Volatility
Market speculation of a further 15% devaluation could erode the calculated 25% margin.
Conduct a sensitivity analysis using the speculated rate (1955 MWK/USD) to prepare a contingency plan.
Price Elasticity
Significant price increases due to FX devaluation could lead to a decrease in farmer adoption.
Cross-reference new prices with market prices and consider a tiered pricing strategy or subsidy for vulnerable farmers.
Programmatic Costs
The model focuses on product margin, omitting significant operational costs (staff, logistics, training).
Review pricing in conjunction with the Site Economics to ensure prices contribute to covering the full cost of the program and achieving overall organizational sustainability.





📂 Repository Contents

•
2024_Pricing_Model_Completed.xlsx: The final Excel workbook with the updated 'Pricing Model' and 'Input Sheet' tabs.

•
pricing_model_update.py: The Python script used to perform the data extraction, calculation, and model update.

•
deliverable_1_explanation.md: Detailed documentation of the process, assumptions, formulas, and the full memo to the CFO/CD.

•
README.md: This overview.

