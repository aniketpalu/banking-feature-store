"""
Transaction features for fraud detection and transaction analytics
Demonstrates: Transaction analytics, fraud detection, multi-entity features
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String, Bool
from datetime import timedelta
from entities import transaction, customer
from data_sources import transaction_source

# Transaction-level features - simplified to match available data
transaction_details = FeatureView(
    name="transaction_details",
    entities=[transaction],
    ttl=timedelta(days=7),  # Transaction details change frequently
    schema=[
        # Basic transaction info (only columns that exist in the data)
        Field(
            name="amount", 
            dtype=Float64,
            description="Transaction amount in USD, primary financial value for fraud detection and risk assessment",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "critical",
                "use_case": "fraud_detection,risk_assessment,transaction_approval",
                "refresh_frequency": "real_time",
                "compliance": "pci_dss_compliant",
                "validation_rules": "amount_non_negative",
                "business_kpi": "fraud_prevention_rate,transaction_accuracy"
            }
        ),
        Field(
            name="transaction_type", 
            dtype=String,
            description="Type of transaction (debit, credit, transfer, etc.), key categorization for fraud detection",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "fraud_detection,type_classification",
                "refresh_frequency": "real_time",
                "compliance": "pci_dss_compliant",
                "validation_rules": "type_valid_enum",
                "business_kpi": "classification_accuracy,type_validation"
            }
        ),
        Field(
            name="merchant_category", 
            dtype=String,
            description="Merchant category code (MCC), used for spending pattern analysis and fraud detection",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "fraud_detection,spending_analysis",
                "refresh_frequency": "real_time",
                "compliance": "pci_dss_compliant",
                "validation_rules": "mcc_valid",
                "business_kpi": "category_accuracy,spending_validation"
            }
        ),
        Field(
            name="location", 
            dtype=String,
            description="Transaction location (city, state, country), critical for geographic fraud detection",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "fraud_detection,geographic_analysis",
                "refresh_frequency": "real_time",
                "compliance": "pci_dss_compliant",
                "validation_rules": "location_valid",
                "business_kpi": "location_accuracy,geographic_validation"
            }
        ),
        Field(
            name="is_fraud", 
            dtype=Bool,
            description="Fraud indicator flag (true/false), ground truth for fraud detection model training",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "fraud",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "critical",
                "use_case": "fraud_detection,model_training",
                "refresh_frequency": "real_time",
                "compliance": "pci_dss_aml_compliant",
                "validation_rules": "boolean_valid",
                "business_kpi": "fraud_accuracy,model_performance"
            }
        ),
    ],
    source=transaction_source,
    tags={
        "team": "risk_fraud",
        "owner": "risk_fraud_team@bank.com",
        "domain": "transaction",
        "data_classification": "confidential",
        "pii": "false",
        "business_impact": "critical",
        "use_case": "fraud_detection",
        "model_usage": "real_time_fraud_detection,transaction_monitoring,risk_assessment",
        "refresh_frequency": "real_time",
        "compliance": "pci_dss_aml_compliant",
        "performance_metrics": "latency_under_50ms,accuracy_96_percent",
        "business_kpi": "fraud_prevention_rate,false_positive_rate,transaction_approval_rate"
    },
    description="Transaction-level features for fraud detection and risk assessment. Provides real-time transaction details, risk indicators, behavioral flags, and processing metrics to enable immediate fraud detection and transaction approval decisions."
)

# Customer-Transaction interaction features (simplified to match available data)
customer_transaction_interaction = FeatureView(
    name="customer_transaction_interaction",
    entities=[customer, transaction],
    ttl=timedelta(days=30),
    schema=[
        # Basic transaction data (only columns that exist in the data)
        Field(name="amount", dtype=Float64, description="Transaction amount in USD", tags={"owner": "risk_fraud_team@bank.com", "domain": "transaction", "data_classification": "confidential", "pii": "false", "business_impact": "critical", "use_case": "fraud_detection,risk_assessment", "refresh_frequency": "real_time", "compliance": "pci_dss_compliant", "validation_rules": "amount_non_negative", "business_kpi": "fraud_prevention_rate"}),
        Field(name="transaction_type", dtype=String, description="Type of transaction", tags={"owner": "risk_fraud_team@bank.com", "domain": "transaction", "data_classification": "confidential", "pii": "false", "business_impact": "high", "use_case": "fraud_detection,type_classification", "refresh_frequency": "real_time", "compliance": "pci_dss_compliant", "validation_rules": "type_valid_enum", "business_kpi": "classification_accuracy"}),
        Field(name="merchant_category", dtype=String, description="Merchant category", tags={"owner": "risk_fraud_team@bank.com", "domain": "transaction", "data_classification": "confidential", "pii": "false", "business_impact": "high", "use_case": "fraud_detection,spending_analysis", "refresh_frequency": "real_time", "compliance": "pci_dss_compliant", "validation_rules": "mcc_valid", "business_kpi": "category_accuracy"}),
        Field(name="is_fraud", dtype=Bool, description="Fraud indicator flag", tags={"owner": "risk_fraud_team@bank.com", "domain": "fraud", "data_classification": "confidential", "pii": "false", "business_impact": "critical", "use_case": "fraud_detection,model_training", "refresh_frequency": "real_time", "compliance": "pci_dss_aml_compliant", "validation_rules": "boolean_valid", "business_kpi": "fraud_accuracy"}),
        Field(name="location", dtype=String, description="Transaction location", tags={"owner": "risk_fraud_team@bank.com", "domain": "transaction", "data_classification": "confidential", "pii": "false", "business_impact": "high", "use_case": "fraud_detection,geographic_analysis", "refresh_frequency": "real_time", "compliance": "pci_dss_compliant", "validation_rules": "location_valid", "business_kpi": "location_accuracy"}),
    ],
    source=transaction_source,
    tags={
        "team": "risk_fraud",
        "owner": "risk_fraud_team@bank.com",
        "domain": "customer_transaction",
        "data_classification": "confidential",
        "pii": "false",
        "business_impact": "high",
        "use_case": "behavior_analysis",
        "model_usage": "behavior_analysis,risk_assessment,customer_segmentation",
        "refresh_frequency": "daily",
        "compliance": "pci_dss_compliant",
        "performance_metrics": "accuracy_89_percent,coverage_94_percent",
        "business_kpi": "risk_mitigation,customer_behavior_insights,transaction_pattern_analysis"
    },
    description="Customer-Transaction interaction features for behavior analysis and risk assessment. Uses basic transaction data including amount, type, merchant category, fraud indicator, and location to understand customer behavior and assess transaction risks."
)
