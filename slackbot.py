##import logging
##logging.basicConfig(level=logging.DEBUG)
##
##import os
##from slack_sdk import WebClient
##from slack_sdk.errors import SlackApiError
##
##slack_token = os.environ["SLACK_BOT_TOKEN"]
##client = WebClient(token=slack_token)
##
##try:
##    response = client.chat_postMessage(
##        channel="C051X1DNTGS",
##        text="Hello from your app! :tada:"
##        
##    )
##except SlackApiError as e:
##    # You will get a SlackApiError if "ok" is False
##    assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'


import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Add functionality here

if __name__ == "__main__":
    # Create an app-level token with connections:write scope
    handler = SocketModeHandler(app, "xapp-1-A051WT32UR1-5078512640561-55fb840edcb63d0d7d329e1ab5eb3eb3b977ad00178579aa836186e00ac2783e")
    handler.start()
