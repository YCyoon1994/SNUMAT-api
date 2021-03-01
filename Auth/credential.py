import json
import os
import re
import SNUMAT.Log.error
"""
json format
{
	"public": {public key},
	"secret": {secret key},
	"region": "SNUMAT-KR-1",
	"auth_uri": "https://account.snumat.com/o/oauth2/auth",
	"token_uri": "https://api.snumat.com/auth/token/verify",
	"version": "v0.3"
}
"""
class Credential:
    def __init__(self, query):
        self.query = query
    def getCredential(self):
        query = self.query
        if os.path.exists(query):
            with open(query, "r") as f:
                try:
                    f = open(query, "r")
                    q = f.read()
                except:
                    pass    
    def parseCredential(self, string):
        try:
            str = string.trim()
            decode = json.loads(str).decode('utf-8')
            if not self._fileChecker(decode):
                return False, {}
            else:
                return True, decode
        except ValueError:
            return False, {}
        except JSONDecodeError:
            return False, {}
    def _fileChecker(self, dics):
        if !("version" in dics.keys()):
            return False
        version = dics.version
        if version == "v0.3":
            keyList = ['public', 'secret', 'region', 'auth_uri', 'token_uri', 'version']
            for k in keyList:
                if !(k in dics.keys()):
                    return False
            return True
        else:
            return False
