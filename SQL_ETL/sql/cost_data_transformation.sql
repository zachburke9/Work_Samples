-- ====================================================
-- SQL Script: Cost Data Transformation and ETL Process
-- Description:
--   This script transforms raw cost data by computing key fields—
--   gross cost, net cost, cost adjustments, and cost discounts—
--   and derives a consolidated inventory category.
--
-- Table Structure Example:
-- Raw Cost Data Example (Service Transaction 123):
-- --------------------------------------------------
-- | Service No | Inventory Category | total_revenue |
-- |------------|--------------------|---------------|
-- |    123     |       BASE         |     100       |
-- |    123     |   ADJUSTMENT       |     -20       |
-- |    123     | PROMOTIONS         |     -10       |
-- --------------------------------------------------
--
-- Background:
--   The raw cost data contains multiple cost items per service transaction.
--   In other words, for a given service transaction (identified by its 
--   service_no), there may be several rows with different cost values.
--   These rows represent various components of the cost, such as the base cost,
--   adjustments, and promotional discounts.
-- ====================================================

WITH transformed_cost_data AS (
    SELECT 
        base.*,
        CASE 
            WHEN base.total_revenue >= 0 THEN base.total_revenue 
            ELSE 0 
        END AS gross_cost,
        base.total_revenue AS net_cost,
        CASE 
            WHEN base.total_revenue < 0 
                 AND NOT UPPER(base.inventory_category) LIKE '%PROMOTIONS%'
            THEN base.total_revenue
            ELSE 0 
        END AS cost_adjustments,
        CASE 
            WHEN base.source_system = 'SYSTEM_A'
                 AND base.total_revenue < 0
                 AND UPPER(base.inventory_category) LIKE '%PROMOTIONS%'
            THEN base.total_revenue
            WHEN base.source_system = 'SYSTEM_B'
                 AND UPPER(base.inventory_category) LIKE '%PROMOTIONS%'
                 AND base.extracted_discount IS NOT NULL
            THEN base.extracted_discount
            ELSE 0
        END AS cost_discounts
    FROM raw_cost_data base
)

SELECT 
    tc.*,
    loc.location_print_name AS service_location_name,
    emp.full_name,
    emp.team_name,
    COALESCE(tc.discount_inventory_category, tc.inventory_category) AS consolidated_inventory_category,
    home_loc.location_print_name AS home_location_name
FROM transformed_cost_data tc
LEFT JOIN locations loc
    ON tc.location_code = loc.location_code
LEFT JOIN employee_info emp
    ON tc.inserted_by = emp.login_id
LEFT JOIN account_location acct
    ON tc.account_no = acct.account_no
LEFT JOIN locations home_loc
    ON acct.location_code = home_loc.location_code
WHERE 
    tc.inventory_category NOT LIKE '%SETTLEMENT%'
    AND tc.inventory_category NOT LIKE '%SPECIAL PROMOTIONS%';
