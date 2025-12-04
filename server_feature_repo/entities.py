"""
Entity definitions for banking feature store
"""
from feast import Entity
from feast.value_type import ValueType

# Primary entity - Customer
customer = Entity(
    name="customer",
    join_keys=["customer_id"],
    value_type=ValueType.STRING,
    description="Primary customer entity representing individual bank customers. Used across all banking use cases including customer charter, behavior prediction, fraud detection, and service optimization.",
    tags={
        "team": "shared",
        "owner": "data_platform_team@bank.com",
        "domain": "customer",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "critical",
        "use_cases": "customer_charter,behavior_prediction,fraud_detection,call_prediction",
        "refresh_frequency": "real_time",
        "compliance": "gdpr_ccpa_compliant"
    }
)

# Secondary entities for different data sources
atm_location = Entity(
    name="atm_location", 
    join_keys=["atm_id"],
    value_type=ValueType.STRING,
    description="ATM location entity for infrastructure optimization and location-based analytics. Enables ATM placement optimization, usage pattern analysis, and operational efficiency improvements.",
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "infrastructure",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "medium",
        "use_cases": "atm_optimization,infrastructure_planning,location_analytics",
        "refresh_frequency": "daily",
        "compliance": "operational_data"
    }
)

branch = Entity(
    name="branch",
    join_keys=["branch_id"],
    value_type=ValueType.STRING,
    description="Bank branch entity for branch operations optimization and customer service analytics. Supports branch performance monitoring, service optimization, and customer experience improvements.",
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "infrastructure",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "high",
        "use_cases": "branch_optimization,service_improvement,customer_experience",
        "refresh_frequency": "daily",
        "compliance": "operational_data"
    }
)

transaction = Entity(
    name="transaction",
    join_keys=["transaction_id"],
    value_type=ValueType.STRING,
    description="Transaction entity for fraud detection, risk assessment, and transaction analytics. Critical for real-time fraud detection, AML compliance, and transaction pattern analysis.",
    tags={
        "team": "risk_fraud",
        "owner": "risk_fraud_team@bank.com",
        "domain": "transaction",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "critical",
        "use_cases": "fraud_detection,aml_compliance,transaction_analytics,risk_assessment",
        "refresh_frequency": "real_time",
        "compliance": "pci_dss_aml_compliant"
    }
)
