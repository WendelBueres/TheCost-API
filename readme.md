# The Cost - API

Uma API para registro de receitas e gastos.

##  Tecnologias utilizadas
Para esse projeto foi utilizado o Python, Django, Django REST Framework, DRF-Spectacular e SQLite.

Django: É um framework baseado em Python, ele facilita o desenvolvimento e disponibiliza diversas soluções de modo integrado, dentre elas o ORM que é utilizado nessa aplicação.

Django REST Framework: É um framework para Django, por meio dele é possível acelerar o desenvolvimento, pois, ele abstrai diversas regras como, por exemplo, a definição de regras para a entrada de campos.

DRF-Spectacular: Ferramenta que auxilia a geração de esquemas para a documentação da API.

SQLite: Um dos banco de dados relacionais mais utilizados no mercado. 

## Instalação
Para executar esse projeto, é necessário que você tenha o Python instalado em sua máquina. Se não tiver, proceda com a instalação antes de executar os passos abaixo.

### Linux/Mac OS
 1. Clone o repositório.
 2. Na raiz do repositório clonado, execute o terminal.
 3. Com o terminal aberto execute o comando: ``python -m venv venv``.
 4. Execute o comando: ``source venv/bin/activate``.
 5. Após ativar o venv (ambiente virtual), execute o comando: ``pip install -r requirements.txt``. Esse comando irá instalar no ambiente virtual as dependências necessárias para executar o projeto.
 6. Execute o comando: ```python manage.py migrate```. Esse comando irá executar as migrações do Django e iniciar o SQLite na raiz do projeto. 
 7. Execute o comando: `python manage.py runserver`.
 8. O Django irá executar o servidor local, por meio dele é possível testar a API, o endereço do servidor local é exibido no terminal. 

### Windows
 1. Clone o repositório.
 2. Na raiz do repositório clonado, execute o terminal.
 3. Com o terminal aberto execute o comando: ``python -m venv venv``.
 4. Execute o comando: ``.\venv\Scripts\activate``.
 5. Após ativar o venv (ambiente virtual), execute o comando: ``pip install -r requirements.txt``, esse comando irá instalar no ambiente virtual as dependências necessárias para executar o projeto.
 6. Execute o comando: ```python manage.py migrate```. Esse comando irá executar as migrações do Django e iniciar o SQLite na raiz do projeto.  
 7. Execute o comando: `python manage.py runserver`
 8. O Django irá executar o servidor local, por meio dele é possível testar a API, o endereço do servidor local é exibido no terminal.  

## Documentação

A documentação do projeto está disponibilizada no endpoint ``/docs``, exemplo: se o servidor local estiver sendo rodado no endereço http://127.0.0.1:8000, será possível acessar a documentação em  http://127.0.0.1:8000/docs.

No repositório está disponível um WorkSpace do Insomnia (Cliente HTTP), por meio dele é possível testar algumas funções da API e entender suas requisições e respostas. 