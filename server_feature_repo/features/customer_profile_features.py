"""
Customer profile features with demographic analysis and risk scoring
Demonstrates: Demographic features, risk scoring, customer segmentation, normalization
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String, Bool
from datetime import timedelta
from entities import customer
from data_sources import customer_source

# Customer demographic features are now defined in customer_features.py as customer_demographics_fv

# Customer behavioral profile features (simplified to match available data)
customer_behavioral_profile = FeatureView(
    name="customer_behavioral_profile",
    entities=[customer],
    ttl=timedelta(days=180),
    schema=[
        # Basic behavioral indicators (derived from existing data)
        Field(name="age", dtype=Int64, description="Customer age for behavioral analysis", tags={"owner": "customer_experience_team@bank.com", "domain": "behavioral", "data_classification": "confidential", "pii": "true", "business_impact": "medium", "use_case": "behavioral_segmentation", "refresh_frequency": "monthly", "compliance": "gdpr_ccpa_compliant", "validation_rules": "age_between_18_80", "business_kpi": "behavioral_accuracy"}),
        Field(name="income", dtype=Int64, description="Income for spending behavior analysis", tags={"owner": "customer_experience_team@bank.com", "domain": "behavioral", "data_classification": "confidential", "pii": "true", "business_impact": "medium", "use_case": "spending_behavior_analysis", "refresh_frequency": "quarterly", "compliance": "gdpr_ccpa_compliant", "validation_rules": "income_positive", "business_kpi": "behavioral_accuracy"}),
        Field(name="credit_score", dtype=Int64, description="Credit score for risk behavior analysis", tags={"owner": "customer_experience_team@bank.com", "domain": "behavioral", "data_classification": "confidential", "pii": "true", "business_impact": "high", "use_case": "risk_behavior_analysis", "refresh_frequency": "monthly", "compliance": "fcra_compliant", "validation_rules": "credit_score_range_300_850", "business_kpi": "behavioral_accuracy"}),
        Field(name="account_tenure_days", dtype=Int64, description="Account tenure for loyalty behavior analysis", tags={"owner": "customer_experience_team@bank.com", "domain": "behavioral", "data_classification": "internal", "pii": "false", "business_impact": "medium", "use_case": "loyalty_behavior_analysis", "refresh_frequency": "daily", "compliance": "standard", "validation_rules": "tenure_positive", "business_kpi": "behavioral_accuracy"}),
        Field(name="risk_profile", dtype=String, description="Risk profile for behavioral segmentation", tags={"owner": "customer_experience_team@bank.com", "domain": "behavioral", "data_classification": "internal", "pii": "false", "business_impact": "high", "use_case": "behavioral_segmentation", "refresh_frequency": "monthly", "compliance": "regulatory_compliant", "validation_rules": "valid_risk_profile", "business_kpi": "behavioral_accuracy"}),
        Field(name="customer_segment", dtype=String, description="Customer segment for behavioral analysis", tags={"owner": "customer_experience_team@bank.com", "domain": "behavioral", "data_classification": "internal", "pii": "false", "business_impact": "high", "use_case": "behavioral_segmentation", "refresh_frequency": "quarterly", "compliance": "standard", "validation_rules": "valid_segment", "business_kpi": "behavioral_accuracy"}),
    ],
    source=customer_source,
    tags={
        "team": "customer_experience",
        "owner": "customer_experience_team@bank.com",
        "domain": "customer",
        "data_classification": "confidential",
        "pii": "true",
        "business_impact": "high",
        "use_cases": "behavior_prediction,customer_segmentation,targeting",
        "refresh_frequency": "weekly",
        "compliance": "gdpr_ccpa_compliant",
        "feature_engineering": "behavioral_clustering_scoring",
        "model_usage": "behavior_prediction,customer_charter,marketing_targeting"
    },
    description="Customer behavioral profile features for segmentation and targeting. Uses basic demographic and account data to analyze customer behavior patterns. Includes age, income, credit score, account tenure, risk profile, and customer segment for behavioral analysis."
)
