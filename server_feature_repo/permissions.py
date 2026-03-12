from feast.feast_object import ALL_RESOURCE_TYPES
from feast.permissions.action import READ, AuthzedAction, ALL_ACTIONS
from feast.permissions.permission import Permission
from feast.permissions.policy import GroupBasedPolicy, NamespaceBasedPolicy
from feast.project import Project
from feast.data_source import DataSource
from feast.entity import Entity
from feast.feature_service import FeatureService
from feast.feature_view import FeatureView
from feast.on_demand_feature_view import OnDemandFeatureView
from feast.saved_dataset import SavedDataset

# OIDC group definitions (Keycloak groups)
admin_groups = ["feast-admins"]
data_engineers_groups = ["feast-data-engineer"]
data_scientists_groups = ["feast-data-scientists"]
restricted_user_groups = ["feast-restricted-group"]

# Namespace - only allow feast namespace for workbench pod access
namespace = ["feast"]

# Resource types for data engineers (excludes DataSource)
data_engineers_resource_types = [
    Project,
    FeatureView,
    OnDemandFeatureView,
    Entity,
    FeatureService,
    SavedDataset,
]

# ============================================================================
# Permission Definitions
# ============================================================================

# 1. Admin Permissions - Full access to everything
admin_perm = Permission(
    name="admin_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=GroupBasedPolicy(groups=admin_groups),
    actions=ALL_ACTIONS
)

# 2. Data Engineers Permissions - Can create/modify features and read/write data
# Access to everything BUT data sources
data_engineers_perm = Permission(
    name="data_engineers_permissions",
    types=data_engineers_resource_types,
    policy=GroupBasedPolicy(groups=data_engineers_groups),
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
# No access to DataSource, no access to transaction-related feature views
data_scientists_perm = Permission(
    name="data_scientists_permissions",
    types=[FeatureView, FeatureService, Entity, Project],
    name_patterns=["^(?!.*transaction).*"],
    policy=GroupBasedPolicy(groups=data_scientists_groups),
    actions=[
        AuthzedAction.DESCRIBE,
        AuthzedAction.READ_OFFLINE,
        AuthzedAction.READ_ONLINE,
    ]
)

# 4. Restricted User Permissions - Can only list feature views
restricted_user_perm = Permission(
    name="restricted_user_permissions",
    types=[FeatureView, Project],
    policy=GroupBasedPolicy(groups=restricted_user_groups),
    actions=[
        AuthzedAction.DESCRIBE,
    ]
)

# 5. Namespace-based Permissions - Allows workbench pods in feast namespace
# Workbench pods authenticate via K8s SA token, namespace extracted by KubernetesTokenParser
feast_namespace_perm = Permission(
    name="feast_namespace_permissions",
    types=ALL_RESOURCE_TYPES,
    policy=NamespaceBasedPolicy(namespaces=namespace),
    actions=ALL_ACTIONS,
)

# ============================================================================
# Export permissions list
# ============================================================================

permissions = [
    admin_perm,
    data_engineers_perm,
    data_scientists_perm,
    restricted_user_perm,
    feast_namespace_perm,
]
