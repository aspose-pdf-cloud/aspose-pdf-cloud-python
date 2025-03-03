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


class PageWordCount(object):
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
        'page_number': 'int',
        'count': 'int'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'count': 'Count'
    }

    def __init__(self, page_number=None, count=None):
        """
        PageWordCount - a model defined in Swagger
        """

        self._page_number = None
        self._count = None

        self.page_number = page_number
        self.count = count

    @property
    def page_number(self):
        """
        Gets the page_number of this PageWordCount.
        Page number.

        :return: The page_number of this PageWordCount.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this PageWordCount.
        Page number.

        :param page_number: The page_number of this PageWordCount.
        :type: int
        """
        if page_number is None:
            raise ValueError("Invalid value for `page_number`, must not be `None`")

        self._page_number = page_number

    @property
    def count(self):
        """
        Gets the count of this PageWordCount.
        Number of words at the page.

        :return: The count of this PageWordCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this PageWordCount.
        Number of words at the page.

        :param count: The count of this PageWordCount.
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")

        self._count = count

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
        if not isinstance(other, PageWordCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
