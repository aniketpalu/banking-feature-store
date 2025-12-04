"""
Call center features with interaction analysis and predictive indicators
Demonstrates: Interaction analytics, predictive features, customer effort scoring
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String, Bool
from datetime import timedelta
from entities import customer
from data_sources import call_center_source

# Call center interaction patterns (90-day window) - simplified to match available data
call_center_90d = FeatureView(
    name="call_center_90d",
    entities=[customer],
    ttl=timedelta(days=90),
    schema=[
        # Basic call center data (only columns that exist in the data)
        Field(
            name="call_type", 
            dtype=String,
            description="Type of call made by customer",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "call_center",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "call_prediction,type_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "type_valid_enum",
                "business_kpi": "type_accuracy"
            }
        ),
        Field(
            name="call_duration_minutes", 
            dtype=Float64,
            description="Duration of call in minutes",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "call_center",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "call_prediction,efficiency_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "duration_non_negative",
                "business_kpi": "efficiency_accuracy"
            }
        ),
        Field(
            name="resolution_time_hours", 
            dtype=Float64,
            description="Time to resolve issue in hours",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "call_center",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "call_prediction,resolution_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "time_non_negative",
                "business_kpi": "resolution_accuracy"
            }
        ),
        Field(
            name="is_resolved", 
            dtype=Bool,
            description="Whether the call was resolved",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "call_center",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "call_prediction,resolution_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "boolean_valid",
                "business_kpi": "resolution_rate"
            }
        ),
        Field(
            name="customer_satisfaction_score", 
            dtype=Float64,
            description="Customer satisfaction score",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "call_center",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "call_prediction,satisfaction_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "score_1_to_5",
                "business_kpi": "satisfaction_accuracy"
            }
        ),
        Field(
            name="escalation_level", 
            dtype=Int64,
            description="Level of escalation for the call",
            tags={
                "owner": "customer_experience_team@bank.com",
                "domain": "call_center",
                "data_classification": "confidential",
                "pii": "false",
                "business_impact": "high",
                "use_case": "call_prediction,escalation_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "level_1_to_5",
                "business_kpi": "escalation_accuracy"
            }
        ),
    ],
    source=call_center_source,
    tags={
        "team": "customer_experience",
        "owner": "customer_experience_team@bank.com",
        "domain": "call_center",
        "data_classification": "confidential",
        "pii": "false",
        "business_impact": "high",
        "aggregation_window": "90d",
        "use_case": "call_prediction",
        "model_usage": "call_prediction,customer_service_optimization,resource_planning",
        "refresh_frequency": "daily",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_87_percent,coverage_93_percent",
        "business_kpi": "call_volume_prediction,customer_satisfaction,operational_efficiency"
    },
    description="90-day call center interaction patterns and metrics for call prediction and customer service optimization. Tracks call frequency, type analysis, duration metrics, resolution rates, satisfaction scores, and escalation patterns to predict call volumes and optimize service delivery."
)

# Call center predictive features (simplified to match available data)
call_center_predictive = FeatureView(
    name="call_center_predictive",
    entities=[customer],
    ttl=timedelta(days=180),
    schema=[
        # Basic call center data (only columns that exist in the data)
        Field(name="call_type", dtype=String, description="Type of call made by customer", tags={"owner": "customer_experience_team@bank.com", "domain": "call_center", "data_classification": "confidential", "pii": "false", "business_impact": "high", "use_case": "call_prediction,type_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "type_valid_enum", "business_kpi": "type_accuracy"}),
        Field(name="call_duration_minutes", dtype=Float64, description="Duration of call in minutes", tags={"owner": "customer_experience_team@bank.com", "domain": "call_center", "data_classification": "confidential", "pii": "false", "business_impact": "medium", "use_case": "efficiency_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "duration_non_negative", "business_kpi": "efficiency_accuracy"}),
        Field(name="resolution_time_hours", dtype=Float64, description="Time to resolve issue in hours", tags={"owner": "customer_experience_team@bank.com", "domain": "call_center", "data_classification": "confidential", "pii": "false", "business_impact": "high", "use_case": "resolution_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "time_non_negative", "business_kpi": "resolution_accuracy"}),
        Field(name="is_resolved", dtype=Bool, description="Whether the call was resolved", tags={"owner": "customer_experience_team@bank.com", "domain": "call_center", "data_classification": "confidential", "pii": "false", "business_impact": "high", "use_case": "resolution_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "boolean_valid", "business_kpi": "resolution_rate"}),
        Field(name="customer_satisfaction_score", dtype=Float64, description="Customer satisfaction score", tags={"owner": "customer_experience_team@bank.com", "domain": "call_center", "data_classification": "confidential", "pii": "false", "business_impact": "high", "use_case": "satisfaction_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "score_1_to_5", "business_kpi": "satisfaction_accuracy"}),
        Field(name="escalation_level", dtype=Int64, description="Level of escalation for the call", tags={"owner": "customer_experience_team@bank.com", "domain": "call_center", "data_classification": "confidential", "pii": "false", "business_impact": "high", "use_case": "escalation_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "level_1_to_5", "business_kpi": "escalation_accuracy"}),
    ],
    source=call_center_source,
    tags={
        "team": "customer_experience",
        "owner": "customer_experience_team@bank.com",
        "domain": "call_center",
        "data_classification": "confidential",
        "pii": "false",
        "business_impact": "high",
        "aggregation_window": "180d",
        "use_case": "proactive_service",
        "model_usage": "proactive_outreach,customer_retention,service_optimization",
        "refresh_frequency": "weekly",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_82_percent,coverage_88_percent",
        "business_kpi": "customer_retention,proactive_resolution_rate,service_quality"
    },
    description="Call center predictive features for proactive customer service and retention. Uses basic call center data including call type, duration, resolution time, resolution status, satisfaction score, and escalation level to enable proactive outreach and service optimization."
)
