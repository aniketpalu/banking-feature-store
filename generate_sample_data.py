"""
Generate sample banking data for Feast demo
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Set random seed for reproducibility
np.random.seed(42)

def generate_customer_data():
    """Generate customer demographic and account data"""
    n_customers = 1000
    
    data = {
        'customer_id': [f'CUST_{i:06d}' for i in range(1, n_customers + 1)],
        'age': np.random.randint(18, 80, n_customers),
        'income': np.random.lognormal(10, 0.5, n_customers).astype(int),
        'credit_score': np.random.normal(650, 100, n_customers).astype(int),
        'account_tenure_days': np.random.randint(30, 3650, n_customers),
        'risk_profile': np.random.choice(['LOW', 'MEDIUM', 'HIGH'], n_customers, p=[0.6, 0.3, 0.1]),
        'customer_segment': np.random.choice(['PREMIUM', 'STANDARD', 'BASIC'], n_customers, p=[0.2, 0.6, 0.2]),
        'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], n_customers),
        'state': np.random.choice(['NY', 'CA', 'IL', 'TX', 'AZ'], n_customers),
        'created_timestamp': pd.date_range('2020-01-01', periods=n_customers, freq='1D')
    }
    
    # Ensure credit score is within valid range
    data['credit_score'] = np.clip(data['credit_score'], 300, 850)
    
    return pd.DataFrame(data)

def generate_transaction_data():
    """Generate transaction data"""
    n_transactions = 50000
    customer_ids = [f'CUST_{i:06d}' for i in range(1, 1001)]
    
    # Generate timestamps over the last 90 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    timestamps = pd.date_range(start_date, end_date, periods=n_transactions)
    
    data = {
        'customer_id': np.random.choice(customer_ids, n_transactions),
        'transaction_id': [f'TXN_{i:08d}' for i in range(1, n_transactions + 1)],
        'amount': np.random.lognormal(5, 1.5, n_transactions),
        'transaction_type': np.random.choice(['ATM_WITHDRAWAL', 'DEBIT_CARD', 'ONLINE_TRANSFER', 'CHECK', 'CASH_DEPOSIT'], 
                                           n_transactions, p=[0.3, 0.4, 0.15, 0.1, 0.05]),
        'merchant_category': np.random.choice(['GROCERY', 'GAS', 'RESTAURANT', 'RETAIL', 'UTILITIES', 'HEALTHCARE'], 
                                            n_transactions),
        'is_fraud': np.random.choice([0, 1], n_transactions, p=[0.95, 0.05]),
        'location': np.random.choice(['LOCAL', 'REGIONAL', 'NATIONAL', 'INTERNATIONAL'], 
                                   n_transactions, p=[0.6, 0.25, 0.1, 0.05]),
        'event_timestamp': timestamps
    }
    
    # Round amounts to 2 decimal places
    data['amount'] = np.round(data['amount'], 2)
    
    return pd.DataFrame(data)

def generate_atm_usage_data():
    """Generate ATM usage data"""
    n_atm_usage = 15000
    customer_ids = [f'CUST_{i:06d}' for i in range(1, 1001)]
    atm_locations = [f'ATM_{i:03d}' for i in range(1, 51)]
    
    # Generate timestamps over the last 60 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)
    timestamps = pd.date_range(start_date, end_date, periods=n_atm_usage)
    
    data = {
        'customer_id': np.random.choice(customer_ids, n_atm_usage),
        'atm_id': np.random.choice(atm_locations, n_atm_usage),
        'withdrawal_amount': np.random.lognormal(4, 1, n_atm_usage),
        'time_of_day': np.random.randint(0, 24, n_atm_usage),
        'day_of_week': np.random.randint(0, 7, n_atm_usage),
        'is_weekend': np.random.choice([0, 1], n_atm_usage, p=[0.7, 0.3]),
        'atm_zone': np.random.choice(['DOWNTOWN', 'SUBURBAN', 'AIRPORT', 'MALL'], n_atm_usage),
        'event_timestamp': timestamps
    }
    
    # Round amounts to 2 decimal places
    data['withdrawal_amount'] = np.round(data['withdrawal_amount'], 2)
    
    return pd.DataFrame(data)

def generate_branch_visit_data():
    """Generate branch visit data"""
    n_visits = 8000
    customer_ids = [f'CUST_{i:06d}' for i in range(1, 1001)]
    branch_ids = [f'BRANCH_{i:03d}' for i in range(1, 21)]
    
    # Generate timestamps over the last 120 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=120)
    timestamps = pd.date_range(start_date, end_date, periods=n_visits)
    
    data = {
        'customer_id': np.random.choice(customer_ids, n_visits),
        'branch_id': np.random.choice(branch_ids, n_visits),
        'service_type': np.random.choice(['ACCOUNT_OPENING', 'LOAN_APPLICATION', 'INQUIRY', 'TRANSACTION', 'COMPLAINT'], 
                                       n_visits, p=[0.1, 0.2, 0.3, 0.3, 0.1]),
        'wait_time_minutes': np.random.exponential(15, n_visits),
        'service_duration_minutes': np.random.exponential(20, n_visits),
        'employee_satisfaction_score': np.random.uniform(1, 5, n_visits),
        'customer_satisfaction_score': np.random.uniform(1, 5, n_visits),
        'event_timestamp': timestamps
    }
    
    # Round scores to 1 decimal place
    data['employee_satisfaction_score'] = np.round(data['employee_satisfaction_score'], 1)
    data['customer_satisfaction_score'] = np.round(data['customer_satisfaction_score'], 1)
    data['wait_time_minutes'] = np.round(data['wait_time_minutes'], 1)
    data['service_duration_minutes'] = np.round(data['service_duration_minutes'], 1)
    
    return pd.DataFrame(data)

def generate_call_center_data():
    """Generate call center data"""
    n_calls = 12000
    customer_ids = [f'CUST_{i:06d}' for i in range(1, 1001)]
    
    # Generate timestamps over the last 90 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    timestamps = pd.date_range(start_date, end_date, periods=n_calls)
    
    data = {
        'customer_id': np.random.choice(customer_ids, n_calls),
        'call_id': [f'CALL_{i:08d}' for i in range(1, n_calls + 1)],
        'call_type': np.random.choice(['INQUIRY', 'COMPLAINT', 'TECHNICAL_SUPPORT', 'ACCOUNT_ISSUE', 'PRODUCT_INFO'], 
                                    n_calls, p=[0.3, 0.2, 0.2, 0.2, 0.1]),
        'call_duration_minutes': np.random.exponential(8, n_calls),
        'resolution_time_hours': np.random.exponential(24, n_calls),
        'is_resolved': np.random.choice([0, 1], n_calls, p=[0.15, 0.85]),
        'customer_satisfaction_score': np.random.uniform(1, 5, n_calls),
        'escalation_level': np.random.choice([1, 2, 3], n_calls, p=[0.7, 0.25, 0.05]),
        'event_timestamp': timestamps
    }
    
    # Round scores and times
    data['customer_satisfaction_score'] = np.round(data['customer_satisfaction_score'], 1)
    data['call_duration_minutes'] = np.round(data['call_duration_minutes'], 1)
    data['resolution_time_hours'] = np.round(data['resolution_time_hours'], 1)
    
    return pd.DataFrame(data)

def main():
    """Generate all sample data files"""
    # Create data directory inside feature_repo
    os.makedirs('server_feature_repo/data', exist_ok=True)
    
    print("Generating customer data...")
    customer_df = generate_customer_data()
    customer_df.to_parquet('server_feature_repo/data/customers.parquet', index=False)
    
    print("Generating transaction data...")
    transaction_df = generate_transaction_data()
    transaction_df.to_parquet('server_feature_repo/data/transactions.parquet', index=False)
    
    print("Generating ATM usage data...")
    atm_df = generate_atm_usage_data()
    atm_df.to_parquet('server_feature_repo/data/atm_usage.parquet', index=False)
    
    print("Generating branch visit data...")
    branch_df = generate_branch_visit_data()
    branch_df.to_parquet('server_feature_repo/data/branch_visits.parquet', index=False)
    
    print("Generating call center data...")
    call_df = generate_call_center_data()
    call_df.to_parquet('server_feature_repo/data/call_center.parquet', index=False)
    
    print("Sample data generation completed!")
    print(f"Generated {len(customer_df)} customers")
    print(f"Generated {len(transaction_df)} transactions")
    print(f"Generated {len(atm_df)} ATM usage records")
    print(f"Generated {len(branch_df)} branch visits")
    print(f"Generated {len(call_df)} call center records")

if __name__ == "__main__":
    main()
