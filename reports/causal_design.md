
# Causal Design — EconoCausal

## 1. Research Question
How does product price affect the number of units sold?

## 2. Causal Variables

- Treatment: Price
- Outcome: Units Sold

## 3. Preliminary Control Variables

Potential controls:
- Competitor Pricing
- Promotion
- Weather Condition
- Seasonality
- Epidemic
- Store ID
- Product ID
- Date

These variables will only be included if their timing and causal role are appropriate.

## 4. Variables Requiring Further Investigation

- Discount: Determine whether it is part of the effective price or an independent confounder.
- Inventory Level: Verify whether it was measured before the pricing decision.
- Units Ordered: Verify its timing and relationship with demand.
- Category: Investigate inconsistent product-to-category mappings.
- Demand: Exclude from the initial model because it may contain information closely related to the outcome.

## 5. Proposed Method

Double Machine Learning (DML) for estimating the effect of continuous treatment Price on outcome Units Sold.

The estimator and nuisance models will be selected after finalizing the control variables and assessing identification assumptions.

## 6. Identification Assumptions

- No important unobserved confounders after conditioning on selected controls.
- Appropriate treatment and outcome measurement.
- Sufficient variation in price across observations.
- No inappropriate post-treatment controls.
- Appropriate temporal ordering of treatment and controls.

## 7. Limitations

Observational data cannot independently establish causality.

The estimated effect will depend on the validity of the identification assumptions and the quality of the available data.

## 8. Next Steps

1. Finalize the treatment and control-variable strategy.
2. Investigate discount and inventory timing.
3. Implement DML using defensible controls.
4. Evaluate uncertainty and model robustness.
5. Report findings with assumptions and limitations.
