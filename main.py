from telethon import TelegramClient, events
from decouple import config

if __name__ == '__main__':
	try:
		# Getting vars from .env file
		api_id = config('api_id')
		api_hash = config('api_hash')
		user_phone_number = config('phonenum_to_watch')

		# Starting the telegram client
		client = TelegramClient('Yingifier_Session', api_id, api_hash)
		client.start()

		# Event watcher waiting for when the user to send a message to any channel/chat
		@client.on(events.NewMessage(outgoing=True))
		async def new_message_handler(event):
			# Extracting the message variables from the event
			message_obj = event.message
			message_id = message_obj.id
			message_text = message_obj.message


		with client:
			client.loop.run_forever()

	except KeyboardInterrupt:
		print('Disconnecting and closing Yingifier')
