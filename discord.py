from discord_webhook import DiscordWebhook


class PostBot:
    def __init__(self):
        with open('webhook') as file:
            url = file.read()

        self.d = DiscordWebhook(
            url=url
        )

    def basic_post(self, msg):
        self.d.content = msg
        return self.d.execute()
