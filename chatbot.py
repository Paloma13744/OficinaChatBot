import telebot
import requests  # Realiza aquisões a url do horóscopo

CHAVE ='6650573725:AAENjg9VHfIEJ1PTOntzB2CQFURnISiuyN0'

bot = telebot.TeleBot(CHAVE)
# Passamos o token para o telebot para que ele seja vinculado ao bot do telegram


#Função de pegar o horóscopo da API
def horoscopo_api(signo):
  #Trecho de código fornecido pela API Rapid
  url = f"https://horoscope-api.p.rapidapi.com/pt/{signo}"

  headers = {
	"X-RapidAPI-Key": "8b741854ffmsh61142dcde9a2b2dp127d53jsn098f2081e931",
	"X-RapidAPI-Host": "horoscope-api.p.rapidapi.com"
}

  resposta = requests.get(url, headers=headers)

  return resposta.json()


@bot.message_handler()
def inicio(msg):
  if(msg.text == "/horoscopo"):
    signo(msg)
  else:
    bot.reply_to(msg, "Oiii, eu sou um ChatBot desenvolvido com Python 🤖\n\nE estou aqui para lhe informar seu horóscopo 🔮\n\nEntão, para receber seu Horoscopo de Hoje, digite /horoscopo")


def signo(msg):
  signos = "Qual é seu Signo? 🔮\nEscolha um:\n*♈️ Aries*\n*♉️ Touro*\n*♊️ Gemeos*\n*♋️ Cancer*\n*♌️ Leao*\n*♍️ Virgem*\n*♎️ Libra*\n*♏️ Escorpiao*\n*♐️ Sagitario*\n*♑️ Capricornio*\n*♒️ Aquario*\n*♓️ Peixes*"
  enviar_msg = bot.send_message(msg.chat.id, signos, parse_mode="Markdown")
  bot.register_next_step_handler(enviar_msg, pegar_horoscopo_api)

def pegar_horoscopo_api(msg):
  signo = msg.text
  resposta = horoscopo_api(signo)
  titulo = resposta['title']
  data = resposta['date']
  texto = resposta['text']
  horoscopo_mensagem = f'*{titulo}*\n\n*Signo:* {signo}\n*Dia:*{data}\n\n{texto}'
  bot.send_message(msg.chat.id, "Aqui está o seu horóscopo!")
  bot.send_message(msg.chat.id, horoscopo_mensagem, parse_mode="Markdown")


bot.infinity_polling()
