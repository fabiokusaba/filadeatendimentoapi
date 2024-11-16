# API para Fila de Atendimento

## Resumo do projeto
API desenvolvida com o propósito de ser utilizada em um totem de uma fila para atendimento presencial.
As funcionalidades da API incluem:
* Exibir todos os clientes na fila com as seguintes informações: posição, nome e data de chegada.
* Retornar os dados do cliente com base em sua posição na fila (id).
* Adicionar um novo cliente na fila passando o seu nome e o tipo de atendimento (normal ou prioritário), ainda é
possível adicionar um cliente com base em sua prioridade, ou seja, clientes prioritários (P) são adicionados antes dos
clientes normais (N).
* Atualizar a posição de cada pessoa na fila, incluindo atendimento com base no sistema de prioridades implementado.
* Remover o cliente especificado atualizando a posição dos demais clientes na fila.

## Tecnologias utilizadas:
* Python3
* FastAPI

## Instruções
* Primeiramente clone o projeto através do comando: `git clone`
* Configure e ative o seu ambiente virtual `venv`
* Instale as dependências do projeto com o comando: `pip install -r requirements.txt`
* Execute a aplicação com o comando: `uvicorn main:app`
* Acesse a URL: [localhost:8000/docs](http://localhost:8000/docs)
 para acessar a documentação da API.
* <strong>OBS:</strong> lembre-se de ter o <i>Python3</i> e o <i>pip</i> instalado em seu SO.