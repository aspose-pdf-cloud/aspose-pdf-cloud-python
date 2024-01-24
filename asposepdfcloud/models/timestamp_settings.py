# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


Copyright (c) 2024 Aspose.PDF Cloud
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



    OpenAPI spec version: 3.0
    
"""


from pprint import pformat
from six import iteritems
import re


class TimestampSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'server_url': 'str',
        'basic_auth_credentials': 'str'
    }

    attribute_map = {
        'server_url': 'ServerUrl',
        'basic_auth_credentials': 'BasicAuthCredentials'
    }

    def __init__(self, server_url=None, basic_auth_credentials=None):
        """
        TimestampSettings - a model defined in Swagger
        """

        self._server_url = None
        self._basic_auth_credentials = None

        if server_url is not None:
          self.server_url = server_url
        if basic_auth_credentials is not None:
          self.basic_auth_credentials = basic_auth_credentials

    @property
    def server_url(self):
        """
        Gets the server_url of this TimestampSettings.
        Gets/sets the timestamp server url.

        :return: The server_url of this TimestampSettings.
        :rtype: str
        """
        return self._server_url

    @server_url.setter
    def server_url(self, server_url):
        """
        Sets the server_url of this TimestampSettings.
        Gets/sets the timestamp server url.

        :param server_url: The server_url of this TimestampSettings.
        :type: str
        """

        self._server_url = server_url

    @property
    def basic_auth_credentials(self):
        """
        Gets the basic_auth_credentials of this TimestampSettings.
        Gets/sets the basic authentication credentials, Username and password are combined into a string \"username:password\".

        :return: The basic_auth_credentials of this TimestampSettings.
        :rtype: str
        """
        return self._basic_auth_credentials

    @basic_auth_credentials.setter
    def basic_auth_credentials(self, basic_auth_credentials):
        """
        Sets the basic_auth_credentials of this TimestampSettings.
        Gets/sets the basic authentication credentials, Username and password are combined into a string \"username:password\".

        :param basic_auth_credentials: The basic_auth_credentials of this TimestampSettings.
        :type: str
        """

        self._basic_auth_credentials = basic_auth_credentials

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TimestampSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
