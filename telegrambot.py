from gettext import dpgettext
from re import S
from aiogram import Bot, Dispatcher, executor, types
import requests
import time
import json
import os

class TelegramBot:
    def __init__(self):
        token = '5301307228:AAGMeKIPPntxRh8uCQZH521ttI--wf1yJtA'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao['result']
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('ajuda', 'Ajuda'):
            return f'''Digite uma das opção para continuar:
             Para Área Cível digite "1"
             Para Área Família digite "2"
             Para Área Penal digite "3"
             Para Área Trabalhista digite "4" '''

        if mensagem == '1':
            return f'''Digite 10 para
Digite 11
Digite 12'''
        elif mensagem == '10':
            return f'''warriors'''

        elif mensagem == '11':
            return f'''spurs'''
            
        elif mensagem == '12':
            return f'''raptors'''

        elif mensagem == '2':
            return f'''Digite 20 para 
Digite 21
Digite 22'''

        if mensagem == '20':
            return f'''thunder'''
        
        elif mensagem == '21':
            return f'''grilles'''
        
        elif mensagem == '22':
            return f'''suns'''

        elif mensagem == '3':
            return f'''Digite 30
Digite 31
Digite 32'''

        if mensagem == '30':
            return f'''honerts'''

        elif mensagem == '31':
            return f'''celtics'''
        
        elif mensagem == '32':
            return f'''lakers'''

        elif mensagem == '4':
            return f'''Digite 40 para está trabalhando. 
Digite 41 para demissão por justa causa.'''

        if mensagem == '40':
                return f'''Digite 42 para tem carteira assinada.
Digite 43 para não tem carteira assinada'''
 
        elif mensagem =='44':
            return f''''''

        elif mensagem == '':
                return f'''Digite  para saber os direitos que você tem.
Digite 44 para caso não tenha sido justa causa.'''
        
        elif mensagem == '':
            return f'''Marque uma ida ao NPJ'''
    
        elif mensagem.lower() in ('s', 'sim', 'Sim', 'S'):
            return ''' ok '''
        elif mensagem.lower() in ('n', 'não', 'Não', 'N'):
            return ''' ok '''
        else:
            return 'Olá! Eu sou a Natalia, sua ajudante digital! Se necessita de ajuda digite "ajuda" '

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()