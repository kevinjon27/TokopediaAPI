# -*- coding: utf-8 -*-
from six.moves import urllib
from io import BytesIO
import logging
import gzip
import json
import os
import uuid
import requests

from .constant import Constant
from .endpoints import (
    SearchEndpointsMixin, ProductEndpointsMixin
)

logger = logging.getLogger(__name__)

from .utils import *


class Client(SearchEndpointsMixin, ProductEndpointsMixin, object):
    def __init__(self, username, password, GODataPath=None):
        self.endpoint = Constant.GRAPHQL_URL
        self.username = username
        self.password = password
        self.token = None
        self.refresh_token = None
        self.uid = None
        self.headername = None
        self.GODataPath = None
        self.customPath = False

        if GODataPath is not None:
            self.GODataPath = GODataPath
            self.customPath = True
        else:
            self.GODataPath = os.path.join(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data'),
                username,
                ''
            )
            if not os.path.isdir(self.GODataPath):
                os.mkdir(self.GODataPath, 0o777)

        self.checkSettings(username)
        self.setUser(username)

        super(Client, self).__init__()


    def setUser(self, username):
        """setUsername

        Arguments:
            username {string}
        """                 
        self.username = username

        self.checkSettings(username)

        if os.path.isfile(self.GODataPath + 'settings-'+ self.username + '.dat') and \
                (self.settings.get('access_token') != None):
            self.token = self.settings.get('access_token')
            self.refresh_token = self.settings.get('refresh_token')
            self.uid = self.settings.get('uid')
        else:
            self.isLoggedIn = False

        print(self.token)

    def checkSettings(self, username):
        if not self.customPath:
            self.GODataPath = os.path.join(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data'),
                username,
                ''
            )

        if not os.path.isdir(self.GODataPath): os.mkdir(self.GODataPath, 0o777)

        self.settings = Settings(
            os.path.join(self.GODataPath, 'settings-' + username + '.dat')
        )
        
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

    def login_with_email(self, force=False):
        response = None
        if (not self.isLoggedIn) or force:

            data = {
                'username': self.username,
                'password': self.password,
                'grant_type': "password"
            }

            response = self._call_api('token', params=data, method="POST", host=Constant.ACCOUNT_URL)
            
            if response["access_token"]:
                self.isLoggedIn = True
                self.uid = str(response['uid'])
                self.token = response['access_token']
                self.refresh_token = response['refresh_token']
                self.settings.set('uid', self.uid)
                self.settings.set('access_token', self.token)
                self.settings.set('refresh_token', self.refresh_token)
            return response
        else:
            return 'user has been logged in.'

    @property
    def default_headers(self):
        return {
            'accept-language': 'id;q=1.0',
            'x-tkpd-authorization': 'TKPD Tokopedia:rALGFVc4jhw/5T7+LMRY737/4MY=',
            'x-device': 'ios',
            'user-agent': Constant.USER_AGENT,
            'x-app-version': Constant.APP_VERSION
        }

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

    
    def _call_api(self, endpoint, params=None, return_response=False, method="GET", host=Constant.API_BASE_URL):
        """
        Calls the private api.
        :param endpoint: endpoint path that should end with '/', example 'discover/explore/'
        :param params: POST parameters
        :param query: GET url query parameters
        :param return_response: return the response instead of the parsed json object
        :param method
        :return:
        """

        url = "{0}{1}".format(host, endpoint)

        headers = self.default_headers
        response = None

        if (self.settings.get('access_token')):
            headers['Authorization'] = 'Bearer ' + self.settings.get('access_token')

        if (method == 'POST'):
            response = requests.post(url, data=params, headers=headers, auth=(Constant.BASIC_AUTH_USER, Constant.BASIC_AUTH_PASW))
        else:
            response = requests.get(url, params=params, headers=headers)



        json_response = response.json()

        print("url: " + url)
        return json_response