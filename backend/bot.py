import discord
import os
from discord.ext import tasks
from backend.converter import file_to_messages



class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        self.printer.start()

    @tasks.loop(seconds=1.0)
    async def printer(self):
        with open("threads", 'r') as f:
            if f.read() != "":
                f.seek(0)
                # print(f.read())
                # f.close()
                filepath = f.read()
                f.close()
                with open("threads","w") as g:
                    g.write("")
                    g.close()
                filename = os.path.basename(filepath)
                filesize = os.path.getsize(filepath)
                print(f"SENDING {filepath} TO SERVER...")
                await client.get_channel(1246476145176870924).send(f"SENDING {filename} -- {str(filesize)} BYTES")
                print("COMPUTING MESSAGES...")
                messages = file_to_messages(filepath)
                print("MESSAGES CALCULATED")
                i = 0
                for x in messages:
                    with open("fragment.ostk", "wb") as f:
                        f.write(messages[0])
                        f.close()
                    i += 1
                    await client.get_channel(1246476145176870924).send(
                        filename + "+-/+" + f"{i}/{len(messages)}" + "+-/+" + str(filesize) + "+-/+          " + str(
                            int(i * 100 / len(messages))) + "%", file=discord.File("fragment.ostk"))
                    print(f"{i}/{len(messages)}")
                await client.get_channel(1246476145176870924).send(f"SENT {filename} TO SERVER!")
                os.remove("fragment.ostk")


intents = discord.Intents.default()
intents.message_content = True
client = BotClient(intents=intents)


def start():
    client.run('MTI4NjcyODIyNDk2OTE5OTc1Ng.GDN89x.0ocHVNaJC7r31sWNxTlk3zqltLjTxbYNBsPMgc')