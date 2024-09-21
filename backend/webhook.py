from discord_webhook import DiscordWebhook
from backend.converter import file_to_messages
import os


# webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1286979733917143110/9nI0lWs7A0klF9PLkTvs3GNLaAKenFLS0F6PgDfOx-gsdV_Pt4xxV_b3bx3faQZ6Vxl2", content="Webhook Message", rate_limit_retry=True)


print("COMPUTING MESSAGES...")
messages = file_to_messages("../sample.zip")
print("MESSAGES CALCULATED")
i = 0
for x in messages[::2]:
    webhook = DiscordWebhook(
        url="https://discord.com/api/webhooks/1286979733917143110/9nI0lWs7A0klF9PLkTvs3GNLaAKenFLS0F6PgDfOx-gsdV_Pt4xxV_b3bx3faQZ6Vxl2",
        content="Webhook Message", rate_limit_retry=True)

    for _ in range(2):
        with open("fragment.ostk", "wb") as f:
            f.write(messages[i])
            f.close()
        i += 1
        with open("fragment.ostk", "rb") as f:
            webhook.add_file(file=f.read(), filename="fragment" + str(i) + ".ostk")
        print(f"{i}/{len(messages)}")


    response = webhook.execute()


os.remove("fragment.ostk")


# response = webhook.execute()