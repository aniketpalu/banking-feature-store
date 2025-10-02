# Banking Feature Store Permissions Configuration
# Demonstrates RBAC with groups and namespaces support (PR #5619 patterns)
# Simplified for easy understanding and testing

from feast.feast_object import ALL_RESOURCE_TYPES
from feast.permissions.action import READ, AuthzedAction, ALL_ACTIONS
from feast.permissions.permission import Permission
from feast.permissions.policy import (
    RoleBasedPolicy, 
    GroupBasedPolicy, 
    NamespaceBasedPolicy, 
    CombinedGroupNamespacePolicy
)

# Simple role definitions
admin_roles = ["banking-admin"]
analyst_roles = ["banking-analyst"]

# Simple group definitions
data_team_groups = ["data-team"]
risk_team_groups = ["risk-team"]

# Simple namespace definitions
prod_namespaces = ["production"]
staging_namespaces = ["staging"]

admin_perm = Permission(
    name="admin_permission",
    types=ALL_RESOURCE_TYPES,
    policy=RoleBasedPolicy(roles=admin_roles),
    actions=ALL_ACTIONS
)

data_team_perm = Permission(
    name="data_team_permission",
    types=ALL_RESOURCE_TYPES,
    policy=GroupBasedPolicy(groups=data_team_groups),
    actions=[AuthzedAction.DESCRIBE] + READ
)

prod_read_perm = Permission(
    name="production_read_permission",
    types=ALL_RESOURCE_TYPES,
    policy=NamespaceBasedPolicy(namespaces=prod_namespaces),
    actions=[AuthzedAction.DESCRIBE] + READ
)

risk_staging_perm = Permission(
    name="risk_staging_permission",
    types=ALL_RESOURCE_TYPES,
    policy=CombinedGroupNamespacePolicy(groups=risk_team_groups, namespaces=staging_namespaces),
    actions=ALL_ACTIONS
)

# Export permissions
permissions = [
    admin_perm,           # Role-based
    data_team_perm,       # Group-based  
    prod_read_perm,       # Namespace-based
    risk_staging_perm,   # Combined
]

# Simple summary
PERMISSION_SUMMARY = {
    "total_permissions": 4,
    "policy_types": ["RoleBasedPolicy", "GroupBasedPolicy", "NamespaceBasedPolicy", "CombinedGroupNamespacePolicy"],
    "roles": ["banking-admin", "banking-analyst"],
    "groups": ["data-team", "risk-team"],
    "namespaces": ["production", "staging"]
}
