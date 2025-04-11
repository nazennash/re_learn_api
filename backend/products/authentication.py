import threading
from rest_framework.authentication import TokenAuthentication

class Tokenizer(TokenAuthentication):
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)

        def delete_token():
            print("Hello World")
            token.delete()

        # timer = threading.Timer(60*60*24, delete_token)
        timer = threading.Timer(1.0, delete_token)
        timer.start()

        return user, token
