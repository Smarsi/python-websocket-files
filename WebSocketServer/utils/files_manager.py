import logging
from uuid import uuid4 as uuid

log = logging.getLogger("uvicorn")

'''
ANOTAÇÃO: Se for necessário lógica de conversão dos dados recebidos (como decode ou cálculos), pode ser implementada na função "convert_bytes_to_file".
'''


# Função usada para converter os bytes recebidos pelo websocket em um arquivo
async def convert_bytes_to_file(received_file: bytes, folder_to_save_files: str) -> bool:
    try:
        # Criamos uma string única para o nome do arquivo
        filename = str(uuid()).replace("-", "")
        
        filepath = f"{folder_to_save_files}/{filename}.txt" # Mude sua extensão de acordo com o tipo de arquivo que você quer salvar
        
        # Abrir o arquivo em mode de escrita binária e escrever os bytes recebidos
        with open(filepath, "wb") as f:
            f.write(received_file)
        return True
    except Exception as e:
        log.error(f"Error: {e}")
        return False

