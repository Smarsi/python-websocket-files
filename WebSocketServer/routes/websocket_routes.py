import os
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

# Project Imports
from utils.websocket_manager import WebSocketConnectionManager
from utils.files_manager import convert_bytes_to_file

PATH_TO_SAVE_FILES = "./received_files" # Esta variável escolhe onde você quer salvar os arquivos recebidos pelo websocket
os.makedirs(PATH_TO_SAVE_FILES, exist_ok=True) # Cria o diretório se ele não existir

router = APIRouter(
    prefix="/ws",
    tags=["websocket"],
)


# Declaramos uma instância global da classe WebSocketManager para gerenciar no nosso projeto
wsocket_manager = WebSocketConnectionManager()

@router.websocket("/file")
@router.websocket("/file/")
async def websocket_endpoint(websocket: WebSocket):
    connection_id = await wsocket_manager.connect(websocket)
    try:
        while True:
            received_file = await websocket.receive_bytes()
            file = await convert_bytes_to_file(received_file, PATH_TO_SAVE_FILES)
            if(file):
                await websocket.send_text("success")
                continue
            await websocket.send_text("error")
    except WebSocketDisconnect:
        await wsocket_manager.disconnect(websocket)
