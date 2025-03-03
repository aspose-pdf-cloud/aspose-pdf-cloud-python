# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


Copyright (c) 2025 Aspose.PDF Cloud
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


class TextReplaceListRequest(object):
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
        'text_replaces': 'list[TextReplace]',
        'default_font': 'str',
        'start_index': 'int',
        'count_replace': 'int'
    }

    attribute_map = {
        'text_replaces': 'TextReplaces',
        'default_font': 'DefaultFont',
        'start_index': 'StartIndex',
        'count_replace': 'CountReplace'
    }

    def __init__(self, text_replaces=None, default_font=None, start_index=None, count_replace=None):
        """
        TextReplaceListRequest - a model defined in Swagger
        """

        self._text_replaces = None
        self._default_font = None
        self._start_index = None
        self._count_replace = None

        self.text_replaces = text_replaces
        if default_font is not None:
          self.default_font = default_font
        if start_index is not None:
          self.start_index = start_index
        if count_replace is not None:
          self.count_replace = count_replace

    @property
    def text_replaces(self):
        """
        Gets the text_replaces of this TextReplaceListRequest.
        A list of text replacement settings.

        :return: The text_replaces of this TextReplaceListRequest.
        :rtype: list[TextReplace]
        """
        return self._text_replaces

    @text_replaces.setter
    def text_replaces(self, text_replaces):
        """
        Sets the text_replaces of this TextReplaceListRequest.
        A list of text replacement settings.

        :param text_replaces: The text_replaces of this TextReplaceListRequest.
        :type: list[TextReplace]
        """
        if text_replaces is None:
            raise ValueError("Invalid value for `text_replaces`, must not be `None`")

        self._text_replaces = text_replaces

    @property
    def default_font(self):
        """
        Gets the default_font of this TextReplaceListRequest.
        Name of font to use if requested font is not embedded into document.

        :return: The default_font of this TextReplaceListRequest.
        :rtype: str
        """
        return self._default_font

    @default_font.setter
    def default_font(self, default_font):
        """
        Sets the default_font of this TextReplaceListRequest.
        Name of font to use if requested font is not embedded into document.

        :param default_font: The default_font of this TextReplaceListRequest.
        :type: str
        """

        self._default_font = default_font

    @property
    def start_index(self):
        """
        Gets the start_index of this TextReplaceListRequest.
        The index of first match to be replaced.

        :return: The start_index of this TextReplaceListRequest.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """
        Sets the start_index of this TextReplaceListRequest.
        The index of first match to be replaced.

        :param start_index: The start_index of this TextReplaceListRequest.
        :type: int
        """

        self._start_index = start_index

    @property
    def count_replace(self):
        """
        Gets the count_replace of this TextReplaceListRequest.
        The number of matches to be replaced.

        :return: The count_replace of this TextReplaceListRequest.
        :rtype: int
        """
        return self._count_replace

    @count_replace.setter
    def count_replace(self, count_replace):
        """
        Sets the count_replace of this TextReplaceListRequest.
        The number of matches to be replaced.

        :param count_replace: The count_replace of this TextReplaceListRequest.
        :type: int
        """

        self._count_replace = count_replace

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
        if not isinstance(other, TextReplaceListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
