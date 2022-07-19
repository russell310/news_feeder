from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


class GetNewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'news'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_news(self, event):
        text_message = event['text']
        await self.send(text_data=text_message)
