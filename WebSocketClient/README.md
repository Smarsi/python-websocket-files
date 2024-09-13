## Requisitos

- Python 3.x
- pip

## Configurando o Ambiente

Para configurar o ambiente e executar o projeto, siga os passos abaixo:

1. Crie e ative a Virtual Environment (Venv):
    <h5>Cada projeto dentro deste repositório deve ter seu próprio env (um para client e outro para server)</h5>

    Na pasta do client:
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

```bash
python3 main.py --config ./path/to/config/file.json
```


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