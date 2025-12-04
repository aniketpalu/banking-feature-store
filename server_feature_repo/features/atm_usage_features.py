"""
ATM usage features with location-based aggregations and time pattern analysis
Demonstrates: Location-based features, time pattern analysis, behavioral clustering
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String, Bool
from datetime import timedelta
from entities import customer
from data_sources import atm_source

# ATM usage frequency and location patterns (30-day window) - simplified to match available data
atm_usage_30d = FeatureView(
    name="atm_usage_30d",
    entities=[customer],
    ttl=timedelta(days=30),
    schema=[
        # Basic ATM usage data (only columns that exist in the data)
        Field(
            name="withdrawal_amount", 
            dtype=Float64,
            description="Amount withdrawn from ATM",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,withdrawal_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "amount_non_negative",
                "business_kpi": "withdrawal_accuracy"
            }
        ),
        Field(
            name="time_of_day", 
            dtype=String,
            description="Time of day when ATM was used",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,time_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "time_valid",
                "business_kpi": "time_accuracy"
            }
        ),
        Field(
            name="day_of_week", 
            dtype=String,
            description="Day of week when ATM was used",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,pattern_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "day_valid",
                "business_kpi": "pattern_accuracy"
            }
        ),
        Field(
            name="is_weekend", 
            dtype=Bool,
            description="Whether the ATM usage was on weekend",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,weekend_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "boolean_valid",
                "business_kpi": "weekend_accuracy"
            }
        ),
        Field(
            name="atm_zone", 
            dtype=String,
            description="Zone where ATM is located",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,location_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "zone_valid",
                "business_kpi": "location_accuracy"
            }
        ),
    ],
    source=atm_source,
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "atm",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "medium",
        "aggregation_window": "30d",
        "use_case": "atm_optimization",
        "model_usage": "atm_placement,usage_prediction,network_optimization",
        "refresh_frequency": "daily",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_85_percent,coverage_90_percent",
        "business_kpi": "atm_utilization,operational_efficiency"
    },
    description="30-day ATM usage patterns with location and time analysis for ATM network optimization. Includes usage metrics, location-based features, time pattern analysis, and behavioral patterns to optimize ATM placement and operations."
)

# ATM usage time patterns and preferences (60-day window) - simplified to match available data
atm_time_patterns = FeatureView(
    name="atm_time_patterns",
    entities=[customer],
    ttl=timedelta(days=60),
    schema=[
        # Basic ATM usage data (only columns that exist in the data)
        Field(
            name="withdrawal_amount", 
            dtype=Float64,
            description="Amount withdrawn from ATM",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,withdrawal_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "amount_non_negative",
                "business_kpi": "withdrawal_accuracy"
            }
        ),
        Field(
            name="time_of_day", 
            dtype=String,
            description="Time of day when ATM was used",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,time_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "time_valid",
                "business_kpi": "time_accuracy"
            }
        ),
        Field(
            name="day_of_week", 
            dtype=String,
            description="Day of week when ATM was used",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,pattern_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "day_valid",
                "business_kpi": "pattern_accuracy"
            }
        ),
        Field(
            name="is_weekend", 
            dtype=Bool,
            description="Whether the ATM usage was on weekend",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,weekend_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "boolean_valid",
                "business_kpi": "weekend_accuracy"
            }
        ),
        Field(
            name="atm_zone", 
            dtype=String,
            description="Zone where ATM is located",
            tags={
                "owner": "operations_team@bank.com",
                "domain": "atm",
                "data_classification": "internal",
                "pii": "false",
                "business_impact": "medium",
                "use_case": "atm_optimization,location_analysis",
                "refresh_frequency": "real_time",
                "compliance": "operational_data",
                "validation_rules": "zone_valid",
                "business_kpi": "location_accuracy"
            }
        ),
    ],
    source=atm_source,
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "atm",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "medium",
        "aggregation_window": "60d",
        "use_case": "behavior_prediction",
        "model_usage": "customer_segmentation,behavior_prediction,service_optimization",
        "refresh_frequency": "weekly",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_80_percent,coverage_85_percent",
        "business_kpi": "customer_satisfaction,service_efficiency"
    },
    description="ATM usage time patterns and behavioral clustering for customer segmentation. Analyzes time preferences, hourly usage patterns, day-of-week patterns, and behavioral clustering to understand customer ATM usage behavior and optimize service delivery."
)
