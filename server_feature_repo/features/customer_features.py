"""
Simple customer features for testing
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String
from datetime import timedelta
from entities import customer
from data_sources import customer_source

# Simple customer demographic features
customer_demographics_fv = FeatureView(
    name="customer_demographics_fv",
    entities=[customer],
    ttl=timedelta(days=365),
    schema=[
        Field(
            name="age", 
            dtype=Int64,
            description="Customer age in years, used for demographic analysis and risk assessment",
            tags={
                "owner": "data_platform_team@bank.com",
                "domain": "demographics",
                "data_classification": "confidential",
                "pii": "true",
                "business_impact": "medium",
                "use_case": "risk_assessment,customer_segmentation",
                "refresh_frequency": "monthly",
                "compliance": "gdpr_compliant",
                "validation_rules": "age_18_to_100",
                "business_kpi": "risk_score_accuracy"
            }
        ),
        Field(
            name="income", 
            dtype=Int64,
            description="Annual income in USD, critical for credit risk assessment and product recommendations",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "financial",
                "data_classification": "confidential",
                "pii": "true",
                "business_impact": "high",
                "use_case": "credit_assessment,product_recommendation",
                "refresh_frequency": "quarterly",
                "compliance": "gdpr_ccpa_compliant",
                "validation_rules": "income_positive",
                "business_kpi": "credit_approval_rate"
            }
        ),
        Field(
            name="credit_score", 
            dtype=Int64,
            description="FICO credit score (300-850), primary indicator for creditworthiness and loan approval",
            tags={
                "owner": "risk_fraud_team@bank.com",
                "domain": "credit",
                "data_classification": "confidential",
                "pii": "true",
                "business_impact": "critical",
                "use_case": "credit_assessment,loan_approval,fraud_detection",
                "refresh_frequency": "monthly",
                "compliance": "fcra_compliant",
                "validation_rules": "score_300_to_850",
                "business_kpi": "loan_approval_rate,default_rate"
            }
        ),
    ],
    source=customer_source,
    tags={
        "team": "shared",
        "owner": "data_platform_team@bank.com",
        "domain": "customer",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "high",
        "use_case": "customer_charter,risk_assessment,product_recommendation",
        "model_usage": "customer_segmentation,credit_assessment,demographic_analysis",
        "refresh_frequency": "monthly",
        "compliance": "gdpr_ccpa_fcra_compliant",
        "performance_metrics": "accuracy_95_percent,coverage_98_percent",
        "business_kpi": "customer_risk_score,product_approval_rate"
    },
    description="Customer demographic information including age, income, and credit score. Essential for customer charter modeling, risk assessment, and product recommendations. Contains PII and requires GDPR/CCPA compliance."
)