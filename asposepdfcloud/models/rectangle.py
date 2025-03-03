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


class Rectangle(object):
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
        'llx': 'float',
        'lly': 'float',
        'urx': 'float',
        'ury': 'float'
    }

    attribute_map = {
        'llx': 'LLX',
        'lly': 'LLY',
        'urx': 'URX',
        'ury': 'URY'
    }

    def __init__(self, llx=None, lly=None, urx=None, ury=None):
        """
        Rectangle - a model defined in Swagger
        """

        self._llx = None
        self._lly = None
        self._urx = None
        self._ury = None

        self.llx = llx
        self.lly = lly
        self.urx = urx
        self.ury = ury

    @property
    def llx(self):
        """
        Gets the llx of this Rectangle.
        X-coordinate of lower - left corner.

        :return: The llx of this Rectangle.
        :rtype: float
        """
        return self._llx

    @llx.setter
    def llx(self, llx):
        """
        Sets the llx of this Rectangle.
        X-coordinate of lower - left corner.

        :param llx: The llx of this Rectangle.
        :type: float
        """
        if llx is None:
            raise ValueError("Invalid value for `llx`, must not be `None`")

        self._llx = llx

    @property
    def lly(self):
        """
        Gets the lly of this Rectangle.
        Y - coordinate of lower-left corner.

        :return: The lly of this Rectangle.
        :rtype: float
        """
        return self._lly

    @lly.setter
    def lly(self, lly):
        """
        Sets the lly of this Rectangle.
        Y - coordinate of lower-left corner.

        :param lly: The lly of this Rectangle.
        :type: float
        """
        if lly is None:
            raise ValueError("Invalid value for `lly`, must not be `None`")

        self._lly = lly

    @property
    def urx(self):
        """
        Gets the urx of this Rectangle.
        X - coordinate of upper-right corner.

        :return: The urx of this Rectangle.
        :rtype: float
        """
        return self._urx

    @urx.setter
    def urx(self, urx):
        """
        Sets the urx of this Rectangle.
        X - coordinate of upper-right corner.

        :param urx: The urx of this Rectangle.
        :type: float
        """
        if urx is None:
            raise ValueError("Invalid value for `urx`, must not be `None`")

        self._urx = urx

    @property
    def ury(self):
        """
        Gets the ury of this Rectangle.
        Y - coordinate of upper-right corner.

        :return: The ury of this Rectangle.
        :rtype: float
        """
        return self._ury

    @ury.setter
    def ury(self, ury):
        """
        Sets the ury of this Rectangle.
        Y - coordinate of upper-right corner.

        :param ury: The ury of this Rectangle.
        :type: float
        """
        if ury is None:
            raise ValueError("Invalid value for `ury`, must not be `None`")

        self._ury = ury

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
        if not isinstance(other, Rectangle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
