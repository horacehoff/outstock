import discord
import os
from backend.converter import file_to_messages


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'sendfile':
            filepath = "../sample.zip"
            filename = os.path.basename(filepath)
            filesize = os.path.getsize(filepath)
            print(f"SENDING {filepath} TO SERVER...")
            await message.channel.send(f"SENDING {filename} -- {str(filesize)} BYTES")
            messages = file_to_messages("../sample.zip")
            i = 0
            for x in messages:
                with open("fragment","wb") as f:
                    f.write(messages[0])
                    f.close()
                i += 1
                await message.channel.send(filename+"+-/+"+f"{i}/{len(messages)}"+"+-/+"+str(filesize)+"+-/+          "+str(int(i*100/len(messages)))+"%", file=discord.File("fragment"))
                print(f"{i}/{len(messages)}")
            await message.channel.send(f"SENT {filename} TO SERVER!")
            os.remove("fragment")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTI4NjcyODIyNDk2OTE5OTc1Ng.GDN89x.0ocHVNaJC7r31sWNxTlk3zqltLjTxbYNBsPMgc')