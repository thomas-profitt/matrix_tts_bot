# matrix\_tts\_bot

This is a super-simple text-to-speech bot for Matrix using espeak. It is useful as an example of a simple Matrix bot and as a source of amusement.

When the bot is told to "say" a phrase, it generates a temporary WAV file and uploads it to the Matrix room to be played (in Matrix clients that show the audio inline) or downloaded as a file.

## Configuring and Running the Bot

1. Create a Matrix account for your bot
2. Enter the account's credentials into _config.yaml_ (see _config.yaml.example_)
3. Check if your machine has `espeak` installed with `which espeak`. If it is missing (e.g. you are a macOS heathen), either install it from your package manager (or, in the case of macOS, one of your package managers) or replace the call to `espeak` in *matrix_tts_bot.py* with a call to another text-to-speech command, like macOS' `say`.
4. Install dependencies with `pip3 install -r requirements.txt`
5. Run your TTS bot with `./matrix_tts_bot`
6. Wait for the bot to initialize and log in.
7. In a room with the bot, give it a spin by sending "!BOT_NAME say Hello, world!", where "BOT_NAME" is "name" in your _config.yaml_

## Known Issues and Limitations
- The bot is not compatible with E2E-encrypted rooms. It can't read commands in E2E encrypted rooms, uploads unencrypted audio files, and sends the events unencrypted.
- Bridged IRC users don't see a link to the file, but the filename as a string. It works for images posted via Riot web/android. I don't yet know enough to say whether the bot's file-posting events are missing data required to fall back properly, or if the IRC bridge doesn't give audio files the same linkification treatment as images.