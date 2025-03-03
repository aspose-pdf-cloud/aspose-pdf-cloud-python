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


class BorderInfo(object):
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
        'left': 'GraphInfo',
        'right': 'GraphInfo',
        'top': 'GraphInfo',
        'bottom': 'GraphInfo',
        'rounded_border_radius': 'float'
    }

    attribute_map = {
        'left': 'Left',
        'right': 'Right',
        'top': 'Top',
        'bottom': 'Bottom',
        'rounded_border_radius': 'RoundedBorderRadius'
    }

    def __init__(self, left=None, right=None, top=None, bottom=None, rounded_border_radius=None):
        """
        BorderInfo - a model defined in Swagger
        """

        self._left = None
        self._right = None
        self._top = None
        self._bottom = None
        self._rounded_border_radius = None

        if left is not None:
          self.left = left
        if right is not None:
          self.right = right
        if top is not None:
          self.top = top
        if bottom is not None:
          self.bottom = bottom
        if rounded_border_radius is not None:
          self.rounded_border_radius = rounded_border_radius

    @property
    def left(self):
        """
        Gets the left of this BorderInfo.
        Gets or sets a object that indicates left of the border.

        :return: The left of this BorderInfo.
        :rtype: GraphInfo
        """
        return self._left

    @left.setter
    def left(self, left):
        """
        Sets the left of this BorderInfo.
        Gets or sets a object that indicates left of the border.

        :param left: The left of this BorderInfo.
        :type: GraphInfo
        """

        self._left = left

    @property
    def right(self):
        """
        Gets the right of this BorderInfo.
        Gets or sets a object that indicates right of the border.

        :return: The right of this BorderInfo.
        :rtype: GraphInfo
        """
        return self._right

    @right.setter
    def right(self, right):
        """
        Sets the right of this BorderInfo.
        Gets or sets a object that indicates right of the border.

        :param right: The right of this BorderInfo.
        :type: GraphInfo
        """

        self._right = right

    @property
    def top(self):
        """
        Gets the top of this BorderInfo.
        Gets or sets a object that indicates the top border.

        :return: The top of this BorderInfo.
        :rtype: GraphInfo
        """
        return self._top

    @top.setter
    def top(self, top):
        """
        Sets the top of this BorderInfo.
        Gets or sets a object that indicates the top border.

        :param top: The top of this BorderInfo.
        :type: GraphInfo
        """

        self._top = top

    @property
    def bottom(self):
        """
        Gets the bottom of this BorderInfo.
        Gets or sets a object that indicates bottom of the border.

        :return: The bottom of this BorderInfo.
        :rtype: GraphInfo
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """
        Sets the bottom of this BorderInfo.
        Gets or sets a object that indicates bottom of the border.

        :param bottom: The bottom of this BorderInfo.
        :type: GraphInfo
        """

        self._bottom = bottom

    @property
    def rounded_border_radius(self):
        """
        Gets the rounded_border_radius of this BorderInfo.
        Gets or sets a rouded border radius

        :return: The rounded_border_radius of this BorderInfo.
        :rtype: float
        """
        return self._rounded_border_radius

    @rounded_border_radius.setter
    def rounded_border_radius(self, rounded_border_radius):
        """
        Sets the rounded_border_radius of this BorderInfo.
        Gets or sets a rouded border radius

        :param rounded_border_radius: The rounded_border_radius of this BorderInfo.
        :type: float
        """

        self._rounded_border_radius = rounded_border_radius

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
        if not isinstance(other, BorderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
