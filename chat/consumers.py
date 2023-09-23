import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone, dateformat

class ChatConsumer(WebsocketConsumer):

    def connect(self):

        self.id = self.scope['url_route']['kwargs']['room_id']
        
        print("Conectado!"+self.id)

        #crear un grupo espesifico para cada una de las habitaciones
        self.room_group_name = 'chat_%s' % self.id

        self.user = self.scope['user']

        #funcion que permite ejecutar codigo asincrono dentro de codigo sincrono

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
        )



        self.accept()

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)
        print("Desconectado")
        

    def receive(self, text_data):
        print("Recibido!")

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        time = timezone.now()
        datetime = dateformat.format(time, 'Y-m-d H:i:s')

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                #chat_message funcion que envia el mensaje
                'type': 'chat_message',
                'username': self.user.username,
                'message': message,
                'datetime':datetime,
                

            }
        )
        
    def chat_message(self, event):

        message = event['message']
        username = event['username']
        datetime = event['datetime']
        self.send(text_data=json.dumps({'message': message, 'username':username, 'datetime':datetime }))
        print(message)

