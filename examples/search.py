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

    api = Client()

    #  Example command:
    #  python examples/search.py
    result = api.search("iphone 6s case")
    
    _dir = os.path.dirname(__file__)
    _dir = os.path.join(_dir, 'json')
    
    if not os.path.exists(_dir):
        print("\n\nCreating json folder..\n\n")
        os.makedirs(_dir)
    
    with open(_dir + '/search.json', 'w') as outfile:
        json.dump(result, outfile, indent=2)

    print('All ok')


