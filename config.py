#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os




class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "88d2fb24-5854-4790-aea0-15a47ef6c30a")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "AtLeastSixteenCharacters_0")
    LUIS_APP_ID = "25a9586a-daa4-437f-b3ab-b347d3f1f467"
    LUIS_API_KEY = "21b55404c0ea4531981fbd9865de699b"
    LUIS_API_HOST_NAME = "westus.api.cognitive.microsoft.com"
