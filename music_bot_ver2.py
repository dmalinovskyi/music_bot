from telebot import TeleBot, types
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = ''
client_secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


bot = TeleBot('')


def get_random_track():
    track_list = sp.search(q='year:2022', type='track', limit=50)['tracks']['items']
    random_track = random.choice(track_list)
    return random_track['external_urls']['spotify']


def get_tracks_by_genre(genre):
    track_list = sp.search(q='genre:' + genre, type='track', limit=50)['tracks']['items']
    random_track = random.choice(track_list)
    return random_track['external_urls']['spotify']


def get_tracks_by_mood(mood):
    if mood == 'happy':
        mood = 'happy OR party'
    elif mood == 'sad':
        mood = 'sad OR melancholic'
    track_list = sp.search(q='year:2022 ' + mood, type='track', limit=50)['tracks']['items']
    random_track = random.choice(track_list)
    return random_track['external_urls']['spotify']


@bot.message_handler(commands=['random'])
def send_random_track(message):
    track_url = get_random_track()
    bot.reply_to(message, 'Ось випадкова пісня: ' + track_url)
    print(message.text)

@bot.message_handler(commands=['random'])
def send_track_by_genre(message):
    genre = message.text.split()[1]
    track_url = get_tracks_by_genre(genre)
    bot.reply_to(message, 'строка' + genre + ':'+ track_url)
    print(message.text)

@bot.message_handler(commands=['mood'])
def send_track_by_mood(message):
# Визначення настрою
    mood = message.text.split()[1]
    track_url = get_tracks_by_mood(mood)
    bot.reply_to(message, 'Ось пісня з настроєм ' + mood + ': ' + track_url)
    print(message.text)

@bot.message_handler(commands=['programming'])
def send_track_for_programming(message):
    track_url = get_tracks_by_genre('classical,techno')
    bot.reply_to(message, 'Ось пісня для програмування: ' + track_url)
    print(f"ID{message.from_user.username}: {message.text}")
    print(f"ID : {message.chat.id}")
    print(f"ID : {message.message_id}")
    print(message.text)

@bot.message_handler(func=lambda message: message.text.lower() == 'привіт')
def say_hello(message):
    bot.reply_to(message, 'Привіт!')
    print(message.text)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, 'Не розумію, що ви маєте на увазі. Спробуйте ще раз.')
    print(message.text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(f"ID{message.from_user.username}: {message.text}")
    print(f"ID : {message.chat.id}")
    print(f"ID : {message.message_id}")
    print(message.text)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.text)


bot.polling()
