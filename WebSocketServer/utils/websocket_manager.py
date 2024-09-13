from uuid import uuid4 as uuid
from fastapi import WebSocket

# Essa classe é responsável por gerenciar as conexões por websocket.
class WebSocketConnectionManager:

    # __init__ é um método especial que é executado quando uma instância da classe é criada (construtor).
    def __init__(self):
        self.active_connections: list[WebSocket] = []
    
    # Método para adicionar uma conexão a lista de conexões ativas
    async def connect(self, websocket: WebSocket) -> str:
        await websocket.accept()
        self.active_connections.append(websocket)
        connection_id = str(uuid()).replace("-", "")
        return connection_id

    # Método para remover uma conexão da lista de conexões ativas
    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)