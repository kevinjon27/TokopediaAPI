import json
import os

try:
    from TokopediaAPI import(Client, __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from TokopediaAPI import(
        Client, __version__ as client_version)


if __name__ == '__main__':

    print('Client version: {0!s}'.format(client_version))

    email = "xxx"
    password= "xxx"

    api = Client(username=email, password=password)

    #  Example command:
    #  python examples/login.py
    result = api.login_with_email()

    print(result)
    print('All ok')


