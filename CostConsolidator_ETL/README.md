# Cost Consolidator ETL

**Note**: This ETL solution demonstrates the technical approach while maintaining data confidentiality. All specific business logic and sensitive data have been removed.

## Overview
This project demonstrates an enterprise-level ETL solution for consolidating cost data across multiple systems. The solution combines SQL transformations with Alteryx workflow automation.

## Components

### SQL ETL
- Located in `SQL_ETL/cost_data_transformation.sql`
- Handles core data transformation logic
- Implements best practices for data warehouse operations

### Alteryx Workflow
- Located in `Alteryx_Workflow/`
- Automates data integration and scheduling
- Includes visual workflow documentation

### Tableau Reports (Optional)
- Located in `Tableau_Reports/`
- Provides visualization of consolidated cost data

## Implementation Details

### SQL Transformation Overview
The SQL ETL process handles:
- Computing key fields (gross cost, net cost, adjustments, discounts)
- Consolidating multiple cost items per service transaction
- Joining contextual information (locations, employee details)
- Handling data from multiple source systems

### Alteryx Workflow Configuration
The workflow performs the following steps:
1. Extracts data from SYSTEM_A and SYSTEM_B
2. Standardizes field names and data types
3. Unions the datasets
4. Schedules automated refresh (daily at 2 AM)

See `Alteryx_Workflow/workflow_diagram.png` for the visual representation.

### Raw Data Structure Example
```sql
Raw Cost Data Example (Service Transaction 123):
--------------------------------------------------
| Service No | Inventory Category | total_revenue |
|------------|--------------------|---------------|
|    123     |       BASE         |     100       |
|    123     |   ADJUSTMENT       |     -20       |
|    123     | PROMOTIONS         |     -10       |
--------------------------------------------------
```

For full implementation details, see the SQL script in `SQL_ETL/cost_data_transformation.sql`.
