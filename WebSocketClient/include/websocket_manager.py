import websockets


class WebSocketClient:
    def __init__(self, url):
        self.url = url

    async def connect(self)->bool:
        try:
            self.connection = await websockets.connect(self.url)
            return True
        except Exception as e:
            print(f"Error - Cannot connect to websocket server: {e}")
            return False

    async def send(self, message):
        if isinstance(message, (bytes, bytearray)):
            await self.connection.send(message)  # Enviar como binário
        else:
            await self.connection.send(str(message))  # Enviar como string

    async def receive(self):
        return await self.connection.recv()

    async def close(self):
        await self.connection.close()
