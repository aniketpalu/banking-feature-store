# # Banking Feature Store Permissions Configuration
# # Demonstrates RBAC with groups and namespaces support (PR #5619 patterns)
# # Simplified for easy understanding and testing

from feast.feast_object import ALL_RESOURCE_TYPES
from feast.permissions.action import READ, AuthzedAction, ALL_ACTIONS
from feast.permissions.permission import Permission
from feast.permissions.policy import (
    GroupBasedPolicy, 
    NamespaceBasedPolicy, 
    CombinedGroupNamespacePolicy
)

# # Simple group definitions
admin_groups = ["banking-admin"]
data_team_groups = ["data-engineers"]
ds_team_groups = ["ds-team"]

# # Simple namespace definitions
prod_namespaces = ["feast-eap"]
staging_namespaces = ["feast-staging"]

admin_perm = Permission(
    name="admin_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=GroupBasedPolicy(groups=admin_groups),
    actions=ALL_ACTIONS
)

data_team_perm = Permission(
    name="data_team_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=CombinedGroupNamespacePolicy(groups=data_team_groups, namespaces=prod_namespaces),
    actions=ALL_ACTIONS
)

ds_team_perm = Permission(
    name="ds_team_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=CombinedGroupNamespacePolicy(namespaces=staging_namespaces, groups=ds_team_groups),
    actions=[AuthzedAction.DESCRIBE] + READ
)


# # Export permissions
permissions = [
    admin_perm,
    data_team_perm,
    ds_team_perm,
]