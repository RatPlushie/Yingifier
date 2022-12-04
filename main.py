import telethon
from decouple import config

if __name__ == '__main__':
	api_id = config('api_id')
	api_hash = config('api_hash')
