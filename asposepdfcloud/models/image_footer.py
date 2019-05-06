# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2019 Aspose.PDF Cloud
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


class ImageFooter(object):
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
        'links': 'list[Link]',
        'background': 'bool',
        'horizontal_alignment': 'HorizontalAlignment',
        'opacity': 'float',
        'rotate': 'Rotation',
        'rotate_angle': 'float',
        'x_indent': 'float',
        'y_indent': 'float',
        'zoom': 'float',
        'file_name': 'str',
        'width': 'float',
        'height': 'float',
        'bottom_margin': 'float',
        'left_margin': 'float',
        'right_margin': 'float'
    }

    attribute_map = {
        'links': 'Links',
        'background': 'Background',
        'horizontal_alignment': 'HorizontalAlignment',
        'opacity': 'Opacity',
        'rotate': 'Rotate',
        'rotate_angle': 'RotateAngle',
        'x_indent': 'XIndent',
        'y_indent': 'YIndent',
        'zoom': 'Zoom',
        'file_name': 'FileName',
        'width': 'Width',
        'height': 'Height',
        'bottom_margin': 'BottomMargin',
        'left_margin': 'LeftMargin',
        'right_margin': 'RightMargin'
    }

    def __init__(self, links=None, background=None, horizontal_alignment=None, opacity=None, rotate=None, rotate_angle=None, x_indent=None, y_indent=None, zoom=None, file_name=None, width=None, height=None, bottom_margin=None, left_margin=None, right_margin=None):
        """
        ImageFooter - a model defined in Swagger
        """

        self._links = None
        self._background = None
        self._horizontal_alignment = None
        self._opacity = None
        self._rotate = None
        self._rotate_angle = None
        self._x_indent = None
        self._y_indent = None
        self._zoom = None
        self._file_name = None
        self._width = None
        self._height = None
        self._bottom_margin = None
        self._left_margin = None
        self._right_margin = None

        if links is not None:
          self.links = links
        if background is not None:
          self.background = background
        if horizontal_alignment is not None:
          self.horizontal_alignment = horizontal_alignment
        if opacity is not None:
          self.opacity = opacity
        if rotate is not None:
          self.rotate = rotate
        if rotate_angle is not None:
          self.rotate_angle = rotate_angle
        if x_indent is not None:
          self.x_indent = x_indent
        if y_indent is not None:
          self.y_indent = y_indent
        if zoom is not None:
          self.zoom = zoom
        if file_name is not None:
          self.file_name = file_name
        if width is not None:
          self.width = width
        if height is not None:
          self.height = height
        if bottom_margin is not None:
          self.bottom_margin = bottom_margin
        if left_margin is not None:
          self.left_margin = left_margin
        if right_margin is not None:
          self.right_margin = right_margin

    @property
    def links(self):
        """
        Gets the links of this ImageFooter.
        Link to the document.

        :return: The links of this ImageFooter.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this ImageFooter.
        Link to the document.

        :param links: The links of this ImageFooter.
        :type: list[Link]
        """

        self._links = links

    @property
    def background(self):
        """
        Gets the background of this ImageFooter.
        Sets or gets a bool value that indicates the content is stamped as background. If the value is true, the stamp content is layed at the bottom. By defalt, the value is false, the stamp content is layed at the top.

        :return: The background of this ImageFooter.
        :rtype: bool
        """
        return self._background

    @background.setter
    def background(self, background):
        """
        Sets the background of this ImageFooter.
        Sets or gets a bool value that indicates the content is stamped as background. If the value is true, the stamp content is layed at the bottom. By defalt, the value is false, the stamp content is layed at the top.

        :param background: The background of this ImageFooter.
        :type: bool
        """

        self._background = background

    @property
    def horizontal_alignment(self):
        """
        Gets the horizontal_alignment of this ImageFooter.
        Gets or sets Horizontal alignment of stamp on the page. 

        :return: The horizontal_alignment of this ImageFooter.
        :rtype: HorizontalAlignment
        """
        return self._horizontal_alignment

    @horizontal_alignment.setter
    def horizontal_alignment(self, horizontal_alignment):
        """
        Sets the horizontal_alignment of this ImageFooter.
        Gets or sets Horizontal alignment of stamp on the page. 

        :param horizontal_alignment: The horizontal_alignment of this ImageFooter.
        :type: HorizontalAlignment
        """

        self._horizontal_alignment = horizontal_alignment

    @property
    def opacity(self):
        """
        Gets the opacity of this ImageFooter.
        Gets or sets a value to indicate the stamp opacity. The value is from 0.0 to 1.0. By default the value is 1.0.

        :return: The opacity of this ImageFooter.
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """
        Sets the opacity of this ImageFooter.
        Gets or sets a value to indicate the stamp opacity. The value is from 0.0 to 1.0. By default the value is 1.0.

        :param opacity: The opacity of this ImageFooter.
        :type: float
        """

        self._opacity = opacity

    @property
    def rotate(self):
        """
        Gets the rotate of this ImageFooter.
        Sets or gets the rotation of stamp content according  values. Note. This property is for set angles which are multiples of 90 degrees (0, 90, 180, 270 degrees). To set arbitrary angle use RotateAngle property.  If angle set by ArbitraryAngle is not multiple of 90 then Rotate property returns Rotation.None.

        :return: The rotate of this ImageFooter.
        :rtype: Rotation
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """
        Sets the rotate of this ImageFooter.
        Sets or gets the rotation of stamp content according  values. Note. This property is for set angles which are multiples of 90 degrees (0, 90, 180, 270 degrees). To set arbitrary angle use RotateAngle property.  If angle set by ArbitraryAngle is not multiple of 90 then Rotate property returns Rotation.None.

        :param rotate: The rotate of this ImageFooter.
        :type: Rotation
        """

        self._rotate = rotate

    @property
    def rotate_angle(self):
        """
        Gets the rotate_angle of this ImageFooter.
        Gets or sets rotate angle of stamp in degrees. This property allows to set arbitrary rotate angle. 

        :return: The rotate_angle of this ImageFooter.
        :rtype: float
        """
        return self._rotate_angle

    @rotate_angle.setter
    def rotate_angle(self, rotate_angle):
        """
        Sets the rotate_angle of this ImageFooter.
        Gets or sets rotate angle of stamp in degrees. This property allows to set arbitrary rotate angle. 

        :param rotate_angle: The rotate_angle of this ImageFooter.
        :type: float
        """

        self._rotate_angle = rotate_angle

    @property
    def x_indent(self):
        """
        Gets the x_indent of this ImageFooter.
        Horizontal stamp coordinate, starting from the left.

        :return: The x_indent of this ImageFooter.
        :rtype: float
        """
        return self._x_indent

    @x_indent.setter
    def x_indent(self, x_indent):
        """
        Sets the x_indent of this ImageFooter.
        Horizontal stamp coordinate, starting from the left.

        :param x_indent: The x_indent of this ImageFooter.
        :type: float
        """

        self._x_indent = x_indent

    @property
    def y_indent(self):
        """
        Gets the y_indent of this ImageFooter.
        Vertical stamp coordinate, starting from the bottom.

        :return: The y_indent of this ImageFooter.
        :rtype: float
        """
        return self._y_indent

    @y_indent.setter
    def y_indent(self, y_indent):
        """
        Sets the y_indent of this ImageFooter.
        Vertical stamp coordinate, starting from the bottom.

        :param y_indent: The y_indent of this ImageFooter.
        :type: float
        """

        self._y_indent = y_indent

    @property
    def zoom(self):
        """
        Gets the zoom of this ImageFooter.
        Zooming factor of the stamp. Allows to scale stamp.

        :return: The zoom of this ImageFooter.
        :rtype: float
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom of this ImageFooter.
        Zooming factor of the stamp. Allows to scale stamp.

        :param zoom: The zoom of this ImageFooter.
        :type: float
        """

        self._zoom = zoom

    @property
    def file_name(self):
        """
        Gets the file_name of this ImageFooter.
        Gets or sets the file name.

        :return: The file_name of this ImageFooter.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this ImageFooter.
        Gets or sets the file name.

        :param file_name: The file_name of this ImageFooter.
        :type: str
        """

        self._file_name = file_name

    @property
    def width(self):
        """
        Gets the width of this ImageFooter.
        Gets or sets image width. Setting this property allos to scal image horizontally.

        :return: The width of this ImageFooter.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this ImageFooter.
        Gets or sets image width. Setting this property allos to scal image horizontally.

        :param width: The width of this ImageFooter.
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this ImageFooter.
        Gets or sets image height. Setting this image allows to scale image vertically.

        :return: The height of this ImageFooter.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this ImageFooter.
        Gets or sets image height. Setting this image allows to scale image vertically.

        :param height: The height of this ImageFooter.
        :type: float
        """

        self._height = height

    @property
    def bottom_margin(self):
        """
        Gets the bottom_margin of this ImageFooter.
        Gets or sets bottom margin of stamp.

        :return: The bottom_margin of this ImageFooter.
        :rtype: float
        """
        return self._bottom_margin

    @bottom_margin.setter
    def bottom_margin(self, bottom_margin):
        """
        Sets the bottom_margin of this ImageFooter.
        Gets or sets bottom margin of stamp.

        :param bottom_margin: The bottom_margin of this ImageFooter.
        :type: float
        """

        self._bottom_margin = bottom_margin

    @property
    def left_margin(self):
        """
        Gets the left_margin of this ImageFooter.
        Gets or sets left margin of stamp.

        :return: The left_margin of this ImageFooter.
        :rtype: float
        """
        return self._left_margin

    @left_margin.setter
    def left_margin(self, left_margin):
        """
        Sets the left_margin of this ImageFooter.
        Gets or sets left margin of stamp.

        :param left_margin: The left_margin of this ImageFooter.
        :type: float
        """

        self._left_margin = left_margin

    @property
    def right_margin(self):
        """
        Gets the right_margin of this ImageFooter.
        Gets or sets right margin of stamp.

        :return: The right_margin of this ImageFooter.
        :rtype: float
        """
        return self._right_margin

    @right_margin.setter
    def right_margin(self, right_margin):
        """
        Sets the right_margin of this ImageFooter.
        Gets or sets right margin of stamp.

        :param right_margin: The right_margin of this ImageFooter.
        :type: float
        """

        self._right_margin = right_margin

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
        if not isinstance(other, ImageFooter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
