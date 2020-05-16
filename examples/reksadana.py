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
    #  python examples/reksadana.py
    # result = api.reksadana_user()
    # result = api.reksadana_user_portofolio()
    result = api.reksadana_order_history()

    print(result)
    print('All ok')


