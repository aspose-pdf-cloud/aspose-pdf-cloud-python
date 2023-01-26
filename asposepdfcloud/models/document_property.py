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


class DocumentProperty(object):
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
        'name': 'str',
        'value': 'str',
        'built_in': 'bool'
    }

    attribute_map = {
        'links': 'Links',
        'name': 'Name',
        'value': 'Value',
        'built_in': 'BuiltIn'
    }

    def __init__(self, links=None, name=None, value=None, built_in=None):
        """
        DocumentProperty - a model defined in Swagger
        """

        self._links = None
        self._name = None
        self._value = None
        self._built_in = None

        if links is not None:
          self.links = links
        if name is not None:
          self.name = name
        if value is not None:
          self.value = value
        self.built_in = built_in

    @property
    def links(self):
        """
        Gets the links of this DocumentProperty.
        Link to the document.

        :return: The links of this DocumentProperty.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this DocumentProperty.
        Link to the document.

        :param links: The links of this DocumentProperty.
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """
        Gets the name of this DocumentProperty.
        Name of the property.

        :return: The name of this DocumentProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DocumentProperty.
        Name of the property.

        :param name: The name of this DocumentProperty.
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """
        Gets the value of this DocumentProperty.
        Property value.

        :return: The value of this DocumentProperty.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DocumentProperty.
        Property value.

        :param value: The value of this DocumentProperty.
        :type: str
        """

        self._value = value

    @property
    def built_in(self):
        """
        Gets the built_in of this DocumentProperty.
        Value indicating whether it is a built-in property.

        :return: The built_in of this DocumentProperty.
        :rtype: bool
        """
        return self._built_in

    @built_in.setter
    def built_in(self, built_in):
        """
        Sets the built_in of this DocumentProperty.
        Value indicating whether it is a built-in property.

        :param built_in: The built_in of this DocumentProperty.
        :type: bool
        """
        if built_in is None:
            raise ValueError("Invalid value for `built_in`, must not be `None`")

        self._built_in = built_in

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
        if not isinstance(other, DocumentProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
