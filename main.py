import discord

client = discord.Client()

token = "here token"
rickrolllog = 0

@client.event
async def on_message(message):
    if(str(message.content).startswith("r!")):
        embedVar = discord.Embed(title="You need to register your user to start the bot!", description="Sorry, it's just how it is!", color=0x000000)
        embedVar.add_field(name="Here's the link", value="[Click to register!](https://www.sanfransentinel.com/help95.html)")
        await message.channel.send(embed=embedVar)
	try:
        	chan = await client.fetch_channel(rickrolllog)
        	await chan.send(f"{message.author} is about to get rickrolled bois!")
	except:
		pass
   
client.run(token)