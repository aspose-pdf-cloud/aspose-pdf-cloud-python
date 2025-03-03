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


class TextLine(object):
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
        'horizontal_alignment': 'TextHorizontalAlignment',
        'segments': 'list[Segment]'
    }

    attribute_map = {
        'horizontal_alignment': 'HorizontalAlignment',
        'segments': 'Segments'
    }

    def __init__(self, horizontal_alignment=None, segments=None):
        """
        TextLine - a model defined in Swagger
        """

        self._horizontal_alignment = None
        self._segments = None

        if horizontal_alignment is not None:
          self.horizontal_alignment = horizontal_alignment
        self.segments = segments

    @property
    def horizontal_alignment(self):
        """
        Gets the horizontal_alignment of this TextLine.
        Line's horizontal alignment

        :return: The horizontal_alignment of this TextLine.
        :rtype: TextHorizontalAlignment
        """
        return self._horizontal_alignment

    @horizontal_alignment.setter
    def horizontal_alignment(self, horizontal_alignment):
        """
        Sets the horizontal_alignment of this TextLine.
        Line's horizontal alignment

        :param horizontal_alignment: The horizontal_alignment of this TextLine.
        :type: TextHorizontalAlignment
        """

        self._horizontal_alignment = horizontal_alignment

    @property
    def segments(self):
        """
        Gets the segments of this TextLine.
        Segments that form the line. Every segment has its own formatting.

        :return: The segments of this TextLine.
        :rtype: list[Segment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """
        Sets the segments of this TextLine.
        Segments that form the line. Every segment has its own formatting.

        :param segments: The segments of this TextLine.
        :type: list[Segment]
        """
        if segments is None:
            raise ValueError("Invalid value for `segments`, must not be `None`")

        self._segments = segments

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
        if not isinstance(other, TextLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
