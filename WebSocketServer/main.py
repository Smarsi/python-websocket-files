import os 
import logging
import logging.config
from uuid import uuid4 as uuid
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

# Project imports
from routes.websocket_routes import router as websocket_router
from utils.websocket_manager import WebSocketConnectionManager
from utils.files_manager import convert_bytes_to_file

# Declaramos o uvicorn como servidor HTTP para receber os logs no terminal
log = logging.getLogger("uvicorn")

# Factory da aplicação FastAPI
def create_application():
    app = FastAPI()
    # Registrar rotas do websocket na nossa aplicação
    app.include_router(
        websocket_router
    )
    return app

# Criamos a aplicação FastAPI
app = create_application()

# ===== Configuração do CORS para não receber erros de conexão ==============
origins = [
    "*", # Allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ===== FIM - Configuração do CORS para não receber erros de conexão ========


# ===== Registro de eventos de startup e shutdown ===========================
@app.on_event("startup")
async def startup():
    log.info("Starting up the application")

@app.on_event("shutdown")
async def shutdown():
    log.info("Shutting down the application")

# ===== FIM - Registro de eventos de startup e shutdown =====================