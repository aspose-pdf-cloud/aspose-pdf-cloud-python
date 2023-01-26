# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


Copyright (c) 2023 Aspose.PDF Cloud
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


class ImageFragment(object):
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
        'image_file': 'str',
        'fix_width': 'float',
        'fix_height': 'float',
        'horizontal_alignment': 'HorizontalAlignment',
        'vertical_alignment': 'VerticalAlignment',
        'image_scale': 'float',
        'margin': 'MarginInfo'
    }

    attribute_map = {
        'image_file': 'ImageFile',
        'fix_width': 'FixWidth',
        'fix_height': 'FixHeight',
        'horizontal_alignment': 'HorizontalAlignment',
        'vertical_alignment': 'VerticalAlignment',
        'image_scale': 'ImageScale',
        'margin': 'Margin'
    }

    def __init__(self, image_file=None, fix_width=None, fix_height=None, horizontal_alignment=None, vertical_alignment=None, image_scale=None, margin=None):
        """
        ImageFragment - a model defined in Swagger
        """

        self._image_file = None
        self._fix_width = None
        self._fix_height = None
        self._horizontal_alignment = None
        self._vertical_alignment = None
        self._image_scale = None
        self._margin = None

        self.image_file = image_file
        if fix_width is not None:
          self.fix_width = fix_width
        if fix_height is not None:
          self.fix_height = fix_height
        if horizontal_alignment is not None:
          self.horizontal_alignment = horizontal_alignment
        if vertical_alignment is not None:
          self.vertical_alignment = vertical_alignment
        if image_scale is not None:
          self.image_scale = image_scale
        if margin is not None:
          self.margin = margin

    @property
    def image_file(self):
        """
        Gets the image_file of this ImageFragment.
        Gets or sets full storage path of image.

        :return: The image_file of this ImageFragment.
        :rtype: str
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        """
        Sets the image_file of this ImageFragment.
        Gets or sets full storage path of image.

        :param image_file: The image_file of this ImageFragment.
        :type: str
        """
        if image_file is None:
            raise ValueError("Invalid value for `image_file`, must not be `None`")
        if image_file is not None and len(image_file) < 1:
            raise ValueError("Invalid value for `image_file`, length must be greater than or equal to `1`")

        self._image_file = image_file

    @property
    def fix_width(self):
        """
        Gets the fix_width of this ImageFragment.
        Gets or sets fix width of the image.

        :return: The fix_width of this ImageFragment.
        :rtype: float
        """
        return self._fix_width

    @fix_width.setter
    def fix_width(self, fix_width):
        """
        Sets the fix_width of this ImageFragment.
        Gets or sets fix width of the image.

        :param fix_width: The fix_width of this ImageFragment.
        :type: float
        """

        self._fix_width = fix_width

    @property
    def fix_height(self):
        """
        Gets the fix_height of this ImageFragment.
        Gets or sets fix height of the image.

        :return: The fix_height of this ImageFragment.
        :rtype: float
        """
        return self._fix_height

    @fix_height.setter
    def fix_height(self, fix_height):
        """
        Sets the fix_height of this ImageFragment.
        Gets or sets fix height of the image.

        :param fix_height: The fix_height of this ImageFragment.
        :type: float
        """

        self._fix_height = fix_height

    @property
    def horizontal_alignment(self):
        """
        Gets the horizontal_alignment of this ImageFragment.
        Gets or sets horizontal alignment of the image.

        :return: The horizontal_alignment of this ImageFragment.
        :rtype: HorizontalAlignment
        """
        return self._horizontal_alignment

    @horizontal_alignment.setter
    def horizontal_alignment(self, horizontal_alignment):
        """
        Sets the horizontal_alignment of this ImageFragment.
        Gets or sets horizontal alignment of the image.

        :param horizontal_alignment: The horizontal_alignment of this ImageFragment.
        :type: HorizontalAlignment
        """

        self._horizontal_alignment = horizontal_alignment

    @property
    def vertical_alignment(self):
        """
        Gets the vertical_alignment of this ImageFragment.
        Gets or sets vertical alignment of the image.

        :return: The vertical_alignment of this ImageFragment.
        :rtype: VerticalAlignment
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """
        Sets the vertical_alignment of this ImageFragment.
        Gets or sets vertical alignment of the image.

        :param vertical_alignment: The vertical_alignment of this ImageFragment.
        :type: VerticalAlignment
        """

        self._vertical_alignment = vertical_alignment

    @property
    def image_scale(self):
        """
        Gets the image_scale of this ImageFragment.
        Gets or sets ImageScale of the image.

        :return: The image_scale of this ImageFragment.
        :rtype: float
        """
        return self._image_scale

    @image_scale.setter
    def image_scale(self, image_scale):
        """
        Sets the image_scale of this ImageFragment.
        Gets or sets ImageScale of the image.

        :param image_scale: The image_scale of this ImageFragment.
        :type: float
        """

        self._image_scale = image_scale

    @property
    def margin(self):
        """
        Gets the margin of this ImageFragment.
        Gets or sets Margin of the image.

        :return: The margin of this ImageFragment.
        :rtype: MarginInfo
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """
        Sets the margin of this ImageFragment.
        Gets or sets Margin of the image.

        :param margin: The margin of this ImageFragment.
        :type: MarginInfo
        """

        self._margin = margin

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
        if not isinstance(other, ImageFragment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
