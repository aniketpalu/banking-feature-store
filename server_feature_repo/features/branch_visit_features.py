"""
Branch visit features with service usage analysis and satisfaction metrics
Demonstrates: Service analytics, satisfaction scoring, operational efficiency metrics
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String, Bool
from datetime import timedelta
from entities import customer
from data_sources import branch_source

# Branch visit frequency and service usage (90-day window) - simplified to match available data
branch_visits_90d = FeatureView(
    name="branch_visits_90d",
    entities=[customer],
    ttl=timedelta(days=90),
    schema=[
        # Basic branch visit data (only columns that exist in the data)
        Field(
            name="service_type", 
            dtype=String,
            description="Type of service used at branch",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "high",
                "use_case": "customer_charter,service_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "service_type_valid",
                "business_kpi": "service_accuracy"
            }
        ),
        Field(
            name="wait_time_minutes", 
            dtype=Float64,
            description="Wait time in minutes at branch",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "high",
                "use_case": "customer_charter,wait_time_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "time_non_negative",
                "business_kpi": "wait_time_accuracy"
            }
        ),
        Field(
            name="service_duration_minutes", 
            dtype=Float64,
            description="Duration of service in minutes",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "customer_charter,service_efficiency",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "duration_non_negative",
                "business_kpi": "duration_accuracy"
            }
        ),
        Field(
            name="employee_satisfaction_score", 
            dtype=Float64,
            description="Employee satisfaction score",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "high",
                "use_case": "customer_charter,employee_satisfaction",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "score_1_to_5",
                "business_kpi": "employee_satisfaction_accuracy"
            }
        ),
        Field(
            name="customer_satisfaction_score", 
            dtype=Float64,
            description="Customer satisfaction score",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "high",
                "use_case": "customer_charter,customer_satisfaction",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "score_1_to_5",
                "business_kpi": "customer_satisfaction_accuracy"
            }
        ),
    ],
    source=branch_source,
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "branch",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "high",
        "aggregation_window": "90d",
        "use_case": "customer_charter",
        "model_usage": "customer_charter_model,service_optimization,branch_analytics",
        "refresh_frequency": "daily",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_88_percent,coverage_92_percent",
        "business_kpi": "customer_satisfaction,branch_efficiency,service_quality"
    },
    description="90-day branch visit patterns with service usage and satisfaction analysis for customer charter modeling. Tracks visit frequency, service usage analysis, operational efficiency metrics, and satisfaction scores to optimize branch operations and customer experience."
)

# Branch service preferences and satisfaction trends (180-day window) - simplified to match available data
branch_service_preferences = FeatureView(
    name="branch_service_preferences",
    entities=[customer],
    ttl=timedelta(days=180),
    schema=[
        # Basic branch visit data (only columns that exist in the data)
        Field(
            name="service_type", 
            dtype=String,
            description="Type of service used at branch",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "high",
                "use_case": "service_optimization,service_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "service_type_valid",
                "business_kpi": "service_accuracy"
            }
        ),
        Field(
            name="wait_time_minutes", 
            dtype=Float64,
            description="Wait time in minutes at branch",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "high",
                "use_case": "service_optimization,wait_time_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "time_non_negative",
                "business_kpi": "wait_time_accuracy"
            }
        ),
        Field(
            name="service_duration_minutes", 
            dtype=Float64,
            description="Duration of service in minutes",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "service_optimization,service_efficiency",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "duration_non_negative",
                "business_kpi": "duration_accuracy"
            }
        ),
        Field(
            name="employee_satisfaction_score", 
            dtype=Float64,
            description="Employee satisfaction score",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "high",
                "use_case": "service_optimization,employee_satisfaction",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "score_1_to_5",
                "business_kpi": "employee_satisfaction_accuracy"
            }
        ),
        Field(
            name="customer_satisfaction_score", 
            dtype=Float64,
            description="Customer satisfaction score",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "branch",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "high",
                "use_case": "service_optimization,customer_satisfaction",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "score_1_to_5",
                "business_kpi": "customer_satisfaction_accuracy"
            }
        ),
    ],
    source=branch_source,
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "branch",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "high",
        "aggregation_window": "180d",
        "use_case": "service_optimization",
        "model_usage": "service_optimization,customer_experience_analytics,digital_transformation",
        "refresh_frequency": "weekly",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_85_percent,coverage_90_percent",
        "business_kpi": "service_efficiency,customer_loyalty,digital_adoption"
    },
    description="180-day branch service preferences and customer experience trends for service optimization. Analyzes long-term service patterns, customer experience metrics, operational insights, and risk indicators to drive service improvements and digital transformation initiatives."
)
