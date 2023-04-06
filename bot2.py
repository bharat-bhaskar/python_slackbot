import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
#app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
app = App(token="xoxb-5088721137360-5062274830501-zZcxY7WwmqFY3pvsqcjwJVxe")


# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html

##@app.message("hello")
##def message_hello(message, say):
##    # say() sends a message to the channel where the event was triggered
##    say(f"Hey there <@{message['user']}>!")

@app.event("message")
def handle_message_events(body):
    print(body)

# Start your app
if __name__ == "__main__":
    #SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    SocketModeHandler(app, "xapp-1-A051WT32UR1-5078512640561-55fb840edcb63d0d7d329e1ab5eb3eb3b977ad00178579aa836186e00ac2783e").start()
