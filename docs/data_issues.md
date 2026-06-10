# Data Profiling Report

## 1. sales_transactions

Total rows: 119,101

Null check:
- order_id: 0 null values detected.

Duplicate check:
- 35,090 duplicate order_id values detected.

Observation:
- This appears to be expected transactional behavior.
- One order can contain multiple product rows.
- Potential business grain: (order_id, product_id)

Data quality checks:
- order_date format appears standardized as YYYY-MM-DD.
- No blank string values detected in net_amount.
- No negative quantity values detected.
- Region values detected: Miền Bắc, Miền Trung, Miền Nam.
- Region naming appears standardized.

Planned Silver layer fixes:
- Cast order_date to DATE datatype.
- Cast numeric columns to NUMERIC / INTEGER.
- Validate correct transaction grain before deduplication.
- Standardize null handling.
- Remove technical duplicates if detected later.

## 2. sales_target_plan

Total raws: 1,950

Null check:
- employee_id: 0 null values detected.
- version_label: 0 null values detected.
- month: 0 null values detected.

Duplicate check:
- No duplicate records detected at grain (employee_id, month, version_label).

Observation:
- Multiple target versions detected (v1 and v2).
- Versioning structure has been preserved during Bronze ingestion.
- v1 contains the original yearly plan.
- v2 contains adjusted targets for the second half of the year.
- No summary rows ("TỔNG") detected.
- month column is currently stored as TEXT in Bronze layer.
- Numeric comparison produces incorrect ordering (e.g. month 10 appears smaller than month 9).

Data quality checks:
- Month values are valid and range from 1 to 12.
- Version labels are populated correctly.
- Numeric target columns are currently stored as TEXT in Bronze layer.

Planned Silver layer fixes:
- Cast numeric target columns to NUMERIC datatype.
- Cast effective date columns to DATE datatype.
- Implement target versioning logic.
- Determine effective version for each month.
- Create is_latest flag for reporting purposes.

## 3. customer_master

Total rows: 2,000

Null check:
- customer_id: 0 null values detected.

Duplicate check:
- 0 duplicate customer_id values detected.

Observation:
- customer_id appears to be a reliable primary key.
- No obvious duplicate customer records detected.

Data quality checks:
- Region values appear standardized.
- Customer names appear populated.
- No major formatting inconsistencies detected during initial inspection.

Planned Silver layer fixes:
- Cast date columns to DATE datatype if needed.
- Trim whitespace in text columns.
- Standardize null handling.
- Validate customer master uniqueness using customer_id.

## 4. product_master

Total rows: 100

Null check:
- product_id: 0 null values detected.

Duplicate check:
- 0 duplicate product_id values detected.

Observation:
- product_id appears to be a reliable primary key.
- Product category values appear standardized.
- No blank product_name values detected.

Data quality checks:
- Numeric columns are currently stored as TEXT in Bronze layer.
- No obvious formatting inconsistencies detected during initial inspection.

Planned Silver layer fixes:
- Cast numeric columns to NUMERIC datatype.
- Trim whitespace in text columns.
- Standardize null handling.
- Enforce uniqueness on product_id.

## 5. distributor_orders

Total rows: 35,945

Null check:
- product_id: 0 null values detected.
- distributor_id: 0 null values detected.

Duplicate check:
- 7,028 duplicate order_id values detected.

Observation:
- This appears to be expected transactional behavior.
- One order can contain multiple product rows.
- Potential business grain: (order_id, product_id)

Data quality checks:
- Delivery status values appear standardized.
- Channel values appear standardized.
- Date columns appear formatted as YYYY-MM-DD.
- No obvious negative quantity values detected during initial inspection.
- Numeric columns are currently stored as TEXT in Bronze layer.

Planned Silver layer fixes:
- Cast date columns to DATE datatype.
- Cast numeric columns to NUMERIC / INTEGER.
- Validate transaction grain before deduplication.
- Standardize null handling.
- Validate delivery logic and fill rate ranges.

## 6. distributor_master

Total rows: 138

Null check:
- distributor_id: 0 null values detected.

Duplicate check:
- 0 duplicate distributor_id values detected.

Observation:
- distributor_id appears to be a reliable primary key.
- No obvious data quality issues detected during initial inspection.

Planned Silver layer fixes:
- Cast join_date to DATE datatype.
- Cast credit_limit to NUMERIC datatype.
- Trim whitespace in text columns.
- Standardize null handling.
- Enforce uniqueness on distributor_id.

## 7. employee_master

Total rows: 114

Null check: 
- employee_id: 0 null values detected.

Duplicate check: 
-  0 duplicate employee_id values detected.

Observation: 
- employee_id appears to be a reliable primary key.
- Employee records appear unique during initial inspection.
- Status values appear standardized.
- Region and team naming appear consistent.
- Version column detected for employee history tracking.

Data quality checks:
- Date columns appear formatted consistently.
- No obvious formatting inconsistencies detected during initial inspection.
- Numeric and date columns are currently stored as TEXT in Bronze layer.

Planned Silver layer fixes:
- Cast date columns to DATE datatype.
- Standardize null handling.
- Trim whitespace in text columns.
- Validate employee status values.
- Enforce uniqueness on employee_id.

## 8. territory_mapping

Total rows: 1,843

Null check: 
- territory_id: 0 null values detected.
- employee_id: 0 null values detected.
- customer_id: 0 null values detected.

Duplicate check: 
- 0 duplicate terrioty_id values detected.

Observation:
- territory_id appears to be a reliable primary key.
- Employee-to-customer assignments appear complete.
- Region and team values appear standardized.
- Version column detected for territory history tracking.

Data quality checks:
- Effective and expiry dates appear consistently formatted.
- No obvious data quality issues detected during initial inspection.

Planned Silver layer fixes:
- Cast effective_date and expiry_date to DATE datatype.
- Standardize null handling.
- Trim whitespace in text columns.
- Enforce uniqueness on territory_id.
- Validate territory assignment date ranges.

## 9. return_transactions

Total rows: 3,665

Null check:
- return_id: 0 null values detected.
- original_order_id: 0 null values detected.
- product_id: 0 null values detected.

Duplicate check:
- 0 duplicate return_id values detected.

Observation:
- return_id appears to be a reliable primary key.
- Return transactions appear complete and uniquely identified.
- Return reason values appear standardized.
- Status values appear standardized.

Data quality checks:
- Date values appear formatted consistently as YYYY-MM-DD.
- No obvious negative return quantities detected.
- No obvious negative return amounts detected.
- Numeric columns are currently stored as TEXT in Bronze layer.

Planned Silver layer fixes:
- Cast date columns to DATE datatype.
- Cast numeric columns to NUMERIC / INTEGER.
- Standardize null handling.
- Trim whitespace in text columns.
- Enforce uniqueness on return_id.
- Validate return amount calculations.

## 10. promotion_program

Total rows: 40

Null check:
- promotion_id: 0 null values detected.

Duplicate check:
- 0 duplicate promotion_id values detected.

Observation:
- promotion_id appears to be a reliable primary key.
- Promotion type values appear standardized.
- Promotion status values appear standardized.
- Promotion records appear complete during initial inspection.

Data quality checks:
- Start and end dates appear consistently formatted.
- No obvious invalid discount percentages detected.
- No obvious negative budget or cost values detected.
- Numeric columns are currently stored as TEXT in Bronze layer.

Planned Silver layer fixes:
- Cast start_date and end_date to DATE datatype.
- Cast numeric columns to NUMERIC datatype.
- Standardize null handling.
- Trim whitespace in text columns.
- Enforce uniqueness on promotion_id.
- Validate promotion date ranges and discount values.