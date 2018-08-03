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



    OpenAPI spec version: 1.1
    
"""


from pprint import pformat
from six import iteritems
import re


class MarginInfo(object):
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
        'left': 'float',
        'right': 'float',
        'top': 'float',
        'bottom': 'float'
    }

    attribute_map = {
        'left': 'Left',
        'right': 'Right',
        'top': 'Top',
        'bottom': 'Bottom'
    }

    def __init__(self, left=None, right=None, top=None, bottom=None):
        """
        MarginInfo - a model defined in Swagger
        """

        self._left = None
        self._right = None
        self._top = None
        self._bottom = None

        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    @property
    def left(self):
        """
        Gets the left of this MarginInfo.

        :return: The left of this MarginInfo.
        :rtype: float
        """
        return self._left

    @left.setter
    def left(self, left):
        """
        Sets the left of this MarginInfo.

        :param left: The left of this MarginInfo.
        :type: float
        """
        if left is None:
            raise ValueError("Invalid value for `left`, must not be `None`")

        self._left = left

    @property
    def right(self):
        """
        Gets the right of this MarginInfo.

        :return: The right of this MarginInfo.
        :rtype: float
        """
        return self._right

    @right.setter
    def right(self, right):
        """
        Sets the right of this MarginInfo.

        :param right: The right of this MarginInfo.
        :type: float
        """
        if right is None:
            raise ValueError("Invalid value for `right`, must not be `None`")

        self._right = right

    @property
    def top(self):
        """
        Gets the top of this MarginInfo.

        :return: The top of this MarginInfo.
        :rtype: float
        """
        return self._top

    @top.setter
    def top(self, top):
        """
        Sets the top of this MarginInfo.

        :param top: The top of this MarginInfo.
        :type: float
        """
        if top is None:
            raise ValueError("Invalid value for `top`, must not be `None`")

        self._top = top

    @property
    def bottom(self):
        """
        Gets the bottom of this MarginInfo.

        :return: The bottom of this MarginInfo.
        :rtype: float
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """
        Sets the bottom of this MarginInfo.

        :param bottom: The bottom of this MarginInfo.
        :type: float
        """
        if bottom is None:
            raise ValueError("Invalid value for `bottom`, must not be `None`")

        self._bottom = bottom

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
        if not isinstance(other, MarginInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
