"""
Shared data sources for the banking feature store
This file contains all data source definitions that can be reused across different feature views
"""
from feast import FileSource

# Customer data source
customer_source = FileSource(
    name="customer_data_source",
    path="data/customers.parquet",
    timestamp_field="created_timestamp",
    description="Customer demographic and profile data including age, income, credit score, account tenure, risk profile, and customer segmentation. Contains PII and is used across all customer-centric use cases.",
    tags={
        "team": "shared",
        "owner": "data_platform_team@bank.com",
        "domain": "customer",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "critical",
        "refresh_frequency": "daily",
        "compliance": "gdpr_ccpa_compliant",
        "source_system": "core_banking_system"
    }
)

# Transaction data source
transaction_source = FileSource(
    name="transaction_data_source",
    path="data/transactions.parquet",
    timestamp_field="event_timestamp",
    description="Customer transaction data with amounts, types, merchant information, and fraud indicators. Critical for fraud detection, AML compliance, and transaction pattern analysis. Contains sensitive financial data.",
    tags={
        "team": "risk_fraud",
        "owner": "risk_fraud_team@bank.com",
        "domain": "transaction",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "critical",
        "refresh_frequency": "real_time",
        "compliance": "pci_dss_aml_compliant",
        "source_system": "transaction_processing_system"
    }
)

# ATM usage data source
atm_source = FileSource(
    name="atm_usage_data_source",
    path="data/atm_usage.parquet",
    timestamp_field="event_timestamp",
    description="ATM usage data including withdrawal amounts, locations, time patterns, and customer behavior. Used for ATM optimization, location analytics, and customer convenience analysis.",
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "atm",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "medium",
        "refresh_frequency": "hourly",
        "compliance": "operational_data",
        "source_system": "atm_network_system"
    }
)

# Branch visit data source
branch_source = FileSource(
    name="branch_details_data_source",
    path="data/branch_visits.parquet",
    timestamp_field="event_timestamp",
    description="Branch visit data including service usage, wait times, satisfaction scores, and customer interactions. Critical for branch optimization, service improvement, and customer experience analytics.",
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "branch",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "high",
        "refresh_frequency": "daily",
        "compliance": "operational_data",
        "source_system": "branch_management_system"
    }
)

# Call center data source
call_center_source = FileSource(
    name="call_center_data_source",
    path="data/call_center.parquet",
    timestamp_field="event_timestamp",
    description="Call center interaction data including call types, duration, resolution, satisfaction scores, and escalation patterns. Essential for call prediction, customer service optimization, and proactive outreach.",
    tags={
        "team": "customer_experience",
        "owner": "customer_experience_team@bank.com",
        "domain": "call_center",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "high",
        "refresh_frequency": "real_time",
        "compliance": "operational_data",
        "source_system": "call_center_system"
    }
)
