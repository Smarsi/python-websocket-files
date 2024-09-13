## Requisitos

- Python 3.x
- pip

## Configurando o Ambiente

Para configurar o ambiente e executar o projeto, siga os passos abaixo:

1. Crie e ative a Virtual Environment (Venv):
    <h5>Cada projeto dentro deste repositório deve ter seu próprio env (um para client e outro para server)</h5>

    Na pasta do server:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Instale as dependências do projeto

    ```bash
    pip install -r requirements.txt
    ```

## Executando o projeto

Quando o ambiente estiver configurado você será capaz de rodar o projeto.
Este projeto permite a execução através de suas ferramentas principais, sendo uma delas recomendado para o ambiente de desenvolvimento a outra para produção.


* <b>Desenvolvimento</b>

```bash
 uvicorn main:app --port 8000
```

Caso queira melhorar sua experiência no ambiente de desenvolvimento, é possível ativar o reload automático através de uma flag.

```bash
 uvicorn main:app --port 8000 --reload
```

Se deseja usar a ferramenta de desenvolvimento na sua rede local é preciso passar outras flags, além disso, também é necessário permitir acesso à porta do projeto no seu Firewall.
Para deixar o sistema disponível na rede use o comando:

```bash
uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000
```
obs: Cada worker declarado no comando acima inicia uma instância do servidor, portanto se você não pretende usar multithreading ou está lidando com processos complexos dos quais não está controlando concorrência deixe apenas 1 worker.

<br>
<b>Atenção:</b> Em todos os casos mostrados a flag --workers diz respeito a quantidade de threads que serão usadas para o <i>multiprocessing</i>, portanto, lembre-se de respeitar os limites de sua máquina. O fastapi é uma ferramenta para construção de APIs Assíncronas, ou seja, o número de cores do seu processador pode mudar totalmente sua experiência com ele.

## Contribuindo

Se deseja contribuir com o projeto, siga os passos abaixo:

1. Crie um novo branch com um nome descritivo:
    
    ```bash
    git checkout -b nome_do_branch
    ```

2. Faça as alterações necessárias e adicione os arquivos modificados:

    ```bash
    git add .
    ```

3. Faça o commit das suas alterações:

    ```bash
    git commit -m "Descrição das alterações"
    ```

4. Faça o push para o repositório remoto:

    ```bash
    git push origin nome_do_branch
    ```

5. Abra um Pull Request explicando as alterações propostas.


---

##### <center> @Copyright - Todos os direitos reservados </center>