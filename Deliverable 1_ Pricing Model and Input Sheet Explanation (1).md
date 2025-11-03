Deliverable 1: Pricing Model and Input Sheet 
Process and Assumptions

* Updated the “Pricing Model” and “Input Sheet” tabs in the Excel file using the new information and the pricing goals.

Assumptions

1. FX rate for 2024 pricing:

Used the confirmed December 2023 FX rate of 1700 MWK/USD for all USD conversions in the 2024 model.
The rumored 15% devaluation in Q2 2024 was noted but not used in the base pricing, since it is speculation and prices should be approved by August 2024. This is covered in Deliverable 2.


2. Target margin:

The goal is 20%–30% margin. We used 25% (the midpoint) to set selling prices.


3. Repayment rate:

Used a strong repayment rate of 98% (0.98) when calculating selling prices needed to hit target revenue.


4. Inventory shrink:

Included inventory shrink/loss of 0.5% (0.005) in the selling price calculation.


5. 2024 adoption rate:

Assumed the 2024 bundle adoption rate is the same as 2023: Total Adoption (2023) / Total Farmers (2023).


6. Regional split for totals:

In the “Pricing Model” tab, first calculated Core Program USD totals (revenue, COGS, margin), then split Southern vs Central using the ratio of their projected 2024 farmer numbers.



Formulas Used

1. Cost of Goods Sold (COGS)


* In the “Input Sheet,” COGS for each bundle (Columns F and J) comes from “Bundle Configuration” (Column H: “COGS per bundle (MWK) — Actual”).
* For the main bundles (0.2 Acre, 1.5 Acre, 1 Acre, 1/2 Acre Maize), COGS is the sum of the COGS of all products inside each bundle, as listed in “Bundle Configuration.”


1. Selling Price (MWK)


* Selling price is set to reach a 25% margin after factoring in non-repayment and inventory shrink.

* Required Revenue (MWK):
Required Revenue=1−Target Margin %COGS (MWK)​

* Selling Price (MWK):
Selling Price=Repayment Rate×(1−Inventory Shrink)Required Revenue​

* In the “Input Sheet,” selling price is in Columns G and K.



1. Adoption Units (No. of Farmers)


* Applied the 2023 adoption % to 2024 projected farmer numbers per region.

* 2023 Adoption %:
2023 Adoption %=Total Farmers (2023)Total Adoption (2023)​

* 2024 Adoption Units (by region):
2024 Adoption Units=2023 Adoption %×Total Farmers (2024, Region)

* In the “Input Sheet,” adoption units are in Columns E and I.



1. Total Revenue, COGS, and Margin (USD)


* Added Southern and Central figures, then converted MWK to USD using the new FX rate.

* In the “Input Sheet,” the USD totals are in Columns S, T, U, V.

* Total Revenue (MWK):
Total Revenue (MWK)=(Southern Units×Southern Selling Price)+(Central Units×Central Selling Price)

* Total Revenue (USD):
Total Revenue (USD)=FX RateTotal Revenue (MWK)​

* Total COGS (MWK):
Total COGS (MWK)=(Southern Units×Southern COGS)+(Central Units×Central COGS)

* Total COGS (USD):
Total COGS (USD)=FX RateTotal COGS (MWK)​

* Total Margin (USD):
Total Margin (USD)=Total Revenue (USD)−Total COGS (USD)

* Product Margin %:
Product Margin %=Total Revenue (USD)Total Margin (USD)​



1. Pricing Model tab calculations


* Total Farmers (Core Program USD):

Sum of Southern + Central projected farmers.


* Total Revenue/COGS/Margin (Core Program USD):

Sum of the respective columns from the “Input Sheet.”


* Regional Revenue/COGS/Margin:

Split by farmer ratio:
Regional Value=Core Program USD Value×Total FarmersRegional Farmers​


* Margin %:
Margin %=Total RevenueMargin​

* TX Size (Transaction Size):
TX Size=Total FarmersTotal Revenue​

* FX Rate:

Set to 1700.0 for all regions.



Deliverable 2: Memo for CFO and CD
MEMORANDUM
TO: CFO and Country Director (CD)
FROM: Reagan Ochola
DATE: November 3, 2025
SUBJECT: Extra factors to consider in the 2024 pricing review
This memo highlights important issues beyond the model’s stated assumptions that you should consider when reviewing the 2024 pricing model.

1. Exchange rate volatility and speculation


* Used the confirmed December 2023 FX rate of 1700 MWK/USD in the model. However, there is market talk of a further 15% devaluation in Q2 2024, which is a real risk.
* Impact on COGS: Since fertilizers are imported and paid in USD, a further devaluation would increase COGS in MWK and reduce our 25% margin.
* Recommendation: Run a sensitivity check using the speculated rate 1700×1.15=1955 MWK/USD to see the margin impact. Consider a contingency plan like a price floor or a way to adjust prices mid-season if the market worsens.


2. Price elasticity and farmer affordability


* Our prices are higher due to FX devaluation. The model keeps 2023 adoption rates, but higher prices may lower demand (price elasticity), especially for bigger bundles.
* Recommendation: Compare the new selling prices with current season market prices (pricing goal 2) and with last year’s prices (pricing goal 3) to stay competitive and affordable. Consider tiered pricing or more subsidy for the most vulnerable farmers to protect reach.


3. Competitor pricing and market dynamics


* The pricing goal says stay within +/-5% of current season market price, but the model does not include a competitor check.
* Impact: Even cost-justified increases can make our bundles less attractive if competitors price lower or accept smaller margins.
* Recommendation: Do a real-time market survey of competitor prices for similar bundles in Southern and Central to confirm our prices before final approval.


4. Non-financial program costs


* The model focuses on product COGS and financial adjustments (non-repayment, shrink). It does not include major Field Program costs like staff, training, logistics, and operations.
* Impact: These costs affect the true margin and program sustainability.
* Recommendation: Review final prices together with the “Site Economics” tab to ensure we cover full program costs and remain sustainable. The 98% repayment rate is a strong result, but the cost of achieving it should be included in the decision.

Considering these points will help the CFO and CD make a stronger, risk-aware decision on the 2024 pricing model.
