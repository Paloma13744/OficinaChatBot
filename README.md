# Horóscopo Bot

## Descrição

Este projeto é um chatbot desenvolvido com **Python** e a biblioteca **Telebot**, que fornece aos usuários do Telegram o horóscopo do dia. Ao interagir com o bot, o usuário pode selecionar seu signo e receber as previsões diretamente no chat. O horóscopo é obtido de uma **API** externa.

## Requisitos

- **Python 3.7+**
- Conta no **Telegram**
- Uma chave **API** válida para o bot no Telegram
- Chave de acesso para a API de Horóscopo da **RapidAPI**

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/horoscopo-bot.git
    cd horoscopo-bot
    ```

2. Instale as dependências:
    ```bash
    pip install pyTelegramBotAPI requests
    ```

3. Configure a chave de API do seu bot do Telegram. Para isso, substitua a variável `CHAVE` no código com o token do seu bot, obtido do BotFather no Telegram:
    ```python
    CHAVE = 'SUA_CHAVE_DE_BOT_DO_TELEGRAM'
    ```

4. Configure a chave de acesso da **RapidAPI** para a API de horóscopo:
    ```python
    headers = {
      "X-RapidAPI-Key": "SUA_CHAVE_DA_RAPIDAPI",
      "X-RapidAPI-Host": "horoscope-api.p.rapidapi.com"
    }
    ```

## Execução

Execute o bot com o seguinte comando:
```bash
python bot.py
