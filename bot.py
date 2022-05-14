import discord
import random
# from hidden import hidden_words
# from discord.ext import commands
# from discord_slash import SlashCommand

# client = commands.Bot(command_prefix="=.")
counter = -1

cory_catchphrases = ["fo sho", "facts", "on god", "that's why they call me the mop",
                    "fr fr", "that's so stupid, if they didn't....", "I wouldn't have died",
                    "I said porshe, not porch", "you didn't have to do me like that",
                    "on fleet", "on facts", "goodnight gentlemen", "I'm gonna go bed",
                    "adits get on valo",  "so max", "I'm cracked", "I know you saw that",
                    "that's facts", "I'm one of the select few dudes here that gets pussy"
                    ]

cory_drops = {      # real odds
    "fo sho": 1, 
    "facts": 1, 
    "on god": 1, 
    "on fleet": 1, 
    "on facts": 1, 
    "fr fr": 1,
    "so max": 1, 
    "I'm cracked": 1, 
    "that's facts": 1, 
    "that's why they call me the mop": 1,
    "you didn't have to do me like that": 1,
    "goodnight gentlemen": 1, 
    "I'm gonna go to bed": 1,

    "I know you saw that": 1,
    "adits get on valo": 1,  

    "that's so stupid, if they didn't....": 1, 
    "I wouldn't have died": 1,
    "I said porshe, not porch": 1, 
    
    "I'm one of the select few dudes here that gets pussy": 1
    # <--------- ADD HIDDEN HERE
}


cory_fake_drops = {      # fake odds
    "fo sho": 1, 
    "facts": 1, 
    "on god": 1, 
    "on fleet": 1, 
    "on facts": 1, 
    "fr fr": 1,
    "so max": 1, 
    "I'm cracked": 1, 
    "that's facts": 1, 
    "that's why they call me the mop": 1,
    "you didn't have to do me like that": 1,
    "goodnight gentlemen": 1, 
    "I'm gonna go to bed": 1,

    "I know you saw that": 1,
    "adits get on valo": 1,  

    "that's so stupid, if they didn't....": 1, 
    "I wouldn't have died": 1,
    "I said porshe, not porch": 1, 
    
    "I'm one of the select few dudes here that gets pussy": 1
}

# print(cory_drops.values())


        
class MyClient(discord.Client):
    async def on_ready(self):
        self.counter = -1
        if self.counter == -1:
            with open('counter.txt', "r") as f:
                self.counter = int(f.readline())
        print("CoryBot is now ready!")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content == "cory_phrases":
            channel = message.channel
            # await channel.send(str(cory_catchphrases))
            await channel.send(str(list(cory_fake_drops.keys())))

        elif message.content == "cory_drops":
            channel = message.channel
            content = ""
            for phrase, rate in cory_fake_drops.items():
                # maybe if in hidden, dont print
                content += f"{phrase} -> {rate}\n"
            await channel.send(content)

        elif message.content == "cory_counter":
            channel = message.channel
            await channel.send(f"cory counter: {self.counter}")

        elif message.content.startswith("cory") or message.content.startswith("Cory"):
            # await message.reply(random.choice(cory_catchphrases)) 
            self.counter += 1
            channel = message.channel
            select = random.choices(list(cory_drops.keys()), weights=list(cory_drops.values()))
            await channel.send(select[0])
            # await channel.send(random.choice(cory_drops.keys()))
            # await channel.send(random.choice(cory_catchphrases))
        
        

# @client.event
# async def on_ready():
#     print("Bot is now ready!")

# @client.event
# async def on_message(message):
#     if message.author.id == self.user.id:


client = MyClient()
# client.run("OTY0Njg2Mjk2MjE3OTQ0MDk0.YloQIA.cANIhJyxwxSTtz3b8NUMe286i1s")
try:
    client.loop.run_until_complete(client.start("MY_API_KEY"))
except KeyboardInterrupt:
    client.loop.run_until_complete(client.close())
    print(client.counter)
    with open('counter.txt', 'w') as f:
        f.writelines(str(client.counter))

finally:
    client.loop.close()
    
    