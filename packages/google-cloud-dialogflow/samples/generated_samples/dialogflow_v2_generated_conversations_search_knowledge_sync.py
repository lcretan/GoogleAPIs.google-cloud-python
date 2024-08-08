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
# Generated code. DO NOT EDIT!
#
# Snippet for SearchKnowledge
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_v2_generated_Conversations_SearchKnowledge_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import dialogflow_v2


def sample_search_knowledge():
    # Create a client
    client = dialogflow_v2.ConversationsClient()

    # Initialize request argument(s)
    query = dialogflow_v2.TextInput()
    query.text = "text_value"
    query.language_code = "language_code_value"

    request = dialogflow_v2.SearchKnowledgeRequest(
        parent="parent_value",
        query=query,
        conversation_profile="conversation_profile_value",
        session_id="session_id_value",
    )

    # Make the request
    response = client.search_knowledge(request=request)

    # Handle the response
    print(response)

# [END dialogflow_v2_generated_Conversations_SearchKnowledge_sync]
