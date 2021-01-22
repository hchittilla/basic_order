# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
from config import DefaultConfig




CONFIG = DefaultConfig()
class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):

        app_id = CONFIG.LUIS_APP_ID
        # version_id = 0.1
        # region='westus'
        predictionEndpoint = f'https://{CONFIG.LUIS_API_HOST_NAME}/'
        luis_api_key = CONFIG.LUIS_API_KEY
        runtimeCredentials = CognitiveServicesCredentials(luis_api_key)
        clientRuntime = LUISRuntimeClient(endpoint=predictionEndpoint, credentials=runtimeCredentials)
        message = turn_context.activity.text
        predictionRequest = {"query": message}
        predictionResponse = clientRuntime.prediction.get_slot_prediction(app_id, "Production", predictionRequest)

        if predictionResponse.prediction.top_intent == 'order_status':
            await turn_context.send_activity("Sure, I can help with your order status")
        elif predictionResponse.prediction.top_intent == 'order_cancellation':
            await turn_context.send_activity("Please enter your orderid.")
        elif predictionResponse.prediction.top_intent == 'None':
            await turn_context.send_activity("switch to parent bot")
        elif predictionResponse.prediction.top_intent == 'order_tracking':
            await turn_context.send_activity("Sure, I can give your order tracking details")
        elif predictionResponse.prediction.top_intent == 'inform':
            if 'orderid' in predictionResponse.prediction.entities.keys():
                if str(predictionResponse.prediction.entities['orderid'][0]).lower() == 'od203820':
                    await turn_context.send_activity("Your order has been cancelled")
                else:
                    await turn_context.send_activity("Invalid order id")
        else:
            await turn_context.send_activity(
                "I couldn't really understand that, can you please rephrase.I am still learning!")

    async def on_members_added_activity(
            self,
            members_added: ChannelAccount,
            turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")



