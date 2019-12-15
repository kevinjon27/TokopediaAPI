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
    #  python examples/product.py
    product_id = 631277786
    result = api.product_detail(product_id)
    
    _dir = os.path.dirname(__file__)
    _dir = os.path.join(_dir, 'json')
    
    if not os.path.exists(_dir):
        print("\n\nCreating json folder..\n\n")
        os.makedirs(_dir)
    
    print("Generate product detail..\n")
    with open(_dir + '/product_{}.json'.format(product_id), 'w') as outfile:
        json.dump(result, outfile, indent=2)
    
    price = result.get('data').get('getPDPInfo').get('basic').get('price')
    
    result = api.product_installment_calculation(price, 1)
    print("Generate product installment calculation..\n")
    with open(_dir + '/product_installment_calculation_{}.json'.format(product_id), 'w') as outfile:
        json.dump(result, outfile, indent=2)

    print('All ok')


