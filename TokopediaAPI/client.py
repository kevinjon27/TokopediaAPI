# -*- coding: utf-8 -*-
from six.moves import urllib
from io import BytesIO
import logging
import gzip
import json

from .constant import Constant
from .utils import Utils
from .endpoints import (
    SearchEndpointsMixin, ProductEndpointsMixin
)

logger = logging.getLogger(__name__)


class Client(SearchEndpointsMixin, ProductEndpointsMixin, Utils, object):
    def __init__(self):
        self.endpoint = Constant.GRAPHQL_URL
        self.token = None
        self.headername = None
        
    def execute(self, query, variables=None):
        return self._send(query, variables)
    
    def inject_token(self, token, headername='Authorization'):
        self.token = token
        self.headername = headername
        
    @staticmethod
    def _read_response(response):
        """
        Extract the response body from a http response.
        :param response:
        :return:
        """
        if response.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO(response.read())
            res = gzip.GzipFile(fileobj=buf).read().decode('utf8')
        else:
            res = response.read().decode('utf8')
        return res

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
        

        if self.token is not None:
            headers[self.headername] = '{}'.format(self.token)

        req = urllib.request.Request(self.endpoint, json.dumps(data).encode('utf-8'), headers)

        try:
            response = urllib.request.urlopen(req)
            
            response_content = self._read_response(response)
            
            json_response = json.loads(response_content)
            
            return json_response
        except urllib.error.HTTPError as e:
            print((e.read()))
            print('')
            raise e