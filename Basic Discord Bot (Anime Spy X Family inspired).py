import discord
import requests
import json

client= discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " ~" + json_data[0]['a']
  return(quote)
  
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('hi'):
    await message.channel.send('Heyyo!!')

  if message.content.startswith('what would you like'):
    await message.channel.send('i want peanuts! 🥺🥺')
  
  if message.content.startswith('anime'+''):
    title= message.content[6:]
    string = title.replace(" ","-")
    await message.channel.send("https://www.anime-planet.com/anime/"+string)
    if string != ('spy-x-family') :
        await message.channel.send("Maybe search for Spy x Family later? 😳😳😳 ")
    if string == ('spy-x-family'):
      await message.channel.send("Am i lookin good?😳")

  if message.content.startswith('anya quote'):
    quote = get_quote()
    await message.channel.send(quote)    
    
  if message.content.startswith('anya?'):
    await message.channel.send('ye? um h-h yes?? ;)') 
    
  if message.content.startswith('anya help'):
    await message.channel.send('Oh okk here are the command you can use😳')
    await message.channel.send("Write 'anya' but i will be kinda embarrassed ")
    await message.channel.send("Write 'anya quote' for a random inspiring quote ig")
    await message.channel.send("Write 'hi' for a surprise")
    await message.channel.send("Write 'bye' for you already know what!")
    await message.channel.send("Write 'anime (The anime)' to get some info")
    await message.channel.send("Hope it helps...gimme a peanut in return tho🥺🥺")

  if message.content.startswith('bye'):
    await message.channel.send('Going so early? Have fun....')
    await message.channel.send('https://tenor.com/view/anya-anya-spy-x-family-anya-cry-anya-sob-anime-gif-25352161')  
    
client.run('Your bot token')
