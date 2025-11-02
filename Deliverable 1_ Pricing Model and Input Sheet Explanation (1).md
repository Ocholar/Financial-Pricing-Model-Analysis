# Deliverable 1: Pricing Model and Input Sheet Explanation

## Process and Assumptions

The task required updating the 'Pricing Model' and 'Input Sheet' tabs of the provided Excel workbook based on new information and a set of pricing goals.

### Assumptions

1.  **FX Rate for 2024 Pricing:** The new FX rate of **1700 MWK/USD** as of December 2023 was used for all USD conversions in the 2024 pricing model, as this is the most recent confirmed rate. The speculated 15% devaluation in Q2 2024 was noted but not incorporated into the base pricing model, as it is a speculation and the pricing is to be approved by August 2024. This speculation will be addressed in Deliverable 2.
2.  **Target Margin:** The pricing goal states that the product margin should be between 20% and 30%. A target margin of **25%** (the midpoint) was chosen for the calculation of the selling price.
3.  **Repayment Rate:** The projected strong repayment rate of **98% (0.98)** was used to calculate the required selling price to achieve the target revenue.
4.  **Inventory Shrink:** The inventory shrink of **0.5% (0.005)**, as indicated in the 'Pricing Model' tab, was incorporated into the selling price calculation.
5.  **2024 Adoption Rate:** As per the instructions, the **2023 bundle adoption rate** (Total Adoption / Total 2023 Farmers) was assumed to be the same for the 2024 forecast.
6.  **Regional Split for Totals:** For the 'Pricing Model' tab, the total revenue, COGS, and margin for the 'Core Program USD' were calculated first. The split between the Southern and Central regions was then determined based on the ratio of their respective projected farmer numbers for 2024.

### Formulas Used

#### 1. Cost of Goods Sold (COGS)

The COGS for each bundle in the 'Input Sheet' (Columns F and J) was sourced from the 'Bundle Configuration' tab (Column H, 'COGS per bundle (MWK) - Actual'). For the main bundles (0.2 Acre, 1.5 Acre, 1 Acre, 1/2 Acre Maize bundles), the COGS was calculated as the sum of the COGS of their component products as listed in the 'Bundle Configuration' tab.

#### 2. Selling Price (MWK)

The selling price (Columns G and K in 'Input Sheet') was calculated to achieve the target margin of 25% after accounting for non-repayment and inventory shrink.

*   **Required Revenue (MWK):**
    $$ \text{Required Revenue} = \frac{\text{COGS (MWK)}}{1 - \text{Target Margin \%}} $$
*   **Selling Price (MWK):**
    $$ \text{Selling Price} = \frac{\text{Required Revenue}}{\text{Repayment Rate} \times (1 - \text{Inventory Shrink})} $$

#### 3. Adoption Units (No. Farmers)

The number of farmers adopting each bundle in each region (Columns E and I in 'Input Sheet') was calculated by applying the 2023 adoption percentage to the projected 2024 farmer numbers for that region.

*   **2023 Adoption %:**
    $$ \text{2023 Adoption \%} = \frac{\text{Total Adoption (2023)}}{\text{Total Farmers (2023)}} $$
*   **2024 Adoption Units (Region):**
    $$ \text{2024 Adoption Units} = \text{2023 Adoption \%} \times \text{Total Farmers (2024, Region)} $$

#### 4. Total Revenue, COGS, and Margin (USD)

These metrics (Columns S, T, U, V in 'Input Sheet') were calculated by summing the regional figures and converting them to USD using the new FX rate.

*   **Total Revenue (MWK):**
    $$ \text{Total Revenue (MWK)} = (\text{Southern Units} \times \text{Southern Selling Price}) + (\text{Central Units} \times \text{Central Selling Price}) $$
*   **Total Revenue (USD):**
    $$ \text{Total Revenue (USD)} = \frac{\text{Total Revenue (MWK)}}{\text{FX Rate}} $$
*   **Total COGS (MWK):**
    $$ \text{Total COGS (MWK)} = (\text{Southern Units} \times \text{Southern COGS}) + (\text{Central Units} \times \text{Central COGS}) $$
*   **Total COGS (USD):**
    $$ \text{Total COGS (USD)} = \frac{\text{Total COGS (MWK)}}{\text{FX Rate}} $$
*   **Total Margin (USD):**
    $$ \text{Total Margin (USD)} = \text{Total Revenue (USD)} - \text{Total COGS (USD)} $$
*   **Product Margin %:**
    $$ \text{Product Margin \%} = \frac{\text{Total Margin (USD)}}{\text{Total Revenue (USD)}} $$

#### 5. Pricing Model Tab Calculations

The aggregate figures in the 'Pricing Model' tab were calculated as follows:

*   **Total Farmers (Core Program USD):** Sum of Southern and Central projected farmers.
*   **Total Revenue/COGS/Margin (Core Program USD):** Sum of the respective columns in the 'Input Sheet'.
*   **Regional Revenue/COGS/Margin:** Calculated by applying the regional farmer ratio to the 'Core Program USD' total.
    $$ \text{Regional Value} = \text{Core Program USD Value} \times \frac{\text{Regional Farmers}}{\text{Total Farmers}} $$
*   **Margin %:**
    $$ \text{Margin \%} = \frac{\text{Margin}}{\text{Total Revenue}} $$
*   **TX Size (Transaction Size):**
    $$ \text{TX Size} = \frac{\text{Total Revenue}}{\text{Total Farmers}} $$
*   **FX Rate:** Updated to **1700.0** for all regions.

## Deliverable 2: Memo for CFO and CD

**MEMORANDUM**

**TO:** CFO and Country Director (CD)
**FROM:** [Candidate Name]
**DATE:** November 3, 2025
**SUBJECT:** Additional Factors for Consideration in 2024 Pricing Model Review

This memo outlines critical factors beyond the model's explicit assumptions that warrant consideration during your review of the 2024 pricing model.

### 1. Exchange Rate Volatility and Speculation

The model incorporates the confirmed December 2023 FX rate of 1700 MWK/USD. However, the market speculation of a **further 15% devaluation in Q2 2024** presents a significant risk.

*   **Impact on COGS:** Since fertilizers are imported and paid in USD, a further devaluation would directly increase the MWK-denominated COGS, eroding the calculated 25% margin.
*   **Recommendation:** A **sensitivity analysis** should be performed using the speculated rate (1700 * 1.15 = 1955 MWK/USD) to understand the impact on the final margin and to determine a contingency plan, such as a price floor or a mechanism for mid-season price adjustment, if market conditions deteriorate.

### 2. Price Elasticity and Farmer Affordability

The pricing model is driven by a target margin and cost recovery, but it does not account for the farmer's ability or willingness to pay at the new price point.

*   **Impact on Adoption:** The new selling prices are significantly higher due to the FX devaluation. While the model assumes a constant adoption rate based on 2023, the price increase could lead to a **decrease in demand** (price elasticity), especially for the higher-value bundles.
*   **Recommendation:** Cross-reference the new selling prices with **current season market prices** (as per pricing goal 2) and last year's prices (as per pricing goal 3) to ensure they remain competitive and affordable. Consider a tiered pricing strategy or increased subsidy for the most vulnerable farmers to maintain program reach.

### 3. Competitor Pricing and Market Dynamics

The pricing goal mentions staying within +/-5% of the current season market price, but the model does not explicitly incorporate a competitive analysis.

*   **Impact on Competitiveness:** A strong price increase, even if cost-justified, could make OAF's bundles less attractive compared to local competitors who may have different cost structures or are willing to operate on lower margins.
*   **Recommendation:** Conduct a **real-time market survey** of competitor pricing for comparable bundles in the Southern and Central regions to validate the competitiveness of the proposed prices before final approval.

### 4. Non-Financial Programmatic Costs

The model focuses on product COGS and associated financial costs (non-repayment, shrink) but omits the significant operational costs of the Field Program.

*   **Impact on True Margin:** Costs such as staff salaries, training, logistics, and field operations are crucial for the program's success and are not fully captured in the product margin calculation.
*   **Recommendation:** The final pricing decision should be reviewed in conjunction with the **Site Economics** tab to ensure the prices contribute adequately to covering the full cost of the program and achieving overall organizational sustainability. The strong repayment rate of 98% is a positive indicator of program effectiveness, but the cost of achieving this high rate must be factored in.

By considering these additional factors, the CFO and CD can make a more robust and risk-aware decision on the 2024 pricing model.
