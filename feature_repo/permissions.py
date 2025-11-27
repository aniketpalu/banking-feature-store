# Banking Feature Store Permissions Configuration
# Demonstrates RBAC with groups and namespaces support
# Uses CombinedGroupNamespacePolicy with namespace 'feast' for all permissions

from feast.feast_object import ALL_RESOURCE_TYPES
from feast.permissions.action import READ, AuthzedAction, ALL_ACTIONS
from feast.permissions.permission import Permission
from feast.permissions.policy import CombinedGroupNamespacePolicy
from feast.project import Project
from feast.data_source import DataSource
from feast.entity import Entity
from feast.feature_service import FeatureService
from feast.feature_view import FeatureView
from feast.on_demand_feature_view import OnDemandFeatureView
from feast.saved_dataset import SavedDataset

# Group definitions
admin_groups = ["banking-admin"]
data_engineers_groups = ["data-engineers"]
data_scientists_groups = ["data-scientists"]
read_only_analysts_groups = ["read-only-analysts"]
restricted_user_groups = ["restricted-user"]

# Namespace - always 'feast' for production
namespace = ["feast"]

# Resource types for feature store operations
resource_types = [
    Project,
    FeatureView,
    OnDemandFeatureView,
    Entity,
    FeatureService,
    DataSource,
    SavedDataset,
]

# ============================================================================
# Permission Definitions
# ============================================================================

# 1. Admin Permissions - Full access to everything
admin_perm = Permission(
    name="admin_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=CombinedGroupNamespacePolicy(groups=admin_groups, namespaces=namespace),
    actions=ALL_ACTIONS
)

# 2. Data Engineers Permissions - Can create/modify features and read/write data
data_engineers_perm = Permission(
    name="data_engineers_permissions",
    types=resource_types,
    policy=CombinedGroupNamespacePolicy(groups=data_engineers_groups, namespaces=namespace),
    actions=[
        AuthzedAction.CREATE,
        AuthzedAction.UPDATE,
        AuthzedAction.DELETE,
        AuthzedAction.DESCRIBE,
        AuthzedAction.READ_OFFLINE,
        AuthzedAction.READ_ONLINE,
        AuthzedAction.WRITE_OFFLINE,
        AuthzedAction.WRITE_ONLINE,
    ]
)

# 3. Data Scientists Permissions - Can read features for ML models (no write access)
data_scientists_perm = Permission(
    name="data_scientists_permissions",
    types=[FeatureView, FeatureService, Entity],
    policy=CombinedGroupNamespacePolicy(groups=data_scientists_groups, namespaces=namespace),
    actions=[
        AuthzedAction.DESCRIBE,
        AuthzedAction.READ_OFFLINE,
        AuthzedAction.READ_ONLINE,
    ]
)

# 4. Read-Only Analysts Permissions - Can only read historical features (no online access)
read_only_analysts_perm = Permission(
    name="read_only_analysts_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=CombinedGroupNamespacePolicy(groups=read_only_analysts_groups, namespaces=namespace),
    actions=[
        AuthzedAction.DESCRIBE,
        AuthzedAction.READ_OFFLINE,
    ]
)

# 5. Restricted User Permissions - Can only list feature views
restricted_user_perm = Permission(
    name="restricted_user_permissions",
    types=[FeatureView],
    policy=CombinedGroupNamespacePolicy(groups=restricted_user_groups, namespaces=namespace),
    actions=[
        AuthzedAction.DESCRIBE,
    ]
)

# ============================================================================
# Export permissions list
# ============================================================================

permissions = [
    admin_perm,
    data_engineers_perm,
    data_scientists_perm,
    read_only_analysts_perm,
    restricted_user_perm,
]
