"""
Feature services for different ML models and use cases
Groups features by business use case for model training and serving
"""
from feast import FeatureService

# Import all feature views
from features.transaction_aggregations import (
    transaction_7d_aggregations,
    transaction_30d_aggregations,
    transaction_90d_patterns
)
from features.atm_usage_features import (
    atm_usage_30d,
    atm_time_patterns
)
from features.branch_visit_features import (
    branch_visits_90d,
    branch_service_preferences
)
from features.call_center_features import (
    call_center_90d,
    call_center_predictive
)
from features.atm_location_features import (
    atm_location_performance,
    customer_atm_interaction
)
from features.branch_features import (
    branch_performance,
    customer_branch_interaction
)
from features.transaction_features import (
    transaction_details,
    customer_transaction_interaction
)

# Customer Charter Model Feature Service
# Used for predicting customer satisfaction and loyalty
customer_charter_service = FeatureService(
    name="customer_charter_service",
    features=[
        # Customer demographics and profile
        customer_behavioral_profile,
        
        # Branch interaction features
        branch_visits_90d,
        branch_service_preferences,
        customer_branch_interaction,
        
        # Call center interaction features
        call_center_90d,
        call_center_predictive,
        
        # Transaction behavior (for context)
        transaction_30d_aggregations,
        customer_transaction_interaction,
    ],
    tags={
        "team": "customer_experience",
        "owner": "customer_experience_team@bank.com",
        "use_case": "customer_charter",
        "model_type": "classification",
        "target": "customer_satisfaction",
        "business_impact": "high",
        "sla": "real_time",
        "data_classification": "confidential",
        "pii": "true",
        "compliance": "gdpr_ccpa_compliant",
        "refresh_frequency": "real_time",
        "model_versions": "v1.0,v1.1",
        "performance_metrics": "accuracy,precision,recall,f1_score",
        "business_kpi": "customer_retention_rate",
        "description": "Features for customer charter model to predict satisfaction and loyalty"
    },
    description="Feature service for customer charter model predicting customer satisfaction and loyalty. Combines customer demographics, branch interactions, call center metrics, and transaction patterns to predict customer satisfaction scores and churn risk. Used for proactive customer retention and service improvement."
)

# Customer Behavior Prediction Feature Service
# Used for predicting spending patterns and financial needs
customer_behavior_service = FeatureService(
    name="customer_behavior_service",
    features=[
        # Transaction patterns
        transaction_7d_aggregations,
        transaction_30d_aggregations,
        transaction_90d_patterns,
        customer_transaction_interaction,
        
        # ATM usage patterns
        atm_usage_30d,
        atm_time_patterns,
        customer_atm_interaction,
        
        # Branch visit patterns
        branch_visits_90d,
        customer_branch_interaction,
    ],
    tags={
        "team": "customer_experience",
        "owner": "customer_experience_team@bank.com",
        "use_case": "behavior_prediction",
        "model_type": "regression",
        "target": "spending_patterns",
        "business_impact": "high",
        "sla": "near_real_time",
        "description": "Features for customer behavior prediction model"
    },
    description="Feature service for customer behavior prediction model to forecast spending patterns and financial needs"
)

# Call Prediction Model Feature Service
# Used for predicting likelihood of customer service calls
call_prediction_service = FeatureService(
    name="call_prediction_service",
    features=[
        
        # Call center history
        call_center_90d,
        call_center_predictive,
        
        # Branch interaction patterns
        branch_visits_90d,
        customer_branch_interaction,
        
        # Transaction issues
        transaction_30d_aggregations,
        customer_transaction_interaction,
        
        # ATM usage issues
        atm_usage_30d,
        customer_atm_interaction,
    ],
    tags={
        "team": "customer_experience",
        "owner": "customer_experience_team@bank.com",
        "use_case": "call_prediction",
        "model_type": "classification",
        "target": "call_probability",
        "business_impact": "high",
        "sla": "real_time",
        "description": "Features for call prediction model to enable proactive customer service"
    },
    description="Feature service for call prediction model to predict likelihood of customer service calls"
)

# Transaction Type Prediction Feature Service
# Used for transaction classification and fraud detection
transaction_prediction_service = FeatureService(
    name="transaction_prediction_service",
    features=[
        
        # Transaction patterns and aggregations
        transaction_7d_aggregations,
        transaction_30d_aggregations,
        transaction_90d_patterns,
        customer_transaction_interaction,
        
        # Transaction details
        transaction_details,
        
        # ATM usage patterns (for context)
        atm_usage_30d,
        customer_atm_interaction,
    ],
    tags={
        "team": "risk_fraud",
        "owner": "risk_fraud_team@bank.com",
        "use_case": "transaction_prediction",
        "model_type": "classification",
        "target": "transaction_type",
        "business_impact": "critical",
        "sla": "real_time",
        "data_classification": "confidential",
        "pii": "true",
        "compliance": "pci_dss_aml_compliant",
        "refresh_frequency": "real_time",
        "model_versions": "v2.0,v2.1,v2.2",
        "performance_metrics": "accuracy,precision,recall,f1_score,auc",
        "business_kpi": "fraud_detection_rate",
        "regulatory_requirement": "aml_compliance",
        "description": "Features for transaction type prediction and fraud detection"
    },
    description="Feature service for transaction type prediction model for fraud detection and transaction classification. Combines customer demographics, transaction patterns, velocity metrics, and behavioral indicators to detect fraudulent transactions and classify transaction types. Critical for real-time fraud prevention and AML compliance."
)

# ATM Optimization Feature Service
# Used for ATM placement and optimization
atm_optimization_service = FeatureService(
    name="atm_optimization_service",
    features=[
        # ATM location performance
        atm_location_performance,
        
        # Customer ATM usage patterns
        atm_usage_30d,
        atm_time_patterns,
        customer_atm_interaction,
        
        # Transaction patterns (for cash needs)
        transaction_30d_aggregations,
        customer_transaction_interaction,
    ],
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "use_case": "atm_optimization",
        "model_type": "regression",
        "target": "atm_utilization",
        "business_impact": "medium",
        "sla": "batch",
        "description": "Features for ATM optimization and placement decisions"
    },
    description="Feature service for ATM optimization model to improve ATM placement and utilization"
)

# Branch Optimization Feature Service
# Used for branch operations and service optimization
branch_optimization_service = FeatureService(
    name="branch_optimization_service",
    features=[
        # Branch performance metrics
        branch_performance,
        
        # Customer branch interaction patterns
        branch_visits_90d,
        branch_service_preferences,
        customer_branch_interaction,
        
        # Call center patterns (for service demand)
        call_center_90d,
        call_center_predictive,
    ],
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "use_case": "branch_optimization",
        "model_type": "regression",
        "target": "branch_efficiency",
        "business_impact": "high",
        "sla": "batch",
        "description": "Features for branch optimization and service improvement"
    },
    description="Feature service for branch optimization model to improve branch operations and customer service"
)

# Comprehensive Banking Features Service
# Used for multiple models and general banking analytics
comprehensive_banking_service = FeatureService(
    name="comprehensive_banking_service",
    features=[
        # Customer features
        customer_behavioral_profile,
        
        # Transaction features
        transaction_7d_aggregations,
        transaction_30d_aggregations,
        transaction_90d_patterns,
        transaction_details,
        customer_transaction_interaction,
        
        # ATM features
        atm_usage_30d,
        atm_time_patterns,
        atm_location_performance,
        customer_atm_interaction,
        
        # Branch features
        branch_visits_90d,
        branch_service_preferences,
        branch_performance,
        customer_branch_interaction,
        
        # Call center features
        call_center_90d,
        call_center_predictive,
    ],
    tags={
        "team": "shared",
        "owner": "data_platform_team@bank.com",
        "use_case": "comprehensive_analytics",
        "model_type": "multi_purpose",
        "target": "multiple",
        "business_impact": "high",
        "sla": "batch",
        "description": "Comprehensive feature service for multiple banking use cases and analytics"
    },
    description="Comprehensive feature service containing all banking features for multiple use cases"
)

# Risk and Compliance Feature Service
# Used for risk assessment and regulatory compliance
risk_compliance_service = FeatureService(
    name="risk_compliance_service",
    features=[
        
        # Transaction risk indicators
        transaction_7d_aggregations,
        transaction_30d_aggregations,
        transaction_90d_patterns,
        transaction_details,
        customer_transaction_interaction,
        
        # Call center risk indicators
        call_center_90d,
        call_center_predictive,
        
        # Branch interaction risk
        branch_visits_90d,
        customer_branch_interaction,
    ],
    tags={
        "team": "risk_fraud",
        "owner": "risk_fraud_team@bank.com",
        "use_case": "risk_compliance",
        "model_type": "classification",
        "target": "risk_score",
        "business_impact": "critical",
        "sla": "real_time",
        "description": "Features for risk assessment and regulatory compliance monitoring"
    },
    description="Feature service for risk assessment and compliance monitoring models"
)
