from discord import Webhook
import aiohttp

async def foo():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('url-here', session=session)
        await webhook.send('Hello World', username='Foo')