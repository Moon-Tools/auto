import discord
import requests
import random
import time
userIDs = {}
token = "" #Your Discord Token
coolDownBeforeAddingUserToTicket = 2 #Time before you add person to ticket you should have like atleast 2 because sometimes the bot doesn't add the user to the ticket
messageToTrigger = ""
print('Made by Moon\n Discord Server is https://discord.gg/c8ksPGPZvk')

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        global session_id
        
        if message.content == messageToTrigger and message.author.id == self.user.id:
            await message.delete()
            headers = {
    'authorization': token,
    'content-type': 'application/json'
 
}

            json_data = {
    'type': 3,
    'nonce': random.randint(1000, 1000000),
    'guild_id': '938011512063275008',
    'channel_id': '1038446057627062312',
    'message_flags': 0,
    'message_id': '1041827004565164042',
    'application_id': '722196398635745312',
    'session_id': self._connection.session_id,
    'data': {
        'component_type': 2,
        'custom_id': '\u2e77㳂畒䐜䨎\u10ca嚒簴㑀ⁱ搩兤\u1ad4㝦グ䑔朸ر渒审才㗩䎔ᝬङ義兀耀',
    },
}

            response = requests.post('https://discord.com/api/v9/interactions',  headers=headers, json=json_data)
            print(response)
            userIDs['userId'] = message.channel.recipient.id
            
        if  message.content == f"<@{self.user.id}> Welcome to our **ROBLOX Limiteds Middleman Service**" and message.author.id == 722196398635745312:
            time.sleep(coolDownBeforeAddingUserToTicket)
            await message.channel.send(userIDs['userId'])
            await client.get_user(userIDs['userId']).send(f'Made Auto Limiteds MM <#{message.channel.id}>')

client = MyClient()
client.run(token)