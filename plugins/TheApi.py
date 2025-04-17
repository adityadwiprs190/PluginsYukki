import aiohttp

class API:
    async def get_advice(self):
        url = "https://api.adviceslip.com/advice"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return data["slip"]["advice"]

api = API()
