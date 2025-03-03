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


class DocumentPrivilege(object):
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
        'allow_print': 'bool',
        'allow_degraded_printing': 'bool',
        'allow_modify_contents': 'bool',
        'allow_copy': 'bool',
        'allow_modify_annotations': 'bool',
        'allow_fill_in': 'bool',
        'allow_screen_readers': 'bool',
        'allow_assembly': 'bool',
        'print_allow_level': 'int',
        'change_allow_level': 'int',
        'copy_allow_level': 'int'
    }

    attribute_map = {
        'allow_print': 'AllowPrint',
        'allow_degraded_printing': 'AllowDegradedPrinting',
        'allow_modify_contents': 'AllowModifyContents',
        'allow_copy': 'AllowCopy',
        'allow_modify_annotations': 'AllowModifyAnnotations',
        'allow_fill_in': 'AllowFillIn',
        'allow_screen_readers': 'AllowScreenReaders',
        'allow_assembly': 'AllowAssembly',
        'print_allow_level': 'PrintAllowLevel',
        'change_allow_level': 'ChangeAllowLevel',
        'copy_allow_level': 'CopyAllowLevel'
    }

    def __init__(self, allow_print=None, allow_degraded_printing=None, allow_modify_contents=None, allow_copy=None, allow_modify_annotations=None, allow_fill_in=None, allow_screen_readers=None, allow_assembly=None, print_allow_level=None, change_allow_level=None, copy_allow_level=None):
        """
        DocumentPrivilege - a model defined in Swagger
        """

        self._allow_print = None
        self._allow_degraded_printing = None
        self._allow_modify_contents = None
        self._allow_copy = None
        self._allow_modify_annotations = None
        self._allow_fill_in = None
        self._allow_screen_readers = None
        self._allow_assembly = None
        self._print_allow_level = None
        self._change_allow_level = None
        self._copy_allow_level = None

        if allow_print is not None:
          self.allow_print = allow_print
        if allow_degraded_printing is not None:
          self.allow_degraded_printing = allow_degraded_printing
        if allow_modify_contents is not None:
          self.allow_modify_contents = allow_modify_contents
        if allow_copy is not None:
          self.allow_copy = allow_copy
        if allow_modify_annotations is not None:
          self.allow_modify_annotations = allow_modify_annotations
        if allow_fill_in is not None:
          self.allow_fill_in = allow_fill_in
        if allow_screen_readers is not None:
          self.allow_screen_readers = allow_screen_readers
        if allow_assembly is not None:
          self.allow_assembly = allow_assembly
        if print_allow_level is not None:
          self.print_allow_level = print_allow_level
        if change_allow_level is not None:
          self.change_allow_level = change_allow_level
        if copy_allow_level is not None:
          self.copy_allow_level = copy_allow_level

    @property
    def allow_print(self):
        """
        Gets the allow_print of this DocumentPrivilege.
        Sets the permission which allow print or not.  true is allow and false or not set is forbidden.

        :return: The allow_print of this DocumentPrivilege.
        :rtype: bool
        """
        return self._allow_print

    @allow_print.setter
    def allow_print(self, allow_print):
        """
        Sets the allow_print of this DocumentPrivilege.
        Sets the permission which allow print or not.  true is allow and false or not set is forbidden.

        :param allow_print: The allow_print of this DocumentPrivilege.
        :type: bool
        """

        self._allow_print = allow_print

    @property
    def allow_degraded_printing(self):
        """
        Gets the allow_degraded_printing of this DocumentPrivilege.
        Sets the permission which allow degraded printing or not.  true is allow and false or not set is forbidden.

        :return: The allow_degraded_printing of this DocumentPrivilege.
        :rtype: bool
        """
        return self._allow_degraded_printing

    @allow_degraded_printing.setter
    def allow_degraded_printing(self, allow_degraded_printing):
        """
        Sets the allow_degraded_printing of this DocumentPrivilege.
        Sets the permission which allow degraded printing or not.  true is allow and false or not set is forbidden.

        :param allow_degraded_printing: The allow_degraded_printing of this DocumentPrivilege.
        :type: bool
        """

        self._allow_degraded_printing = allow_degraded_printing

    @property
    def allow_modify_contents(self):
        """
        Gets the allow_modify_contents of this DocumentPrivilege.
        Sets the permission which allow modify contents or not.  true is allow and false or not set is forbidden.

        :return: The allow_modify_contents of this DocumentPrivilege.
        :rtype: bool
        """
        return self._allow_modify_contents

    @allow_modify_contents.setter
    def allow_modify_contents(self, allow_modify_contents):
        """
        Sets the allow_modify_contents of this DocumentPrivilege.
        Sets the permission which allow modify contents or not.  true is allow and false or not set is forbidden.

        :param allow_modify_contents: The allow_modify_contents of this DocumentPrivilege.
        :type: bool
        """

        self._allow_modify_contents = allow_modify_contents

    @property
    def allow_copy(self):
        """
        Gets the allow_copy of this DocumentPrivilege.
        Sets the permission which allow copy or not.  true is allow and false or not set is forbidden.

        :return: The allow_copy of this DocumentPrivilege.
        :rtype: bool
        """
        return self._allow_copy

    @allow_copy.setter
    def allow_copy(self, allow_copy):
        """
        Sets the allow_copy of this DocumentPrivilege.
        Sets the permission which allow copy or not.  true is allow and false or not set is forbidden.

        :param allow_copy: The allow_copy of this DocumentPrivilege.
        :type: bool
        """

        self._allow_copy = allow_copy

    @property
    def allow_modify_annotations(self):
        """
        Gets the allow_modify_annotations of this DocumentPrivilege.
        Sets the permission which allow modify annotations or not.  true is allow and false or not set is forbidden.

        :return: The allow_modify_annotations of this DocumentPrivilege.
        :rtype: bool
        """
        return self._allow_modify_annotations

    @allow_modify_annotations.setter
    def allow_modify_annotations(self, allow_modify_annotations):
        """
        Sets the allow_modify_annotations of this DocumentPrivilege.
        Sets the permission which allow modify annotations or not.  true is allow and false or not set is forbidden.

        :param allow_modify_annotations: The allow_modify_annotations of this DocumentPrivilege.
        :type: bool
        """

        self._allow_modify_annotations = allow_modify_annotations

    @property
    def allow_fill_in(self):
        """
        Gets the allow_fill_in of this DocumentPrivilege.
        Sets the permission which allow fill in forms or not.  true is allow and false or not set is forbidden.

        :return: The allow_fill_in of this DocumentPrivilege.
        :rtype: bool
        """
        return self._allow_fill_in

    @allow_fill_in.setter
    def allow_fill_in(self, allow_fill_in):
        """
        Sets the allow_fill_in of this DocumentPrivilege.
        Sets the permission which allow fill in forms or not.  true is allow and false or not set is forbidden.

        :param allow_fill_in: The allow_fill_in of this DocumentPrivilege.
        :type: bool
        """

        self._allow_fill_in = allow_fill_in

    @property
    def allow_screen_readers(self):
        """
        Gets the allow_screen_readers of this DocumentPrivilege.
        Sets the permission which allow screen readers or not.  true is allow and false or not set is forbidden.

        :return: The allow_screen_readers of this DocumentPrivilege.
        :rtype: bool
        """
        return self._allow_screen_readers

    @allow_screen_readers.setter
    def allow_screen_readers(self, allow_screen_readers):
        """
        Sets the allow_screen_readers of this DocumentPrivilege.
        Sets the permission which allow screen readers or not.  true is allow and false or not set is forbidden.

        :param allow_screen_readers: The allow_screen_readers of this DocumentPrivilege.
        :type: bool
        """

        self._allow_screen_readers = allow_screen_readers

    @property
    def allow_assembly(self):
        """
        Gets the allow_assembly of this DocumentPrivilege.
        Sets the permission which allow assembly or not.  true is allow and false or not set is forbidden.

        :return: The allow_assembly of this DocumentPrivilege.
        :rtype: bool
        """
        return self._allow_assembly

    @allow_assembly.setter
    def allow_assembly(self, allow_assembly):
        """
        Sets the allow_assembly of this DocumentPrivilege.
        Sets the permission which allow assembly or not.  true is allow and false or not set is forbidden.

        :param allow_assembly: The allow_assembly of this DocumentPrivilege.
        :type: bool
        """

        self._allow_assembly = allow_assembly

    @property
    def print_allow_level(self):
        """
        Gets the print_allow_level of this DocumentPrivilege.
        Sets the print level of  document's privilege. Just as the Adobe Professional's Printing Allowed settings. 0: None. 1: Low Resolution (150 dpi). 2: High Resolution.

        :return: The print_allow_level of this DocumentPrivilege.
        :rtype: int
        """
        return self._print_allow_level

    @print_allow_level.setter
    def print_allow_level(self, print_allow_level):
        """
        Sets the print_allow_level of this DocumentPrivilege.
        Sets the print level of  document's privilege. Just as the Adobe Professional's Printing Allowed settings. 0: None. 1: Low Resolution (150 dpi). 2: High Resolution.

        :param print_allow_level: The print_allow_level of this DocumentPrivilege.
        :type: int
        """

        self._print_allow_level = print_allow_level

    @property
    def change_allow_level(self):
        """
        Gets the change_allow_level of this DocumentPrivilege.
        Sets the change level of  document's privilege. Just as the Adobe Professional's Changes Allowed settings. 0: None. 1: Inserting, Deleting and Rotating pages. 2: Filling in form fields and signing existing signature fields. 3: Commenting, filling in form fields, and signing existing signature fields. 4: Any except extracting pages.

        :return: The change_allow_level of this DocumentPrivilege.
        :rtype: int
        """
        return self._change_allow_level

    @change_allow_level.setter
    def change_allow_level(self, change_allow_level):
        """
        Sets the change_allow_level of this DocumentPrivilege.
        Sets the change level of  document's privilege. Just as the Adobe Professional's Changes Allowed settings. 0: None. 1: Inserting, Deleting and Rotating pages. 2: Filling in form fields and signing existing signature fields. 3: Commenting, filling in form fields, and signing existing signature fields. 4: Any except extracting pages.

        :param change_allow_level: The change_allow_level of this DocumentPrivilege.
        :type: int
        """

        self._change_allow_level = change_allow_level

    @property
    def copy_allow_level(self):
        """
        Gets the copy_allow_level of this DocumentPrivilege.
        Sets the copy level of  document's privilege. Just as the Adobe Professional's permission settings. 0: None. 1: Enable text access for screen reader devices for the visually impaired. 2: Enable copying of text, images and other content.

        :return: The copy_allow_level of this DocumentPrivilege.
        :rtype: int
        """
        return self._copy_allow_level

    @copy_allow_level.setter
    def copy_allow_level(self, copy_allow_level):
        """
        Sets the copy_allow_level of this DocumentPrivilege.
        Sets the copy level of  document's privilege. Just as the Adobe Professional's permission settings. 0: None. 1: Enable text access for screen reader devices for the visually impaired. 2: Enable copying of text, images and other content.

        :param copy_allow_level: The copy_allow_level of this DocumentPrivilege.
        :type: int
        """

        self._copy_allow_level = copy_allow_level

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
        if not isinstance(other, DocumentPrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
