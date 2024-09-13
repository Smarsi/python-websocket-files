import os
import time
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .websocket_manager import WebSocketClient

class Handler(FileSystemEventHandler):
    def __init__(self, ws_connection: WebSocketClient):
        self.ws_connection = ws_connection

    def on_created(self, event):
        if event.is_directory:
            return None
        print(f'Arquivo {event.src_path} foi criado!')

        file_path = event.src_path

        # Envia o caminho do arquivo para o WebSocket
        try:
            with open(file_path, 'rb') as file:  # Abre o arquivo como binário
                file_content = file.read()
            
            # Envia o conteúdo binário do arquivo via WebSocket
            asyncio.run(self.ws_connection.send(file_content))
            print(f"Conteúdo do arquivo {file_path} enviado com sucesso!")
        
        except Exception as e:
            print(f"Erro ao enviar arquivo pelo WebSocket: {e}")



class Watcher:
    running: bool
    ws_connection: WebSocketClient

    def __init__(self, directory_to_watch, websocket_connection: WebSocketClient):
        self.directory_to_watch = directory_to_watch
        self.observer = Observer()
        self.running = False
        self.ws_connection = websocket_connection

    def run(self):
        event_handler = Handler(self.ws_connection)
        self.observer.schedule(event_handler, self.directory_to_watch, recursive=False)
        self.observer.start()
        self.running = True

        # Loop Principal - Mantém o programa rodando enquanto o observer estiver rodando
        while self.running:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                print("Stopping the program")
                self.stop()
                break

    def stop(self):
        if self.running:
            self.running = False
            self.observer.stop()
            self.observer.join()
