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


class SignatureCustomAppearance(object):
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
        'font_family_name': 'str',
        'font_size': 'float',
        'show_contact_info': 'bool',
        'show_reason': 'bool',
        'show_location': 'bool',
        'contact_info_label': 'str',
        'reason_label': 'str',
        'location_label': 'str',
        'digital_signed_label': 'str',
        'date_signed_at_label': 'str',
        'date_time_local_format': 'str',
        'date_time_format': 'str'
    }

    attribute_map = {
        'font_family_name': 'FontFamilyName',
        'font_size': 'FontSize',
        'show_contact_info': 'ShowContactInfo',
        'show_reason': 'ShowReason',
        'show_location': 'ShowLocation',
        'contact_info_label': 'ContactInfoLabel',
        'reason_label': 'ReasonLabel',
        'location_label': 'LocationLabel',
        'digital_signed_label': 'DigitalSignedLabel',
        'date_signed_at_label': 'DateSignedAtLabel',
        'date_time_local_format': 'DateTimeLocalFormat',
        'date_time_format': 'DateTimeFormat'
    }

    def __init__(self, font_family_name=None, font_size=None, show_contact_info=None, show_reason=None, show_location=None, contact_info_label=None, reason_label=None, location_label=None, digital_signed_label=None, date_signed_at_label=None, date_time_local_format=None, date_time_format=None):
        """
        SignatureCustomAppearance - a model defined in Swagger
        """

        self._font_family_name = None
        self._font_size = None
        self._show_contact_info = None
        self._show_reason = None
        self._show_location = None
        self._contact_info_label = None
        self._reason_label = None
        self._location_label = None
        self._digital_signed_label = None
        self._date_signed_at_label = None
        self._date_time_local_format = None
        self._date_time_format = None

        if font_family_name is not None:
          self.font_family_name = font_family_name
        self.font_size = font_size
        self.show_contact_info = show_contact_info
        self.show_reason = show_reason
        self.show_location = show_location
        if contact_info_label is not None:
          self.contact_info_label = contact_info_label
        if reason_label is not None:
          self.reason_label = reason_label
        if location_label is not None:
          self.location_label = location_label
        if digital_signed_label is not None:
          self.digital_signed_label = digital_signed_label
        if date_signed_at_label is not None:
          self.date_signed_at_label = date_signed_at_label
        if date_time_local_format is not None:
          self.date_time_local_format = date_time_local_format
        if date_time_format is not None:
          self.date_time_format = date_time_format

    @property
    def font_family_name(self):
        """
        Gets the font_family_name of this SignatureCustomAppearance.
        Gets/sets font family name. It should be existed in the document. Default value: Arial.

        :return: The font_family_name of this SignatureCustomAppearance.
        :rtype: str
        """
        return self._font_family_name

    @font_family_name.setter
    def font_family_name(self, font_family_name):
        """
        Sets the font_family_name of this SignatureCustomAppearance.
        Gets/sets font family name. It should be existed in the document. Default value: Arial.

        :param font_family_name: The font_family_name of this SignatureCustomAppearance.
        :type: str
        """

        self._font_family_name = font_family_name

    @property
    def font_size(self):
        """
        Gets the font_size of this SignatureCustomAppearance.
        Gets/sets font size. Default value: 10.

        :return: The font_size of this SignatureCustomAppearance.
        :rtype: float
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """
        Sets the font_size of this SignatureCustomAppearance.
        Gets/sets font size. Default value: 10.

        :param font_size: The font_size of this SignatureCustomAppearance.
        :type: float
        """
        if font_size is None:
            raise ValueError("Invalid value for `font_size`, must not be `None`")

        self._font_size = font_size

    @property
    def show_contact_info(self):
        """
        Gets the show_contact_info of this SignatureCustomAppearance.
        Gets/sets contact info visibility. Default value: true.

        :return: The show_contact_info of this SignatureCustomAppearance.
        :rtype: bool
        """
        return self._show_contact_info

    @show_contact_info.setter
    def show_contact_info(self, show_contact_info):
        """
        Sets the show_contact_info of this SignatureCustomAppearance.
        Gets/sets contact info visibility. Default value: true.

        :param show_contact_info: The show_contact_info of this SignatureCustomAppearance.
        :type: bool
        """
        if show_contact_info is None:
            raise ValueError("Invalid value for `show_contact_info`, must not be `None`")

        self._show_contact_info = show_contact_info

    @property
    def show_reason(self):
        """
        Gets the show_reason of this SignatureCustomAppearance.
        Gets/sets reason visibility. Default value: true.

        :return: The show_reason of this SignatureCustomAppearance.
        :rtype: bool
        """
        return self._show_reason

    @show_reason.setter
    def show_reason(self, show_reason):
        """
        Sets the show_reason of this SignatureCustomAppearance.
        Gets/sets reason visibility. Default value: true.

        :param show_reason: The show_reason of this SignatureCustomAppearance.
        :type: bool
        """
        if show_reason is None:
            raise ValueError("Invalid value for `show_reason`, must not be `None`")

        self._show_reason = show_reason

    @property
    def show_location(self):
        """
        Gets the show_location of this SignatureCustomAppearance.
        Gets/sets location visibility. Default value: true.

        :return: The show_location of this SignatureCustomAppearance.
        :rtype: bool
        """
        return self._show_location

    @show_location.setter
    def show_location(self, show_location):
        """
        Sets the show_location of this SignatureCustomAppearance.
        Gets/sets location visibility. Default value: true.

        :param show_location: The show_location of this SignatureCustomAppearance.
        :type: bool
        """
        if show_location is None:
            raise ValueError("Invalid value for `show_location`, must not be `None`")

        self._show_location = show_location

    @property
    def contact_info_label(self):
        """
        Gets the contact_info_label of this SignatureCustomAppearance.
        Gets/sets contact info label. Default value: \"Contact\".

        :return: The contact_info_label of this SignatureCustomAppearance.
        :rtype: str
        """
        return self._contact_info_label

    @contact_info_label.setter
    def contact_info_label(self, contact_info_label):
        """
        Sets the contact_info_label of this SignatureCustomAppearance.
        Gets/sets contact info label. Default value: \"Contact\".

        :param contact_info_label: The contact_info_label of this SignatureCustomAppearance.
        :type: str
        """

        self._contact_info_label = contact_info_label

    @property
    def reason_label(self):
        """
        Gets the reason_label of this SignatureCustomAppearance.
        Gets/sets reason label. Default value: \"Reason\".

        :return: The reason_label of this SignatureCustomAppearance.
        :rtype: str
        """
        return self._reason_label

    @reason_label.setter
    def reason_label(self, reason_label):
        """
        Sets the reason_label of this SignatureCustomAppearance.
        Gets/sets reason label. Default value: \"Reason\".

        :param reason_label: The reason_label of this SignatureCustomAppearance.
        :type: str
        """

        self._reason_label = reason_label

    @property
    def location_label(self):
        """
        Gets the location_label of this SignatureCustomAppearance.
        Gets/sets location label. Default value: \"Location\".

        :return: The location_label of this SignatureCustomAppearance.
        :rtype: str
        """
        return self._location_label

    @location_label.setter
    def location_label(self, location_label):
        """
        Sets the location_label of this SignatureCustomAppearance.
        Gets/sets location label. Default value: \"Location\".

        :param location_label: The location_label of this SignatureCustomAppearance.
        :type: str
        """

        self._location_label = location_label

    @property
    def digital_signed_label(self):
        """
        Gets the digital_signed_label of this SignatureCustomAppearance.
        Gets/sets digital signed label. Default value: \"Digitally signed by\".

        :return: The digital_signed_label of this SignatureCustomAppearance.
        :rtype: str
        """
        return self._digital_signed_label

    @digital_signed_label.setter
    def digital_signed_label(self, digital_signed_label):
        """
        Sets the digital_signed_label of this SignatureCustomAppearance.
        Gets/sets digital signed label. Default value: \"Digitally signed by\".

        :param digital_signed_label: The digital_signed_label of this SignatureCustomAppearance.
        :type: str
        """

        self._digital_signed_label = digital_signed_label

    @property
    def date_signed_at_label(self):
        """
        Gets the date_signed_at_label of this SignatureCustomAppearance.
        Gets/sets date signed label. Default value: \"Date\".

        :return: The date_signed_at_label of this SignatureCustomAppearance.
        :rtype: str
        """
        return self._date_signed_at_label

    @date_signed_at_label.setter
    def date_signed_at_label(self, date_signed_at_label):
        """
        Sets the date_signed_at_label of this SignatureCustomAppearance.
        Gets/sets date signed label. Default value: \"Date\".

        :param date_signed_at_label: The date_signed_at_label of this SignatureCustomAppearance.
        :type: str
        """

        self._date_signed_at_label = date_signed_at_label

    @property
    def date_time_local_format(self):
        """
        Gets the date_time_local_format of this SignatureCustomAppearance.
        Gets/sets datetime local format. Default value: \"yyyy.MM.dd HH:mm:ss zzz\".

        :return: The date_time_local_format of this SignatureCustomAppearance.
        :rtype: str
        """
        return self._date_time_local_format

    @date_time_local_format.setter
    def date_time_local_format(self, date_time_local_format):
        """
        Sets the date_time_local_format of this SignatureCustomAppearance.
        Gets/sets datetime local format. Default value: \"yyyy.MM.dd HH:mm:ss zzz\".

        :param date_time_local_format: The date_time_local_format of this SignatureCustomAppearance.
        :type: str
        """

        self._date_time_local_format = date_time_local_format

    @property
    def date_time_format(self):
        """
        Gets the date_time_format of this SignatureCustomAppearance.
        Gets/sets datetime format. Default value: \"yyyy.MM.dd HH:mm:ss\".

        :return: The date_time_format of this SignatureCustomAppearance.
        :rtype: str
        """
        return self._date_time_format

    @date_time_format.setter
    def date_time_format(self, date_time_format):
        """
        Sets the date_time_format of this SignatureCustomAppearance.
        Gets/sets datetime format. Default value: \"yyyy.MM.dd HH:mm:ss\".

        :param date_time_format: The date_time_format of this SignatureCustomAppearance.
        :type: str
        """

        self._date_time_format = date_time_format

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
        if not isinstance(other, SignatureCustomAppearance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
