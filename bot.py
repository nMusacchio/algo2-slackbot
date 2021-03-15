import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']


@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    if not user_id == BOT_ID and "windows" in text.lower():
        ts = event.get('ts')
        client.chat_postMessage(channel=channel_id, thread_ts = ts, text="No respondemos consultas sobre Windows :no_entry: \n Lo aclaramos la primera clase: https://docs.google.com/presentation/d/1CoK6dhq9vM68Ugk67HaY5AxDebD1s6RZDxvyOJxABqQ/edit#slide=id.g6cabada2a4_0_61")

if __name__ == "__main__":
    app.run(debug=True)