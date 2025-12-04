"""
ATM location features for infrastructure optimization
Demonstrates: Location-based aggregations, infrastructure analytics, multi-entity features
"""
from feast import (
    FeatureView,
    Field,
    Entity,
)
from feast.types import Float64, Int64, String, Bool
from datetime import timedelta
from entities import atm_location, customer
from data_sources import atm_source

# ATM location performance features - simplified to match available data
atm_location_performance = FeatureView(
    name="atm_location_performance",
    entities=[atm_location],
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
        "domain": "infrastructure",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "medium",
        "use_case": "atm_optimization",
        "model_usage": "atm_placement,network_optimization,infrastructure_planning",
        "refresh_frequency": "daily",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_83_percent,coverage_89_percent",
        "business_kpi": "atm_utilization,operational_efficiency,network_performance"
    },
    description="ATM location performance metrics for infrastructure optimization and network planning. Tracks usage metrics, performance indicators, location characteristics, and operational metrics to optimize ATM placement and network efficiency."
)

# Customer-ATM interaction features (multi-entity)
customer_atm_interaction = FeatureView(
    name="customer_atm_interaction",
    entities=[customer, atm_location],
    ttl=timedelta(days=60),
    schema=[
        # Basic ATM usage data (only columns that exist in the data)
        Field(name="withdrawal_amount", dtype=Float64, description="Amount withdrawn from ATM", tags={"owner": "operations_team@bank.com", "domain": "atm", "data_classification": "internal", "pii": "false", "business_impact": "medium", "use_case": "atm_optimization,withdrawal_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "amount_non_negative", "business_kpi": "withdrawal_accuracy"}),
        Field(name="time_of_day", dtype=String, description="Time of day when ATM was used", tags={"owner": "operations_team@bank.com", "domain": "atm", "data_classification": "internal", "pii": "false", "business_impact": "medium", "use_case": "atm_optimization,time_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "time_valid", "business_kpi": "time_accuracy"}),
        Field(name="day_of_week", dtype=String, description="Day of week when ATM was used", tags={"owner": "operations_team@bank.com", "domain": "atm", "data_classification": "internal", "pii": "false", "business_impact": "medium", "use_case": "atm_optimization,pattern_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "day_valid", "business_kpi": "pattern_accuracy"}),
        Field(name="is_weekend", dtype=Bool, description="Whether the ATM usage was on weekend", tags={"owner": "operations_team@bank.com", "domain": "atm", "data_classification": "internal", "pii": "false", "business_impact": "medium", "use_case": "atm_optimization,weekend_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "boolean_valid", "business_kpi": "weekend_accuracy"}),
        Field(name="atm_zone", dtype=String, description="Zone where ATM is located", tags={"owner": "operations_team@bank.com", "domain": "atm", "data_classification": "internal", "pii": "false", "business_impact": "medium", "use_case": "atm_optimization,location_analysis", "refresh_frequency": "real_time", "compliance": "operational_data", "validation_rules": "zone_valid", "business_kpi": "location_accuracy"}),
    ],
    source=atm_source,
    tags={
        "team": "operations",
        "owner": "operations_team@bank.com",
        "domain": "customer_infrastructure",
        "data_classification": "internal",
        "pii": "false",
        "business_impact": "medium",
        "use_case": "location_optimization",
        "model_usage": "personalized_service,location_optimization,customer_behavior_analysis",
        "refresh_frequency": "weekly",
        "compliance": "operational_data",
        "performance_metrics": "accuracy_81_percent,coverage_87_percent",
        "business_kpi": "customer_satisfaction,location_efficiency,service_personalization"
    },
    description="Customer-ATM location interaction features for personalized service and location optimization. Uses basic ATM usage data including withdrawal amount, time of day, day of week, weekend flag, and ATM zone to enhance service delivery and optimize ATM network."
)
