import requests

class SAPI:
    def __init__(self, credential):
        self.credential = credential
    def _url(self):
        url = "https://api.snumat.com/user/auth/token"
        return url
    def getToken(self):
        requests.post(_url('/tasks/'), json={
            'summary': summary,
            'description': description,
        })
