# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.netapp import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.netapp_v1.services.net_app.async_client import NetAppAsyncClient
from google.cloud.netapp_v1.services.net_app.client import NetAppClient
from google.cloud.netapp_v1.types.active_directory import (
    ActiveDirectory,
    CreateActiveDirectoryRequest,
    DeleteActiveDirectoryRequest,
    GetActiveDirectoryRequest,
    ListActiveDirectoriesRequest,
    ListActiveDirectoriesResponse,
    UpdateActiveDirectoryRequest,
)
from google.cloud.netapp_v1.types.cloud_netapp_service import OperationMetadata
from google.cloud.netapp_v1.types.common import EncryptionType, ServiceLevel
from google.cloud.netapp_v1.types.kms import (
    CreateKmsConfigRequest,
    DeleteKmsConfigRequest,
    EncryptVolumesRequest,
    GetKmsConfigRequest,
    KmsConfig,
    ListKmsConfigsRequest,
    ListKmsConfigsResponse,
    UpdateKmsConfigRequest,
    VerifyKmsConfigRequest,
    VerifyKmsConfigResponse,
)
from google.cloud.netapp_v1.types.replication import (
    CreateReplicationRequest,
    DeleteReplicationRequest,
    DestinationVolumeParameters,
    GetReplicationRequest,
    ListReplicationsRequest,
    ListReplicationsResponse,
    Replication,
    ResumeReplicationRequest,
    ReverseReplicationDirectionRequest,
    StopReplicationRequest,
    TransferStats,
    UpdateReplicationRequest,
)
from google.cloud.netapp_v1.types.snapshot import (
    CreateSnapshotRequest,
    DeleteSnapshotRequest,
    GetSnapshotRequest,
    ListSnapshotsRequest,
    ListSnapshotsResponse,
    Snapshot,
    UpdateSnapshotRequest,
)
from google.cloud.netapp_v1.types.storage_pool import (
    CreateStoragePoolRequest,
    DeleteStoragePoolRequest,
    GetStoragePoolRequest,
    ListStoragePoolsRequest,
    ListStoragePoolsResponse,
    StoragePool,
    UpdateStoragePoolRequest,
)
from google.cloud.netapp_v1.types.volume import (
    AccessType,
    CreateVolumeRequest,
    DailySchedule,
    DeleteVolumeRequest,
    ExportPolicy,
    GetVolumeRequest,
    HourlySchedule,
    ListVolumesRequest,
    ListVolumesResponse,
    MonthlySchedule,
    MountOption,
    Protocols,
    RestoreParameters,
    RestrictedAction,
    RevertVolumeRequest,
    SecurityStyle,
    SimpleExportPolicyRule,
    SMBSettings,
    SnapshotPolicy,
    UpdateVolumeRequest,
    Volume,
    WeeklySchedule,
)

__all__ = (
    "NetAppClient",
    "NetAppAsyncClient",
    "ActiveDirectory",
    "CreateActiveDirectoryRequest",
    "DeleteActiveDirectoryRequest",
    "GetActiveDirectoryRequest",
    "ListActiveDirectoriesRequest",
    "ListActiveDirectoriesResponse",
    "UpdateActiveDirectoryRequest",
    "OperationMetadata",
    "EncryptionType",
    "ServiceLevel",
    "CreateKmsConfigRequest",
    "DeleteKmsConfigRequest",
    "EncryptVolumesRequest",
    "GetKmsConfigRequest",
    "KmsConfig",
    "ListKmsConfigsRequest",
    "ListKmsConfigsResponse",
    "UpdateKmsConfigRequest",
    "VerifyKmsConfigRequest",
    "VerifyKmsConfigResponse",
    "CreateReplicationRequest",
    "DeleteReplicationRequest",
    "DestinationVolumeParameters",
    "GetReplicationRequest",
    "ListReplicationsRequest",
    "ListReplicationsResponse",
    "Replication",
    "ResumeReplicationRequest",
    "ReverseReplicationDirectionRequest",
    "StopReplicationRequest",
    "TransferStats",
    "UpdateReplicationRequest",
    "CreateSnapshotRequest",
    "DeleteSnapshotRequest",
    "GetSnapshotRequest",
    "ListSnapshotsRequest",
    "ListSnapshotsResponse",
    "Snapshot",
    "UpdateSnapshotRequest",
    "CreateStoragePoolRequest",
    "DeleteStoragePoolRequest",
    "GetStoragePoolRequest",
    "ListStoragePoolsRequest",
    "ListStoragePoolsResponse",
    "StoragePool",
    "UpdateStoragePoolRequest",
    "CreateVolumeRequest",
    "DailySchedule",
    "DeleteVolumeRequest",
    "ExportPolicy",
    "GetVolumeRequest",
    "HourlySchedule",
    "ListVolumesRequest",
    "ListVolumesResponse",
    "MonthlySchedule",
    "MountOption",
    "RestoreParameters",
    "RevertVolumeRequest",
    "SimpleExportPolicyRule",
    "SnapshotPolicy",
    "UpdateVolumeRequest",
    "Volume",
    "WeeklySchedule",
    "AccessType",
    "Protocols",
    "RestrictedAction",
    "SecurityStyle",
    "SMBSettings",
)
