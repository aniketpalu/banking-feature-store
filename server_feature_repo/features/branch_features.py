"""
Branch features for operational analytics and performance monitoring
Demonstrates: Branch analytics, operational metrics, multi-entity features
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String, Bool
from datetime import timedelta
from entities import branch, customer
from data_sources import branch_source

# Branch performance features - simplified to match available data
branch_performance = FeatureView(
    name="branch_performance",
    entities=[branch],
    ttl=timedelta(days=30),
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
                "use_case": "branch_optimization,service_analysis",
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
                "use_case": "branch_optimization,wait_time_analysis",
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
                "use_case": "branch_optimization,service_efficiency",
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
                "use_case": "branch_optimization,employee_satisfaction",
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
                "use_case": "branch_optimization,customer_satisfaction",
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
        "domain": "infrastructure",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "high",
        "use_case": "branch_optimization",
        "model_usage": "branch_analytics,operational_optimization,performance_monitoring",
        "refresh_frequency": "daily",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_86_percent,coverage_91_percent",
        "business_kpi": "branch_efficiency,customer_satisfaction,operational_performance"
    },
    description="Branch performance metrics for operational optimization and performance monitoring. Tracks customer traffic, service metrics, operational efficiency, customer satisfaction, and financial metrics to optimize branch operations and customer experience."
)

# Customer-Branch interaction features (multi-entity) - simplified to match available data
customer_branch_interaction = FeatureView(
    name="customer_branch_interaction",
    entities=[customer, branch],
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
                "use_case": "customer_experience,service_analysis",
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
                "use_case": "customer_experience,wait_time_analysis",
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
                "use_case": "customer_experience,service_efficiency",
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
                "use_case": "customer_experience,employee_satisfaction",
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
                "use_case": "customer_experience,customer_satisfaction",
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
        "domain": "customer_infrastructure",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "high",
        "use_case": "customer_experience",
        "model_usage": "customer_experience_analytics,personalized_service,branch_optimization",
        "refresh_frequency": "weekly",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_84_percent,coverage_90_percent",
        "business_kpi": "customer_satisfaction,branch_loyalty,service_quality"
    },
    description="Customer-Branch interaction patterns for personalized service and customer experience optimization. Analyzes interaction frequency, service usage, experience metrics, and relationship strength to enhance customer experience and optimize branch service delivery."
)
