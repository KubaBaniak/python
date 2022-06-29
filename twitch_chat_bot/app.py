from requests import get

url = 'https://www.twitch.tv/loltyler1'

raw = get(url).text
chat = raw.split('chat-room-component-layout')
print(chat)
