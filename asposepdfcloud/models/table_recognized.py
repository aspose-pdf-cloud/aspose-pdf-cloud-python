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


class TableRecognized(object):
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
        'row_list': 'list[RowRecognized]',
        'rectangle': 'Rectangle',
        'page_num': 'int',
        'id': 'str'
    }

    attribute_map = {
        'links': 'Links',
        'row_list': 'RowList',
        'rectangle': 'Rectangle',
        'page_num': 'PageNum',
        'id': 'Id'
    }

    def __init__(self, links=None, row_list=None, rectangle=None, page_num=None, id=None):
        """
        TableRecognized - a model defined in Swagger
        """

        self._links = None
        self._row_list = None
        self._rectangle = None
        self._page_num = None
        self._id = None

        if links is not None:
          self.links = links
        if row_list is not None:
          self.row_list = row_list
        if rectangle is not None:
          self.rectangle = rectangle
        if page_num is not None:
          self.page_num = page_num
        if id is not None:
          self.id = id

    @property
    def links(self):
        """
        Gets the links of this TableRecognized.
        Link to the document.

        :return: The links of this TableRecognized.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this TableRecognized.
        Link to the document.

        :param links: The links of this TableRecognized.
        :type: list[Link]
        """

        self._links = links

    @property
    def row_list(self):
        """
        Gets the row_list of this TableRecognized.
        Gets readonly IList containing rows of the table

        :return: The row_list of this TableRecognized.
        :rtype: list[RowRecognized]
        """
        return self._row_list

    @row_list.setter
    def row_list(self, row_list):
        """
        Sets the row_list of this TableRecognized.
        Gets readonly IList containing rows of the table

        :param row_list: The row_list of this TableRecognized.
        :type: list[RowRecognized]
        """

        self._row_list = row_list

    @property
    def rectangle(self):
        """
        Gets the rectangle of this TableRecognized.
        Gets rectangle that describes position of the table on page

        :return: The rectangle of this TableRecognized.
        :rtype: Rectangle
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, rectangle):
        """
        Sets the rectangle of this TableRecognized.
        Gets rectangle that describes position of the table on page

        :param rectangle: The rectangle of this TableRecognized.
        :type: Rectangle
        """

        self._rectangle = rectangle

    @property
    def page_num(self):
        """
        Gets the page_num of this TableRecognized.
        Gets number of the page containing this table

        :return: The page_num of this TableRecognized.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """
        Sets the page_num of this TableRecognized.
        Gets number of the page containing this table

        :param page_num: The page_num of this TableRecognized.
        :type: int
        """

        self._page_num = page_num

    @property
    def id(self):
        """
        Gets the id of this TableRecognized.
        Gets ID of the table.

        :return: The id of this TableRecognized.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TableRecognized.
        Gets ID of the table.

        :param id: The id of this TableRecognized.
        :type: str
        """

        self._id = id

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
        if not isinstance(other, TableRecognized):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
