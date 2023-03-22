import random
from spotipy.oauth2 import SpotifyClientCredentials
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler
import spotipy
import spotipy.util as util
import os

#os.environ['https_proxy'] = 'https://user:password@host:port'


CLIENT_ID = 'client_ID'
CLIENT_SECRET = 'client_private_key'


TELEGRAM_TOKEN = ':'
bot = telegram.Bot(token=TELEGRAM_TOKEN)

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


GENRES = ['pop', 'rock', 'hiphop', 'jazz', 'classical']


def get_random_track(genre=None, mood=None):
    
    if genre:
        query = f'genre:{genre}'
    
    elif mood:
        query = f'mood:{mood}'
   
    else:
        query = random.choice(GENRES)
   
    results = spotify.search(q=query, type='track', limit=1)
    track = results['tracks']['items'][0]
    
    track_url = track['external_urls']['spotify']
    return track_url


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Вітаю!')
