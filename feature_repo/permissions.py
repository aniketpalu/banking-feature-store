# # Banking Feature Store Permissions Configuration
# # Demonstrates RBAC with groups and namespaces support (PR #5619 patterns)
# # Simplified for easy understanding and testing

from feast.feast_object import ALL_RESOURCE_TYPES, FeastObject
from feast.permissions.action import READ, AuthzedAction, ALL_ACTIONS
from feast.permissions.permission import Permission
from feast.permissions.policy import (
    GroupBasedPolicy,
    CombinedGroupNamespacePolicy,
    NamespaceBasedPolicy
)
from feast.project import Project
from feast.data_source import DataSource
from feast.entity import Entity
from feast.feature_service import FeatureService
from feast.feature_view import FeatureView
from feast.on_demand_feature_view import OnDemandFeatureView
from feast.permissions.permission import Permission
from feast.saved_dataset import SavedDataset

# # Simple group definitions
admin_groups = ["banking-admin"]
data_team_groups = ["data-engineers"]
ds_team_groups = ["ds-team"]

# # Simple namespace definitions
prod_namespaces = ["feast"]
staging_namespaces = ["feast-staging"]


resource_types_without_permissions = [
    Project,
    FeatureView,
    OnDemandFeatureView,
    Entity,
    FeatureService,
    DataSource,
    SavedDataset,
]

admin_perm = Permission(
    name="admin_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=NamespaceBasedPolicy(namespaces=prod_namespaces),
    actions=ALL_ACTIONS
)

# data_team_perm = Permission(
#     name="data_team_permissions",
#     types=resource_types_without_permissions,
#     policy=CombinedGroupNamespacePolicy(groups=data_team_groups, namespaces=prod_namespaces),
#     actions=ALL_ACTIONS
# )

# ds_team_perm = Permission(
#     name="ds_team_permissions",
#     types=resource_types_without_permissions,
#     policy=CombinedGroupNamespacePolicy(namespaces=staging_namespaces, groups=ds_team_groups),
#     actions=[AuthzedAction.DESCRIBE] + READ
# )
