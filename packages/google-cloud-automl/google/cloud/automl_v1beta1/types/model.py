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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.automl_v1beta1.types import image, tables, text, translation, video
from google.protobuf import timestamp_pb2  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.automl.v1beta1",
    manifest={
        "Model",
    },
)


class Model(proto.Message):
    r"""API proto representing a trained machine learning model.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        translation_model_metadata (google.cloud.automl_v1beta1.types.TranslationModelMetadata):
            Metadata for translation models.

            This field is a member of `oneof`_ ``model_metadata``.
        image_classification_model_metadata (google.cloud.automl_v1beta1.types.ImageClassificationModelMetadata):
            Metadata for image classification models.

            This field is a member of `oneof`_ ``model_metadata``.
        text_classification_model_metadata (google.cloud.automl_v1beta1.types.TextClassificationModelMetadata):
            Metadata for text classification models.

            This field is a member of `oneof`_ ``model_metadata``.
        image_object_detection_model_metadata (google.cloud.automl_v1beta1.types.ImageObjectDetectionModelMetadata):
            Metadata for image object detection models.

            This field is a member of `oneof`_ ``model_metadata``.
        video_classification_model_metadata (google.cloud.automl_v1beta1.types.VideoClassificationModelMetadata):
            Metadata for video classification models.

            This field is a member of `oneof`_ ``model_metadata``.
        video_object_tracking_model_metadata (google.cloud.automl_v1beta1.types.VideoObjectTrackingModelMetadata):
            Metadata for video object tracking models.

            This field is a member of `oneof`_ ``model_metadata``.
        text_extraction_model_metadata (google.cloud.automl_v1beta1.types.TextExtractionModelMetadata):
            Metadata for text extraction models.

            This field is a member of `oneof`_ ``model_metadata``.
        tables_model_metadata (google.cloud.automl_v1beta1.types.TablesModelMetadata):
            Metadata for Tables models.

            This field is a member of `oneof`_ ``model_metadata``.
        text_sentiment_model_metadata (google.cloud.automl_v1beta1.types.TextSentimentModelMetadata):
            Metadata for text sentiment models.

            This field is a member of `oneof`_ ``model_metadata``.
        name (str):
            Output only. Resource name of the model. Format:
            ``projects/{project_id}/locations/{location_id}/models/{model_id}``
        display_name (str):
            Required. The name of the model to show in the interface.
            The name can be up to 32 characters long and can consist
            only of ASCII Latin letters A-Z and a-z, underscores (_),
            and ASCII digits 0-9. It must start with a letter.
        dataset_id (str):
            Required. The resource ID of the dataset used
            to create the model. The dataset must come from
            the same ancestor project and location.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the model
            training finished  and can be used for
            prediction.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this model was
            last updated.
        deployment_state (google.cloud.automl_v1beta1.types.Model.DeploymentState):
            Output only. Deployment state of the model. A
            model can only serve prediction requests after
            it gets deployed.
    """

    class DeploymentState(proto.Enum):
        r"""Deployment state of the model.

        Values:
            DEPLOYMENT_STATE_UNSPECIFIED (0):
                Should not be used, an un-set enum has this
                value by default.
            DEPLOYED (1):
                Model is deployed.
            UNDEPLOYED (2):
                Model is not deployed.
        """
        DEPLOYMENT_STATE_UNSPECIFIED = 0
        DEPLOYED = 1
        UNDEPLOYED = 2

    translation_model_metadata: translation.TranslationModelMetadata = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="model_metadata",
        message=translation.TranslationModelMetadata,
    )
    image_classification_model_metadata: image.ImageClassificationModelMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=13,
            oneof="model_metadata",
            message=image.ImageClassificationModelMetadata,
        )
    )
    text_classification_model_metadata: text.TextClassificationModelMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=14,
            oneof="model_metadata",
            message=text.TextClassificationModelMetadata,
        )
    )
    image_object_detection_model_metadata: image.ImageObjectDetectionModelMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="model_metadata",
            message=image.ImageObjectDetectionModelMetadata,
        )
    )
    video_classification_model_metadata: video.VideoClassificationModelMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=23,
            oneof="model_metadata",
            message=video.VideoClassificationModelMetadata,
        )
    )
    video_object_tracking_model_metadata: video.VideoObjectTrackingModelMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=21,
            oneof="model_metadata",
            message=video.VideoObjectTrackingModelMetadata,
        )
    )
    text_extraction_model_metadata: text.TextExtractionModelMetadata = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="model_metadata",
        message=text.TextExtractionModelMetadata,
    )
    tables_model_metadata: tables.TablesModelMetadata = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="model_metadata",
        message=tables.TablesModelMetadata,
    )
    text_sentiment_model_metadata: text.TextSentimentModelMetadata = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="model_metadata",
        message=text.TextSentimentModelMetadata,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    deployment_state: DeploymentState = proto.Field(
        proto.ENUM,
        number=8,
        enum=DeploymentState,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
