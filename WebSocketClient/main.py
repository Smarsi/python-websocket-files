import os
import json
import asyncio
import argparse
import threading
from signal import SIGINT
import time

# Project Imports
from include.websocket_manager import WebSocketClient
from include.watchfiles_manager import Watcher

async def main(config_file: str):
    ws_url = None
    folder_to_watch = None
    try:
        config_info = json.loads(open(config_file).read()) 
        ws_url = config_info["websocket_url"]
        folder_to_watch = config_info["local_folder_to_watch_files"]
    except Exception as e:
        print("Error - Cannot read config file... please check the file and try again")
        print(f"Error: {e}")
        return
    
    if (not ws_url or not folder_to_watch):
        print("Error - Cannot read config file... please check the file and try again")
        print(f"Error: {e}")
        return


    # Connect to websocket
    ws = WebSocketClient(ws_url)
    await ws.connect()

    # Watcher
    watcher = Watcher(folder_to_watch, ws)
    watcher_thread = threading.Thread(target=watcher.run) 
    watcher_thread.daemon = True # Deamon Thread is used to stop the thread when the main thread is stopped
    watcher_thread.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping the program")
            watcher.stop()
            break
        except SIGINT:
            print("Stopping the program")
            watcher.stop()
            break

if __name__ == "__main__":
    
    # Declara os argumentos obrigatórios para rodar o projeto
    parser = argparse.ArgumentParser(description="Websocket client for send files")
    parser.add_argument("--config", type=str, help="Path to config file", required=True)
    
    # Pega o argumento passado
    config_file = parser.parse_args().config
    
    # Chama a função principal
    asyncio.run(main(config_file))
