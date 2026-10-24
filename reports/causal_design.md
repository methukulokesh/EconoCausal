# Causal Design — EconoCausal

## 1. Research Question
How does product price affect the number of units sold?

## 2. Variables
- **Treatment:** Price
- **Outcome:** Units Sold
- **Potential control variables:** Discount, Promotion, Competitor Pricing, Store ID, Product ID, and Date.

## 3. Proposed Method
Double Machine Learning (DML), subject to verifying that the dataset supports a defensible causal estimate.

## 4. Important Limitation
Differences in sales across prices do not prove that price caused those differences. Promotions, discounts, competitor prices, and other factors may influence both pricing and sales. The available control variables must be assessed before estimating a causal effect.

## 5. Next Steps
- Validate the treatment, outcome, and potential confounders.
- Check for data leakage and missing important confounders.
- Select an appropriate DML model only after assessing the data.
- Report assumptions and limitations alongside the results.