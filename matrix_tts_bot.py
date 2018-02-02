from subprocess import call
import os
import uuid

from matrix_bot_api.matrix_bot_api import MatrixBotAPI
from matrix_bot_api.mcommand_handler import MCommandHandler
import yaml


bot = None
config = yaml.load(open("config.yaml"))


def say_callback(room, event):
    args = event['content']['body'].split()
    args.pop(0)
    args.pop(0)
    phrase_to_say = ' '.join(args)
    print("Say command received:")
    print("    Room name: " + room.name)
    print("    Phrase to say: " + phrase_to_say)
    file_path = "/tmp/" + config["name"] + "-" + uuid.uuid4().hex + ".wav"
    call(["espeak", "-p 0", "-s 1", "-w " + file_path, phrase_to_say])
    f = open(file_path, "rb")
    f_duration = 0 # We can get away with this until further notice.
    f_bytes = f.read()
    f.close()
    os.remove(file_path)
    print("    WAV file saved, read, and removed. Uploading to homeserver.")
    content_uri = bot.client.upload(f_bytes, "audio/x-wav")
    print("    Upload complete. Sending event to room.")
    room.send_audio(
        content_uri,
        config["name"] + ".wav",
        duration=f_duration,
        mimetype="audio/x-wav",
        size=len(f_bytes)
    )
    print("    Event sent.")


def main():
    global bot
    global config

    bot = MatrixBotAPI(config['username'], config['password'], config['homeserver_url'])

    say_handler = MCommandHandler(config["name"].lower() + " say", say_callback)
    bot.add_handler(say_handler)

    bot.start_polling()

    print(config["name"] + " has initialized. Listening for commands.")

    while True:
        input()


if __name__ == "__main__":
    main()
