from discord_webhook import DiscordWebhook, DiscordEmbed
from backend.converter import file_to_messages
import os
import json
import time

#from gui import increase_current_step, get_number_of_files

current_step = 0
number_of_frag = 0

def increase_current_step(from_webhook = True):
    global current_step
    if from_webhook:
        current_step += 1
    else:
        return int(current_step)

def get_number_of_files(length, from_webhook = True):
    global number_of_frag
    if from_webhook:
        number_of_frag = length
    else:
        return int(number_of_frag)

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
            url="INSERT YOUR WEBHOOK URL HERE",
            content="", rate_limit_retry=True, wait=True)
        embed = DiscordEmbed(title=filename + f" -- Fragments {i + 1}/{len(messages)}", color="FF0000")
        get_number_of_files(int(len(messages)))
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

        increase_current_step()

    with open("history", "w") as f:
        f.write(json.dumps(history))
    os.remove("fragment.ostk")
    print(f"SENT {filename} SUCCESSFULLY!")

