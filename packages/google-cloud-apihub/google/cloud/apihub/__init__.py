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
from google.cloud.apihub import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.apihub_v1.services.api_hub.async_client import ApiHubAsyncClient
from google.cloud.apihub_v1.services.api_hub.client import ApiHubClient
from google.cloud.apihub_v1.services.api_hub_dependencies.async_client import (
    ApiHubDependenciesAsyncClient,
)
from google.cloud.apihub_v1.services.api_hub_dependencies.client import (
    ApiHubDependenciesClient,
)
from google.cloud.apihub_v1.services.api_hub_plugin.async_client import (
    ApiHubPluginAsyncClient,
)
from google.cloud.apihub_v1.services.api_hub_plugin.client import ApiHubPluginClient
from google.cloud.apihub_v1.services.host_project_registration_service.async_client import (
    HostProjectRegistrationServiceAsyncClient,
)
from google.cloud.apihub_v1.services.host_project_registration_service.client import (
    HostProjectRegistrationServiceClient,
)
from google.cloud.apihub_v1.services.linting_service.async_client import (
    LintingServiceAsyncClient,
)
from google.cloud.apihub_v1.services.linting_service.client import LintingServiceClient
from google.cloud.apihub_v1.services.provisioning.async_client import (
    ProvisioningAsyncClient,
)
from google.cloud.apihub_v1.services.provisioning.client import ProvisioningClient
from google.cloud.apihub_v1.services.runtime_project_attachment_service.async_client import (
    RuntimeProjectAttachmentServiceAsyncClient,
)
from google.cloud.apihub_v1.services.runtime_project_attachment_service.client import (
    RuntimeProjectAttachmentServiceClient,
)
from google.cloud.apihub_v1.types.apihub_service import (
    ApiHubResource,
    CreateApiRequest,
    CreateAttributeRequest,
    CreateDependencyRequest,
    CreateDeploymentRequest,
    CreateExternalApiRequest,
    CreateSpecRequest,
    CreateVersionRequest,
    DeleteApiRequest,
    DeleteAttributeRequest,
    DeleteDependencyRequest,
    DeleteDeploymentRequest,
    DeleteExternalApiRequest,
    DeleteSpecRequest,
    DeleteVersionRequest,
    GetApiOperationRequest,
    GetApiRequest,
    GetAttributeRequest,
    GetDefinitionRequest,
    GetDependencyRequest,
    GetDeploymentRequest,
    GetExternalApiRequest,
    GetSpecContentsRequest,
    GetSpecRequest,
    GetVersionRequest,
    ListApiOperationsRequest,
    ListApiOperationsResponse,
    ListApisRequest,
    ListApisResponse,
    ListAttributesRequest,
    ListAttributesResponse,
    ListDependenciesRequest,
    ListDependenciesResponse,
    ListDeploymentsRequest,
    ListDeploymentsResponse,
    ListExternalApisRequest,
    ListExternalApisResponse,
    ListSpecsRequest,
    ListSpecsResponse,
    ListVersionsRequest,
    ListVersionsResponse,
    SearchResourcesRequest,
    SearchResourcesResponse,
    SearchResult,
    UpdateApiRequest,
    UpdateAttributeRequest,
    UpdateDependencyRequest,
    UpdateDeploymentRequest,
    UpdateExternalApiRequest,
    UpdateSpecRequest,
    UpdateVersionRequest,
)
from google.cloud.apihub_v1.types.common_fields import (
    Api,
    ApiHubInstance,
    ApiOperation,
    Attribute,
    AttributeValues,
    Definition,
    Dependency,
    DependencyEntityReference,
    DependencyErrorDetail,
    Deployment,
    Documentation,
    ExternalApi,
    HttpOperation,
    Issue,
    Linter,
    LintResponse,
    LintState,
    OpenApiSpecDetails,
    OperationDetails,
    OperationMetadata,
    Owner,
    Path,
    Point,
    Range,
    Schema,
    Severity,
    Spec,
    SpecContents,
    SpecDetails,
    Version,
)
from google.cloud.apihub_v1.types.host_project_registration_service import (
    CreateHostProjectRegistrationRequest,
    GetHostProjectRegistrationRequest,
    HostProjectRegistration,
    ListHostProjectRegistrationsRequest,
    ListHostProjectRegistrationsResponse,
)
from google.cloud.apihub_v1.types.linting_service import (
    GetStyleGuideContentsRequest,
    GetStyleGuideRequest,
    LintSpecRequest,
    StyleGuide,
    StyleGuideContents,
    UpdateStyleGuideRequest,
)
from google.cloud.apihub_v1.types.plugin_service import (
    DisablePluginRequest,
    EnablePluginRequest,
    GetPluginRequest,
    Plugin,
)
from google.cloud.apihub_v1.types.provisioning_service import (
    CreateApiHubInstanceRequest,
    GetApiHubInstanceRequest,
    LookupApiHubInstanceRequest,
    LookupApiHubInstanceResponse,
)
from google.cloud.apihub_v1.types.runtime_project_attachment_service import (
    CreateRuntimeProjectAttachmentRequest,
    DeleteRuntimeProjectAttachmentRequest,
    GetRuntimeProjectAttachmentRequest,
    ListRuntimeProjectAttachmentsRequest,
    ListRuntimeProjectAttachmentsResponse,
    LookupRuntimeProjectAttachmentRequest,
    LookupRuntimeProjectAttachmentResponse,
    RuntimeProjectAttachment,
)

__all__ = (
    "ApiHubClient",
    "ApiHubAsyncClient",
    "ApiHubDependenciesClient",
    "ApiHubDependenciesAsyncClient",
    "ApiHubPluginClient",
    "ApiHubPluginAsyncClient",
    "HostProjectRegistrationServiceClient",
    "HostProjectRegistrationServiceAsyncClient",
    "LintingServiceClient",
    "LintingServiceAsyncClient",
    "ProvisioningClient",
    "ProvisioningAsyncClient",
    "RuntimeProjectAttachmentServiceClient",
    "RuntimeProjectAttachmentServiceAsyncClient",
    "ApiHubResource",
    "CreateApiRequest",
    "CreateAttributeRequest",
    "CreateDependencyRequest",
    "CreateDeploymentRequest",
    "CreateExternalApiRequest",
    "CreateSpecRequest",
    "CreateVersionRequest",
    "DeleteApiRequest",
    "DeleteAttributeRequest",
    "DeleteDependencyRequest",
    "DeleteDeploymentRequest",
    "DeleteExternalApiRequest",
    "DeleteSpecRequest",
    "DeleteVersionRequest",
    "GetApiOperationRequest",
    "GetApiRequest",
    "GetAttributeRequest",
    "GetDefinitionRequest",
    "GetDependencyRequest",
    "GetDeploymentRequest",
    "GetExternalApiRequest",
    "GetSpecContentsRequest",
    "GetSpecRequest",
    "GetVersionRequest",
    "ListApiOperationsRequest",
    "ListApiOperationsResponse",
    "ListApisRequest",
    "ListApisResponse",
    "ListAttributesRequest",
    "ListAttributesResponse",
    "ListDependenciesRequest",
    "ListDependenciesResponse",
    "ListDeploymentsRequest",
    "ListDeploymentsResponse",
    "ListExternalApisRequest",
    "ListExternalApisResponse",
    "ListSpecsRequest",
    "ListSpecsResponse",
    "ListVersionsRequest",
    "ListVersionsResponse",
    "SearchResourcesRequest",
    "SearchResourcesResponse",
    "SearchResult",
    "UpdateApiRequest",
    "UpdateAttributeRequest",
    "UpdateDependencyRequest",
    "UpdateDeploymentRequest",
    "UpdateExternalApiRequest",
    "UpdateSpecRequest",
    "UpdateVersionRequest",
    "Api",
    "ApiHubInstance",
    "ApiOperation",
    "Attribute",
    "AttributeValues",
    "Definition",
    "Dependency",
    "DependencyEntityReference",
    "DependencyErrorDetail",
    "Deployment",
    "Documentation",
    "ExternalApi",
    "HttpOperation",
    "Issue",
    "LintResponse",
    "OpenApiSpecDetails",
    "OperationDetails",
    "OperationMetadata",
    "Owner",
    "Path",
    "Point",
    "Range",
    "Schema",
    "Spec",
    "SpecContents",
    "SpecDetails",
    "Version",
    "Linter",
    "LintState",
    "Severity",
    "CreateHostProjectRegistrationRequest",
    "GetHostProjectRegistrationRequest",
    "HostProjectRegistration",
    "ListHostProjectRegistrationsRequest",
    "ListHostProjectRegistrationsResponse",
    "GetStyleGuideContentsRequest",
    "GetStyleGuideRequest",
    "LintSpecRequest",
    "StyleGuide",
    "StyleGuideContents",
    "UpdateStyleGuideRequest",
    "DisablePluginRequest",
    "EnablePluginRequest",
    "GetPluginRequest",
    "Plugin",
    "CreateApiHubInstanceRequest",
    "GetApiHubInstanceRequest",
    "LookupApiHubInstanceRequest",
    "LookupApiHubInstanceResponse",
    "CreateRuntimeProjectAttachmentRequest",
    "DeleteRuntimeProjectAttachmentRequest",
    "GetRuntimeProjectAttachmentRequest",
    "ListRuntimeProjectAttachmentsRequest",
    "ListRuntimeProjectAttachmentsResponse",
    "LookupRuntimeProjectAttachmentRequest",
    "LookupRuntimeProjectAttachmentResponse",
    "RuntimeProjectAttachment",
)
