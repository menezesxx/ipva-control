# 🚗 IPVA Control

Sistema para controlar o **IPVA parcelado** de clientes e avisar quais boletos estão perto de vencer.

Comecei esse projeto para estudar back-end com Python, mas a ideia nasceu de um problema real: em despachantes, acompanhar dezenas de parcelas e vencimentos na mão (ou em planilha) dá muito trabalho e é fácil esquecer alguém. Quis ver como isso ficaria como sistema real.

> ⚠️ **Projeto de estudo com dados fictícios.** Nenhum dado real de cliente é usado aqui.

## 🚧 Status

Ainda estou construindo, então o projeto cresce a cada commit.

- [x] Conexão com o banco de dados (Supabase)
- [x] Listar clientes (`GET /clientes`)
- [x] Cadastrar cliente (`POST /clientes`): em teste
- [x] Buscar, atualizar e deletar cliente
- [ ] Cadastro de veículos
- [ ] Parcelas do IPVA com data de vencimento
- [ ] Painel com os boletos que estão para vencer
- [ ] Login de usuários

## 🛠️ Tecnologias

- Python 3.13
- FastAPI
- Supabase (PostgreSQL)
- Pydantic

## ▶️ Como rodar

1. Clone o repositório e entre na pasta:
   ```
   git clone https://github.com/menezesxx/ipva-control.git
   cd ipva-control
   ```
2. Crie e ative o ambiente virtual:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` na raiz do projeto com as suas chaves do Supabase:
   ```
   SUPABASE_URL=
   SUPABASE_PUBLISHABLE_KEY=
   ```
5. Rode a API:
   ```
   uvicorn main:app --reload
   ```
6. Abra `http://127.0.0.1:8000/docs` para ver e testar as rotas.

## 📚 O que estou aprendendo com ele

Construir uma API do zero, validar dados com Pydantic, usar um banco na nuvem, organizar um projeto no Git e escrever commits.


## 🤖 Uso de IA

Estou fazendo este projeto com o auxílio de IA generativa (**ChatGPT** e **Claude**). Uso essas ferramentas como um mentor: para tirar dúvidas, entender erros, revisar o que escrevi e decidir os próximos passos. Eu escrevo o código, testo e faço os commits, e tento entender cada parte antes de seguir.

## 👤 Autor


Feito por **Kauan Menezes**, estudante de Sistemas de Informação no CEFET-MG.
[GitHub](https://github.com/menezesxx) · [LinkedIn](https://www.linkedin.com/in/kauanmenezesbecatti/)