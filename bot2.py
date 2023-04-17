import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re
from wb import update_facebook_status
# Initializes your app with your bot token and socket mode handler
#app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
app = App(token="xoxb-5088721137360-5062274830501-uget8C6DgVDBB6JG5VqrWNt7")


# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html

@app.message("#writefacebookstatus")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    msg_txt = message["text"]
    status_txt = re.findall("status:(.*)", msg_txt)[0]
    print(status_txt)
    login_facebook(status_txt)
    say(f"Hey there <@{message['user']}>! , facebook status has been updated.")

def login_facebook(status_text):
    update_facebook_status(status_text)


# Start your app
if __name__ == "__main__":
    #SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    SocketModeHandler(app, "xapp-1-A051WT32UR1-5056008578727-60d6a59da18b4314005de3e5e5d2760b320faf19231ff31bb7cb2023f3a8a583").start()
