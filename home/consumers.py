from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class HomeConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.send_json({
            'msg': 'Hello world'
        })
