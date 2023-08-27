import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Тут мы отправляем, а в lobby.html обрабатываем
        self.accept()
        
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!'
        }))
        
    def receive(self, text_data):
        # Здесь мы получаем message из form lobby.html
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        print('Message: ', message)
        
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))