from telethon import TelegramClient, events
from decouple import config

if __name__ == '__main__':
	try:
		# Getting api config from .env file
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
			peer_id = message_obj.peer_id
			entity_id = ''
			if hasattr(peer_id, 'user_id'):
				entity_id = peer_id.user_id

			if hasattr(peer_id, 'channel_id'):
				entity_id = peer_id.channel_id



			#print(message_obj)
			#print('Message ID: {}, Message Text: {}, Entity ID: {}'.format(message_id, message_text, entity_id))

			# Replacing the captured method with the new string
			await client.edit_message(entity=entity_id, message=message_id, text='Replacement test')


		with client:
			client.loop.run_forever()

	except KeyboardInterrupt:
		print('\nDisconnecting and closing Yingifier')
		client.disconnect()
