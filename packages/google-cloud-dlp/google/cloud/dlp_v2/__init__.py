# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from google.cloud.dlp_v2 import gapic_version as package_version

__version__ = package_version.__version__


from .services.dlp_service import DlpServiceAsyncClient, DlpServiceClient
from .types.dlp import (
    Action,
    ActionDetails,
    ActivateJobTriggerRequest,
    AllOtherDatabaseResources,
    AnalyzeDataSourceRiskDetails,
    BigQueryDiscoveryTarget,
    BigQueryRegex,
    BigQueryRegexes,
    BigQuerySchemaModification,
    BigQueryTableCollection,
    BigQueryTableModification,
    BigQueryTableType,
    BigQueryTableTypeCollection,
    BigQueryTableTypes,
    BoundingBox,
    BucketingConfig,
    ByteContentItem,
    CancelDlpJobRequest,
    CharacterMaskConfig,
    CharsToIgnore,
    CloudSqlDiscoveryTarget,
    CloudSqlIamCredential,
    CloudSqlProperties,
    Color,
    ColumnDataProfile,
    Connection,
    ConnectionState,
    Container,
    ContentItem,
    ContentLocation,
    ContentOption,
    CreateConnectionRequest,
    CreateDeidentifyTemplateRequest,
    CreateDiscoveryConfigRequest,
    CreateDlpJobRequest,
    CreateInspectTemplateRequest,
    CreateJobTriggerRequest,
    CreateStoredInfoTypeRequest,
    CryptoDeterministicConfig,
    CryptoHashConfig,
    CryptoKey,
    CryptoReplaceFfxFpeConfig,
    DatabaseResourceCollection,
    DatabaseResourceReference,
    DatabaseResourceRegex,
    DatabaseResourceRegexes,
    DataProfileAction,
    DataProfileBigQueryRowSchema,
    DataProfileConfigSnapshot,
    DataProfileJobConfig,
    DataProfileLocation,
    DataProfilePubSubCondition,
    DataProfilePubSubMessage,
    DataProfileUpdateFrequency,
    DataRiskLevel,
    DataSourceType,
    DateShiftConfig,
    DateTime,
    DeidentifyConfig,
    DeidentifyContentRequest,
    DeidentifyContentResponse,
    DeidentifyDataSourceDetails,
    DeidentifyDataSourceStats,
    DeidentifyTemplate,
    DeleteConnectionRequest,
    DeleteDeidentifyTemplateRequest,
    DeleteDiscoveryConfigRequest,
    DeleteDlpJobRequest,
    DeleteInspectTemplateRequest,
    DeleteJobTriggerRequest,
    DeleteStoredInfoTypeRequest,
    DeleteTableDataProfileRequest,
    Disabled,
    DiscoveryBigQueryConditions,
    DiscoveryBigQueryFilter,
    DiscoveryCloudSqlConditions,
    DiscoveryCloudSqlFilter,
    DiscoveryCloudSqlGenerationCadence,
    DiscoveryConfig,
    DiscoveryGenerationCadence,
    DiscoverySchemaModifiedCadence,
    DiscoveryStartingLocation,
    DiscoveryTableModifiedCadence,
    DiscoveryTarget,
    DlpJob,
    DlpJobType,
    DocumentLocation,
    EncryptionStatus,
    Error,
    ExcludeByHotword,
    ExcludeInfoTypes,
    ExclusionRule,
    FieldTransformation,
    Finding,
    FinishDlpJobRequest,
    FixedSizeBucketingConfig,
    GetColumnDataProfileRequest,
    GetConnectionRequest,
    GetDeidentifyTemplateRequest,
    GetDiscoveryConfigRequest,
    GetDlpJobRequest,
    GetInspectTemplateRequest,
    GetJobTriggerRequest,
    GetProjectDataProfileRequest,
    GetStoredInfoTypeRequest,
    GetTableDataProfileRequest,
    HybridContentItem,
    HybridFindingDetails,
    HybridInspectDlpJobRequest,
    HybridInspectJobTriggerRequest,
    HybridInspectResponse,
    HybridInspectStatistics,
    ImageLocation,
    ImageTransformations,
    InfoTypeCategory,
    InfoTypeDescription,
    InfoTypeStats,
    InfoTypeSummary,
    InfoTypeSupportedBy,
    InfoTypeTransformations,
    InspectConfig,
    InspectContentRequest,
    InspectContentResponse,
    InspectDataSourceDetails,
    InspectionRule,
    InspectionRuleSet,
    InspectJobConfig,
    InspectResult,
    InspectTemplate,
    JobTrigger,
    KmsWrappedCryptoKey,
    LargeCustomDictionaryConfig,
    LargeCustomDictionaryStats,
    ListColumnDataProfilesRequest,
    ListColumnDataProfilesResponse,
    ListConnectionsRequest,
    ListConnectionsResponse,
    ListDeidentifyTemplatesRequest,
    ListDeidentifyTemplatesResponse,
    ListDiscoveryConfigsRequest,
    ListDiscoveryConfigsResponse,
    ListDlpJobsRequest,
    ListDlpJobsResponse,
    ListInfoTypesRequest,
    ListInfoTypesResponse,
    ListInspectTemplatesRequest,
    ListInspectTemplatesResponse,
    ListJobTriggersRequest,
    ListJobTriggersResponse,
    ListProjectDataProfilesRequest,
    ListProjectDataProfilesResponse,
    ListStoredInfoTypesRequest,
    ListStoredInfoTypesResponse,
    ListTableDataProfilesRequest,
    ListTableDataProfilesResponse,
    Location,
    Manual,
    MatchingType,
    MetadataLocation,
    MetadataType,
    NullPercentageLevel,
    OtherInfoTypeSummary,
    OutputStorageConfig,
    PrimitiveTransformation,
    PrivacyMetric,
    ProfileStatus,
    ProjectDataProfile,
    QuasiId,
    QuoteInfo,
    Range,
    RecordCondition,
    RecordLocation,
    RecordSuppression,
    RecordTransformation,
    RecordTransformations,
    RedactConfig,
    RedactImageRequest,
    RedactImageResponse,
    ReidentifyContentRequest,
    ReidentifyContentResponse,
    RelationalOperator,
    ReplaceDictionaryConfig,
    ReplaceValueConfig,
    ReplaceWithInfoTypeConfig,
    ResourceVisibility,
    RiskAnalysisJobConfig,
    Schedule,
    SearchConnectionsRequest,
    SearchConnectionsResponse,
    SecretManagerCredential,
    SecretsDiscoveryTarget,
    StatisticalTable,
    StorageMetadataLabel,
    StoredInfoType,
    StoredInfoTypeConfig,
    StoredInfoTypeState,
    StoredInfoTypeStats,
    StoredInfoTypeVersion,
    Table,
    TableDataProfile,
    TableLocation,
    TimePartConfig,
    TransformationConfig,
    TransformationContainerType,
    TransformationDescription,
    TransformationDetails,
    TransformationDetailsStorageConfig,
    TransformationErrorHandling,
    TransformationLocation,
    TransformationOverview,
    TransformationResultStatus,
    TransformationResultStatusType,
    TransformationSummary,
    TransformationType,
    TransientCryptoKey,
    UniquenessScoreLevel,
    UnwrappedCryptoKey,
    UpdateConnectionRequest,
    UpdateDeidentifyTemplateRequest,
    UpdateDiscoveryConfigRequest,
    UpdateInspectTemplateRequest,
    UpdateJobTriggerRequest,
    UpdateStoredInfoTypeRequest,
    Value,
    ValueFrequency,
    VersionDescription,
)
from .types.storage import (
    BigQueryField,
    BigQueryKey,
    BigQueryOptions,
    BigQueryTable,
    CloudStorageFileSet,
    CloudStorageOptions,
    CloudStoragePath,
    CloudStorageRegexFileSet,
    CustomInfoType,
    DatastoreKey,
    DatastoreOptions,
    EntityId,
    FieldId,
    FileType,
    HybridOptions,
    InfoType,
    Key,
    KindExpression,
    Likelihood,
    PartitionId,
    RecordKey,
    SensitivityScore,
    StorageConfig,
    StoredType,
    TableOptions,
    TableReference,
)

__all__ = (
    "DlpServiceAsyncClient",
    "Action",
    "ActionDetails",
    "ActivateJobTriggerRequest",
    "AllOtherDatabaseResources",
    "AnalyzeDataSourceRiskDetails",
    "BigQueryDiscoveryTarget",
    "BigQueryField",
    "BigQueryKey",
    "BigQueryOptions",
    "BigQueryRegex",
    "BigQueryRegexes",
    "BigQuerySchemaModification",
    "BigQueryTable",
    "BigQueryTableCollection",
    "BigQueryTableModification",
    "BigQueryTableType",
    "BigQueryTableTypeCollection",
    "BigQueryTableTypes",
    "BoundingBox",
    "BucketingConfig",
    "ByteContentItem",
    "CancelDlpJobRequest",
    "CharacterMaskConfig",
    "CharsToIgnore",
    "CloudSqlDiscoveryTarget",
    "CloudSqlIamCredential",
    "CloudSqlProperties",
    "CloudStorageFileSet",
    "CloudStorageOptions",
    "CloudStoragePath",
    "CloudStorageRegexFileSet",
    "Color",
    "ColumnDataProfile",
    "Connection",
    "ConnectionState",
    "Container",
    "ContentItem",
    "ContentLocation",
    "ContentOption",
    "CreateConnectionRequest",
    "CreateDeidentifyTemplateRequest",
    "CreateDiscoveryConfigRequest",
    "CreateDlpJobRequest",
    "CreateInspectTemplateRequest",
    "CreateJobTriggerRequest",
    "CreateStoredInfoTypeRequest",
    "CryptoDeterministicConfig",
    "CryptoHashConfig",
    "CryptoKey",
    "CryptoReplaceFfxFpeConfig",
    "CustomInfoType",
    "DataProfileAction",
    "DataProfileBigQueryRowSchema",
    "DataProfileConfigSnapshot",
    "DataProfileJobConfig",
    "DataProfileLocation",
    "DataProfilePubSubCondition",
    "DataProfilePubSubMessage",
    "DataProfileUpdateFrequency",
    "DataRiskLevel",
    "DataSourceType",
    "DatabaseResourceCollection",
    "DatabaseResourceReference",
    "DatabaseResourceRegex",
    "DatabaseResourceRegexes",
    "DatastoreKey",
    "DatastoreOptions",
    "DateShiftConfig",
    "DateTime",
    "DeidentifyConfig",
    "DeidentifyContentRequest",
    "DeidentifyContentResponse",
    "DeidentifyDataSourceDetails",
    "DeidentifyDataSourceStats",
    "DeidentifyTemplate",
    "DeleteConnectionRequest",
    "DeleteDeidentifyTemplateRequest",
    "DeleteDiscoveryConfigRequest",
    "DeleteDlpJobRequest",
    "DeleteInspectTemplateRequest",
    "DeleteJobTriggerRequest",
    "DeleteStoredInfoTypeRequest",
    "DeleteTableDataProfileRequest",
    "Disabled",
    "DiscoveryBigQueryConditions",
    "DiscoveryBigQueryFilter",
    "DiscoveryCloudSqlConditions",
    "DiscoveryCloudSqlFilter",
    "DiscoveryCloudSqlGenerationCadence",
    "DiscoveryConfig",
    "DiscoveryGenerationCadence",
    "DiscoverySchemaModifiedCadence",
    "DiscoveryStartingLocation",
    "DiscoveryTableModifiedCadence",
    "DiscoveryTarget",
    "DlpJob",
    "DlpJobType",
    "DlpServiceClient",
    "DocumentLocation",
    "EncryptionStatus",
    "EntityId",
    "Error",
    "ExcludeByHotword",
    "ExcludeInfoTypes",
    "ExclusionRule",
    "FieldId",
    "FieldTransformation",
    "FileType",
    "Finding",
    "FinishDlpJobRequest",
    "FixedSizeBucketingConfig",
    "GetColumnDataProfileRequest",
    "GetConnectionRequest",
    "GetDeidentifyTemplateRequest",
    "GetDiscoveryConfigRequest",
    "GetDlpJobRequest",
    "GetInspectTemplateRequest",
    "GetJobTriggerRequest",
    "GetProjectDataProfileRequest",
    "GetStoredInfoTypeRequest",
    "GetTableDataProfileRequest",
    "HybridContentItem",
    "HybridFindingDetails",
    "HybridInspectDlpJobRequest",
    "HybridInspectJobTriggerRequest",
    "HybridInspectResponse",
    "HybridInspectStatistics",
    "HybridOptions",
    "ImageLocation",
    "ImageTransformations",
    "InfoType",
    "InfoTypeCategory",
    "InfoTypeDescription",
    "InfoTypeStats",
    "InfoTypeSummary",
    "InfoTypeSupportedBy",
    "InfoTypeTransformations",
    "InspectConfig",
    "InspectContentRequest",
    "InspectContentResponse",
    "InspectDataSourceDetails",
    "InspectJobConfig",
    "InspectResult",
    "InspectTemplate",
    "InspectionRule",
    "InspectionRuleSet",
    "JobTrigger",
    "Key",
    "KindExpression",
    "KmsWrappedCryptoKey",
    "LargeCustomDictionaryConfig",
    "LargeCustomDictionaryStats",
    "Likelihood",
    "ListColumnDataProfilesRequest",
    "ListColumnDataProfilesResponse",
    "ListConnectionsRequest",
    "ListConnectionsResponse",
    "ListDeidentifyTemplatesRequest",
    "ListDeidentifyTemplatesResponse",
    "ListDiscoveryConfigsRequest",
    "ListDiscoveryConfigsResponse",
    "ListDlpJobsRequest",
    "ListDlpJobsResponse",
    "ListInfoTypesRequest",
    "ListInfoTypesResponse",
    "ListInspectTemplatesRequest",
    "ListInspectTemplatesResponse",
    "ListJobTriggersRequest",
    "ListJobTriggersResponse",
    "ListProjectDataProfilesRequest",
    "ListProjectDataProfilesResponse",
    "ListStoredInfoTypesRequest",
    "ListStoredInfoTypesResponse",
    "ListTableDataProfilesRequest",
    "ListTableDataProfilesResponse",
    "Location",
    "Manual",
    "MatchingType",
    "MetadataLocation",
    "MetadataType",
    "NullPercentageLevel",
    "OtherInfoTypeSummary",
    "OutputStorageConfig",
    "PartitionId",
    "PrimitiveTransformation",
    "PrivacyMetric",
    "ProfileStatus",
    "ProjectDataProfile",
    "QuasiId",
    "QuoteInfo",
    "Range",
    "RecordCondition",
    "RecordKey",
    "RecordLocation",
    "RecordSuppression",
    "RecordTransformation",
    "RecordTransformations",
    "RedactConfig",
    "RedactImageRequest",
    "RedactImageResponse",
    "ReidentifyContentRequest",
    "ReidentifyContentResponse",
    "RelationalOperator",
    "ReplaceDictionaryConfig",
    "ReplaceValueConfig",
    "ReplaceWithInfoTypeConfig",
    "ResourceVisibility",
    "RiskAnalysisJobConfig",
    "Schedule",
    "SearchConnectionsRequest",
    "SearchConnectionsResponse",
    "SecretManagerCredential",
    "SecretsDiscoveryTarget",
    "SensitivityScore",
    "StatisticalTable",
    "StorageConfig",
    "StorageMetadataLabel",
    "StoredInfoType",
    "StoredInfoTypeConfig",
    "StoredInfoTypeState",
    "StoredInfoTypeStats",
    "StoredInfoTypeVersion",
    "StoredType",
    "Table",
    "TableDataProfile",
    "TableLocation",
    "TableOptions",
    "TableReference",
    "TimePartConfig",
    "TransformationConfig",
    "TransformationContainerType",
    "TransformationDescription",
    "TransformationDetails",
    "TransformationDetailsStorageConfig",
    "TransformationErrorHandling",
    "TransformationLocation",
    "TransformationOverview",
    "TransformationResultStatus",
    "TransformationResultStatusType",
    "TransformationSummary",
    "TransformationType",
    "TransientCryptoKey",
    "UniquenessScoreLevel",
    "UnwrappedCryptoKey",
    "UpdateConnectionRequest",
    "UpdateDeidentifyTemplateRequest",
    "UpdateDiscoveryConfigRequest",
    "UpdateInspectTemplateRequest",
    "UpdateJobTriggerRequest",
    "UpdateStoredInfoTypeRequest",
    "Value",
    "ValueFrequency",
    "VersionDescription",
)
