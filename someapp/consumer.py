from channels.generic.websocket import AsyncWebsocketConsumer

class EchoConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data=None, bytes_data=None):
        try:
            a, op, b = text_data.split()
            a, b = float(a), float(b)
            ops = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}
            result = ops[op]
            if result.is_integer():
                result = int(result)
        except Exception:
            result = 'error'
        await self.send(str(result))