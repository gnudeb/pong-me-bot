import asyncio
import json
import logging
from sys import stdout
from urllib.parse import urlencode

import aiohttp


log = logging.getLogger()
logging.basicConfig(stream=stdout, level=logging.DEBUG)


class BadAPIResponseError(Exception):
    pass


class Bot:
    _api_entry = "https://api.telegram.org"

    def __init__(self, token: str):
        self.token = token
        self.http_session: aiohttp.ClientSession
        self.update_offset = -1
        self.polling = False
        self.running = True
        self.handler = None

    async def _startup(self):
        log.info("Bot starting...")
        self.http_session = aiohttp.ClientSession()

    async def _shutdown(self):
        log.info("Bot shutting down...")
        await self.http_session.close()

    async def _wait_for_exit(self):
        while self.running:
            await asyncio.sleep(0)

    async def run_async(self):
        await self._startup()
        self.start_polling()
        await self._wait_for_exit()
        await self._shutdown()

    def run(self, loop=None):
        loop = loop or asyncio.get_event_loop()
        loop.run_until_complete(self.run_async())

    def start_polling(self):
        self.polling = True
        loop = asyncio.get_event_loop()
        loop.create_task(self.poll())

    async def api_call(self, method: str, **kwargs):
        url = f"{self._api_entry}/bot{self.token}/{method}"

        if kwargs:
            url += f"?{urlencode(kwargs)}"

        log.debug(f"Issuing API call: {url}")
        async with self.http_session.get(url) as response:
            if response.status != 200:
                msg = f"API call returned code {response.status}: {url}"
                log.error(msg)
                raise BadAPIResponseError(msg)

            data = json.loads(await response.read())

        if not data['ok']:
            raise BadAPIResponseError(f"API call returned not ok with message: {data['description']}")

        return data['result']

    async def get_updates(self, offset, timeout=60):
        return await self.api_call("getUpdates", offset=offset, timeout=timeout)

    async def poll(self):
        loop = asyncio.get_event_loop()
        while self.polling:
            messages = await self.get_updates(self.update_offset)
            for message in messages:
                log.debug(f"Got message: {message}")
                self.update_offset = max(message['update_id'] + 1, self.update_offset)
                loop.create_task(self.handler(message))
