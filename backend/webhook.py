from discord_webhook import DiscordWebhook, DiscordEmbed
from backend.converter import file_to_messages
import os
import json
import time

def upload_file(filepath):
    timestamp = int(time.time() * 1000)
    history = {}
    try:
        with open("history", "r") as f:
            try:
                history = json.loads(f.read())
            except:
                pass
    except:
        pass

    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    history[str(filename + "-**-" + str(timestamp))] = []

    print(f"SENDING {filename}...")
    print("COMPUTING MESSAGES...")
    messages = file_to_messages(filepath)
    print("MESSAGES CALCULATED")
    i = 0
    for x in messages:
        webhook = DiscordWebhook(
            url="https://discord.com/api/webhooks/1286979733917143110/9nI0lWs7A0klF9PLkTvs3GNLaAKenFLS0F6PgDfOx-gsdV_Pt4xxV_b3bx3faQZ6Vxl2",
            content="", rate_limit_retry=True, wait=True)
        embed = DiscordEmbed(title=filename + f" -- Fragments {i + 1}/{len(messages)}", color="FF0000")
        webhook.add_embed(embed)

        with open("fragment.ostk", "wb") as f:
            f.write(messages[i])
            f.close()
        i += 1
        with open("fragment.ostk", "rb") as f:
            webhook.add_file(file=f.read(), filename="fragment" + str(i) + ".ostk")
        print(f"{i}/{len(messages)}")

        response = webhook.execute()
        history[str(filename+"-**-"+str(timestamp))].append(response.json()["attachments"][0]["url"])

    with open("history", "w") as f:
        f.write(json.dumps(history))
    os.remove("fragment.ostk")
    print(f"SENT {filename} SUCCESSFULLY!")
