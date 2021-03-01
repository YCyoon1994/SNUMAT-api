import logging

class Error:
    def __init__(self):
        pass
    def print(self, code):
        errorList = self._list()
        if code in errorList.keys():
            self._print(code, errorList.code)
        else:
            self._print('-1', errorList['0'])
    def _print(self, code, message):
        logging.error(f`[SM{code}] {message}`)
    def _list(self):
        return {
            '0' : 'Unexpected error',
            '-1001' : 'Wrong credential format. String of credential must be json format and include "public", "secret" ... keys. If you want to ',
            '-1002' : 'Credential file doesn\'t exist. Check the path of credential file'
        }
