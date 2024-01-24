# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


Copyright (c) 2024 Aspose.PDF Cloud
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


class AttachmentInfo(object):
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
        'path': 'str',
        'description': 'str',
        'name': 'str',
        'mime_type': 'str'
    }

    attribute_map = {
        'path': 'Path',
        'description': 'Description',
        'name': 'Name',
        'mime_type': 'MimeType'
    }

    def __init__(self, path=None, description=None, name=None, mime_type=None):
        """
        AttachmentInfo - a model defined in Swagger
        """

        self._path = None
        self._description = None
        self._name = None
        self._mime_type = None

        self.path = path
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if mime_type is not None:
          self.mime_type = mime_type

    @property
    def path(self):
        """
        Gets the path of this AttachmentInfo.
        Attachment file path.

        :return: The path of this AttachmentInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this AttachmentInfo.
        Attachment file path.

        :param path: The path of this AttachmentInfo.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")
        if path is not None and len(path) < 1:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")

        self._path = path

    @property
    def description(self):
        """
        Gets the description of this AttachmentInfo.
        Attachment file description.

        :return: The description of this AttachmentInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AttachmentInfo.
        Attachment file description.

        :param description: The description of this AttachmentInfo.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this AttachmentInfo.
        Attachment file name.

        :return: The name of this AttachmentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AttachmentInfo.
        Attachment file name.

        :param name: The name of this AttachmentInfo.
        :type: str
        """

        self._name = name

    @property
    def mime_type(self):
        """
        Gets the mime_type of this AttachmentInfo.
        Attachment file MIME type.

        :return: The mime_type of this AttachmentInfo.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this AttachmentInfo.
        Attachment file MIME type.

        :param mime_type: The mime_type of this AttachmentInfo.
        :type: str
        """

        self._mime_type = mime_type

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
        if not isinstance(other, AttachmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
