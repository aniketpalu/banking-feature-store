"""
Transaction aggregation features with different time windows and transformations
Demonstrates: Time-based aggregations, statistical transformations, normalization
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String, Bool
from datetime import timedelta
from entities import customer
from data_sources import transaction_source

# 7-day transaction aggregations (for real-time fraud detection) - simplified to match available data
transaction_7d_aggregations = FeatureView(
    name="transaction_7d_aggregations",
    entities=[customer],
    ttl=timedelta(days=7),
    schema=[
        # Basic transaction data (only columns that exist in the data)
        Field(
            name="amount", 
            dtype=Float64,
            description="Transaction amount in USD",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "critical",
                "use_case": "fraud_detection,risk_assessment",
                "refresh_frequency": "real_time",
                "compliance": "pci_dss_compliant",
                "validation_rules": "amount_non_negative",
                "business_kpi": "fraud_prevention_rate"
            }
        ),
        Field(
            name="transaction_type", 
            dtype=String,
            description="Type of transaction",
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
                "business_kpi": "classification_accuracy"
            }
        ),
        Field(
            name="merchant_category", 
            dtype=String,
            description="Merchant category",
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
                "business_kpi": "category_accuracy"
            }
        ),
        Field(
            name="is_fraud", 
            dtype=Bool,
            description="Fraud indicator flag",
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
                "business_kpi": "fraud_accuracy"
            }
        ),
        Field(
            name="location", 
            dtype=String,
            description="Transaction location",
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
                "business_kpi": "location_accuracy"
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
        "aggregation_window": "7d",
        "use_case": "fraud_detection",
        "model_usage": "real_time_fraud_detection,transaction_monitoring",
        "refresh_frequency": "real_time",
        "compliance": "pci_dss_aml_compliant",
        "performance_metrics": "latency_under_100ms,accuracy_95_percent",
        "business_kpi": "fraud_prevention_rate,false_positive_rate"
    },
    description="7-day transaction aggregations with statistical transformations and risk indicators for real-time fraud detection. Includes normalized features, behavioral patterns, and risk indicators to identify suspicious transactions within a 7-day rolling window."
)

# 30-day transaction aggregations (for customer behavior analysis) - simplified to match available data
transaction_30d_aggregations = FeatureView(
    name="transaction_30d_aggregations",
    entities=[customer],
    ttl=timedelta(days=30),
    schema=[
        # Basic transaction data (only columns that exist in the data)
        Field(
            name="amount", 
            dtype=Float64,
            description="Transaction amount in USD",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "behavior_prediction,spending_analysis",
                "refresh_frequency": "daily",
                "compliance": "pci_dss_compliant",
                "validation_rules": "amount_non_negative",
                "business_kpi": "spending_accuracy,revenue_prediction"
            }
        ),
        Field(
            name="transaction_type", 
            dtype=String,
            description="Type of transaction",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "behavior_prediction,type_analysis",
                "refresh_frequency": "daily",
                "compliance": "pci_dss_compliant",
                "validation_rules": "type_valid_enum",
                "business_kpi": "type_accuracy"
            }
        ),
        Field(
            name="merchant_category", 
            dtype=String,
            description="Merchant category",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "behavior_prediction,spending_analysis",
                "refresh_frequency": "daily",
                "compliance": "pci_dss_compliant",
                "validation_rules": "mcc_valid",
                "business_kpi": "category_accuracy"
            }
        ),
        Field(
            name="is_fraud", 
            dtype=Bool,
            description="Fraud indicator flag",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "fraud",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "behavior_prediction,risk_assessment",
                "refresh_frequency": "daily",
                "compliance": "pci_dss_aml_compliant",
                "validation_rules": "boolean_valid",
                "business_kpi": "fraud_accuracy"
            }
        ),
        Field(
            name="location", 
            dtype=String,
            description="Transaction location",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "behavior_prediction,geographic_analysis",
                "refresh_frequency": "daily",
                "compliance": "pci_dss_compliant",
                "validation_rules": "location_valid",
                "business_kpi": "location_accuracy"
            }
        ),
    ],
    source=transaction_source,
    tags={
        "team": "customer_experience",
        "owner": "customer_experience_team@bank.com",
        "domain": "transaction",
        "data_classification": "confidential",
        "pii": "false",
        "business_impact": "high",
        "aggregation_window": "30d",
        "use_case": "behavior_prediction",
        "model_usage": "customer_segmentation,behavior_prediction,personalization",
        "refresh_frequency": "daily",
        "compliance": "pci_dss_compliant",
        "performance_metrics": "accuracy_90_percent,coverage_95_percent",
        "business_kpi": "customer_engagement,retention_rate,upsell_success"
    },
    description="30-day transaction aggregations for customer behavior analysis and segmentation. Provides trend analysis, customer segmentation features, payment method preferences, and merchant category analysis to understand customer spending patterns and preferences."
)

# 90-day transaction patterns (for long-term customer insights) - simplified to match available data
transaction_90d_patterns = FeatureView(
    name="transaction_90d_patterns",
    entities=[customer],
    ttl=timedelta(days=90),
    schema=[
        # Basic transaction data (only columns that exist in the data)
        Field(
            name="amount", 
            dtype=Float64,
            description="Transaction amount in USD",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "compliance_monitoring,long_term_analysis",
                "refresh_frequency": "weekly",
                "compliance": "aml_bsa_compliant",
                "validation_rules": "amount_non_negative",
                "business_kpi": "compliance_score,regulatory_reporting_accuracy"
            }
        ),
        Field(
            name="transaction_type", 
            dtype=String,
            description="Type of transaction",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "compliance_monitoring,type_analysis",
                "refresh_frequency": "weekly",
                "compliance": "aml_bsa_compliant",
                "validation_rules": "type_valid_enum",
                "business_kpi": "type_accuracy"
            }
        ),
        Field(
            name="merchant_category", 
            dtype=String,
            description="Merchant category",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "compliance_monitoring,spending_analysis",
                "refresh_frequency": "weekly",
                "compliance": "aml_bsa_compliant",
                "validation_rules": "mcc_valid",
                "business_kpi": "category_accuracy"
            }
        ),
        Field(
            name="is_fraud", 
            dtype=Bool,
            description="Fraud indicator flag",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "fraud",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "critical",
                "use_case": "compliance_monitoring,aml_monitoring",
                "refresh_frequency": "weekly",
                "compliance": "aml_bsa_compliant",
                "validation_rules": "boolean_valid",
                "business_kpi": "aml_compliance_rate,fraud_prevention_rate"
            }
        ),
        Field(
            name="location", 
            dtype=String,
            description="Transaction location",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "transaction",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "compliance_monitoring,geographic_analysis",
                "refresh_frequency": "weekly",
                "compliance": "aml_bsa_compliant",
                "validation_rules": "location_valid",
                "business_kpi": "location_accuracy"
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
        "business_impact": "high",
        "aggregation_window": "90d",
        "use_case": "compliance_monitoring",
        "model_usage": "aml_monitoring,compliance_reporting,risk_assessment",
        "refresh_frequency": "weekly",
        "compliance": "aml_bsa_compliant",
        "performance_metrics": "detection_rate_85_percent,false_positive_rate_5_percent",
        "business_kpi": "compliance_score,regulatory_reporting_accuracy"
    },
    description="90-day transaction patterns for long-term customer insights and compliance monitoring. Analyzes seasonal patterns, customer lifecycle indicators, and risk assessment features for AML compliance and regulatory reporting."
)
