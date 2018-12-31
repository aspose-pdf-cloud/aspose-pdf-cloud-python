# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2018 Aspose.PDF Cloud
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



    OpenAPI spec version: 2.0
    
"""


from pprint import pformat
from six import iteritems
import re


class DocumentPagesResponse(object):
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
        'code': 'int',
        'status': 'str',
        'pages': 'Pages'
    }

    attribute_map = {
        'code': 'Code',
        'status': 'Status',
        'pages': 'Pages'
    }

    def __init__(self, code=None, status=None, pages=None):
        """
        DocumentPagesResponse - a model defined in Swagger
        """

        self._code = None
        self._status = None
        self._pages = None

        self.code = code
        if status is not None:
          self.status = status
        if pages is not None:
          self.pages = pages

    @property
    def code(self):
        """
        Gets the code of this DocumentPagesResponse.
        Response status code.

        :return: The code of this DocumentPagesResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this DocumentPagesResponse.
        Response status code.

        :param code: The code of this DocumentPagesResponse.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def status(self):
        """
        Gets the status of this DocumentPagesResponse.
        Response status.

        :return: The status of this DocumentPagesResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DocumentPagesResponse.
        Response status.

        :param status: The status of this DocumentPagesResponse.
        :type: str
        """

        self._status = status

    @property
    def pages(self):
        """
        Gets the pages of this DocumentPagesResponse.
        Page object

        :return: The pages of this DocumentPagesResponse.
        :rtype: Pages
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages of this DocumentPagesResponse.
        Page object

        :param pages: The pages of this DocumentPagesResponse.
        :type: Pages
        """

        self._pages = pages

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
        if not isinstance(other, DocumentPagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
