# # Banking Feature Store Permissions Configuration
# # Demonstrates RBAC with groups and namespaces support (PR #5619 patterns)
# # Simplified for easy understanding and testing

from feast.feast_object import ALL_RESOURCE_TYPES, FeastObject
from feast.permissions.action import READ, AuthzedAction, ALL_ACTIONS
from feast.permissions.permission import Permission
from feast.permissions.policy import (
    GroupBasedPolicy,
    CombinedGroupNamespacePolicy
)

# # Simple group definitions
admin_groups = ["banking-admin"]
data_team_groups = ["data-engineers"]
ds_team_groups = ["ds-team"]

# # Simple namespace definitions
prod_namespaces = ["feast-eap"]
staging_namespaces = ["feast-staging"]


resource_types_without_permissions = [
    FeastObject.Project,
    FeastObject.FeatureView,
    FeastObject.OnDemandFeatureView,
    FeastObject.BatchFeatureView,
    FeastObject.StreamFeatureView,
    FeastObject.Entity,
    FeastObject.FeatureService,
    FeastObject.DataSource,
    FeastObject.ValidationReference,
    FeastObject.SavedDataset,
]

admin_perm = Permission(
    name="admin_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=GroupBasedPolicy(groups=admin_groups),
    actions=ALL_ACTIONS
)

data_team_perm = Permission(
    name="data_team_permissions",
    types=resource_types_without_permissions,
    policy=CombinedGroupNamespacePolicy(groups=data_team_groups, namespaces=prod_namespaces),
    actions=ALL_ACTIONS
)

ds_team_perm = Permission(
    name="ds_team_permissions",
    types=resource_types_without_permissions,
    policy=CombinedGroupNamespacePolicy(namespaces=staging_namespaces, groups=ds_team_groups),
    actions=[AuthzedAction.DESCRIBE] + READ
)


# # Export permissions
permissions = [
    admin_perm,
    data_team_perm,
    ds_team_perm,
]