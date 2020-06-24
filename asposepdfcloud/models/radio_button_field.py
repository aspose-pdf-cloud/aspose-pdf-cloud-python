# coding: utf-8

"""
    Aspose.PDF Cloud API Reference


   Copyright (c) 2020 Aspose.PDF Cloud
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


class RadioButtonField(object):
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
        'partial_name': 'str',
        'full_name': 'str',
        'rect': 'Rectangle',
        'value': 'str',
        'page_index': 'int',
        'height': 'float',
        'width': 'float',
        'z_index': 'int',
        'is_group': 'bool',
        'parent': 'FormField',
        'is_shared_field': 'bool',
        'flags': 'list[AnnotationFlags]',
        'color': 'Color',
        'contents': 'str',
        'margin': 'MarginInfo',
        'highlighting': 'LinkHighlightingMode',
        'horizontal_alignment': 'HorizontalAlignment',
        'vertical_alignment': 'VerticalAlignment',
        'border': 'Border',
        'multi_select': 'bool',
        'selected': 'int',
        'options': 'list[Option]',
        'radio_button_options_field': 'list[RadioButtonOptionField]',
        'style': 'BoxStyle'
    }

    attribute_map = {
        'links': 'Links',
        'partial_name': 'PartialName',
        'full_name': 'FullName',
        'rect': 'Rect',
        'value': 'Value',
        'page_index': 'PageIndex',
        'height': 'Height',
        'width': 'Width',
        'z_index': 'ZIndex',
        'is_group': 'IsGroup',
        'parent': 'Parent',
        'is_shared_field': 'IsSharedField',
        'flags': 'Flags',
        'color': 'Color',
        'contents': 'Contents',
        'margin': 'Margin',
        'highlighting': 'Highlighting',
        'horizontal_alignment': 'HorizontalAlignment',
        'vertical_alignment': 'VerticalAlignment',
        'border': 'Border',
        'multi_select': 'MultiSelect',
        'selected': 'Selected',
        'options': 'Options',
        'radio_button_options_field': 'RadioButtonOptionsField',
        'style': 'Style'
    }

    def __init__(self, links=None, partial_name=None, full_name=None, rect=None, value=None, page_index=None, height=None, width=None, z_index=None, is_group=None, parent=None, is_shared_field=None, flags=None, color=None, contents=None, margin=None, highlighting=None, horizontal_alignment=None, vertical_alignment=None, border=None, multi_select=None, selected=None, options=None, radio_button_options_field=None, style=None):
        """
        RadioButtonField - a model defined in Swagger
        """

        self._links = None
        self._partial_name = None
        self._full_name = None
        self._rect = None
        self._value = None
        self._page_index = None
        self._height = None
        self._width = None
        self._z_index = None
        self._is_group = None
        self._parent = None
        self._is_shared_field = None
        self._flags = None
        self._color = None
        self._contents = None
        self._margin = None
        self._highlighting = None
        self._horizontal_alignment = None
        self._vertical_alignment = None
        self._border = None
        self._multi_select = None
        self._selected = None
        self._options = None
        self._radio_button_options_field = None
        self._style = None

        if links is not None:
          self.links = links
        if partial_name is not None:
          self.partial_name = partial_name
        if full_name is not None:
          self.full_name = full_name
        if rect is not None:
          self.rect = rect
        if value is not None:
          self.value = value
        self.page_index = page_index
        if height is not None:
          self.height = height
        if width is not None:
          self.width = width
        if z_index is not None:
          self.z_index = z_index
        if is_group is not None:
          self.is_group = is_group
        if parent is not None:
          self.parent = parent
        if is_shared_field is not None:
          self.is_shared_field = is_shared_field
        if flags is not None:
          self.flags = flags
        if color is not None:
          self.color = color
        if contents is not None:
          self.contents = contents
        if margin is not None:
          self.margin = margin
        if highlighting is not None:
          self.highlighting = highlighting
        if horizontal_alignment is not None:
          self.horizontal_alignment = horizontal_alignment
        if vertical_alignment is not None:
          self.vertical_alignment = vertical_alignment
        if border is not None:
          self.border = border
        if multi_select is not None:
          self.multi_select = multi_select
        if selected is not None:
          self.selected = selected
        if options is not None:
          self.options = options
        if radio_button_options_field is not None:
          self.radio_button_options_field = radio_button_options_field
        if style is not None:
          self.style = style

    @property
    def links(self):
        """
        Gets the links of this RadioButtonField.
        Link to the document.

        :return: The links of this RadioButtonField.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this RadioButtonField.
        Link to the document.

        :param links: The links of this RadioButtonField.
        :type: list[Link]
        """

        self._links = links

    @property
    def partial_name(self):
        """
        Gets the partial_name of this RadioButtonField.
        Field name.

        :return: The partial_name of this RadioButtonField.
        :rtype: str
        """
        return self._partial_name

    @partial_name.setter
    def partial_name(self, partial_name):
        """
        Sets the partial_name of this RadioButtonField.
        Field name.

        :param partial_name: The partial_name of this RadioButtonField.
        :type: str
        """

        self._partial_name = partial_name

    @property
    def full_name(self):
        """
        Gets the full_name of this RadioButtonField.
        Full Field name.

        :return: The full_name of this RadioButtonField.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this RadioButtonField.
        Full Field name.

        :param full_name: The full_name of this RadioButtonField.
        :type: str
        """

        self._full_name = full_name

    @property
    def rect(self):
        """
        Gets the rect of this RadioButtonField.
        Field rectangle.

        :return: The rect of this RadioButtonField.
        :rtype: Rectangle
        """
        return self._rect

    @rect.setter
    def rect(self, rect):
        """
        Sets the rect of this RadioButtonField.
        Field rectangle.

        :param rect: The rect of this RadioButtonField.
        :type: Rectangle
        """

        self._rect = rect

    @property
    def value(self):
        """
        Gets the value of this RadioButtonField.
        Field value.

        :return: The value of this RadioButtonField.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this RadioButtonField.
        Field value.

        :param value: The value of this RadioButtonField.
        :type: str
        """

        self._value = value

    @property
    def page_index(self):
        """
        Gets the page_index of this RadioButtonField.
        Page index.

        :return: The page_index of this RadioButtonField.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """
        Sets the page_index of this RadioButtonField.
        Page index.

        :param page_index: The page_index of this RadioButtonField.
        :type: int
        """
        if page_index is None:
            raise ValueError("Invalid value for `page_index`, must not be `None`")

        self._page_index = page_index

    @property
    def height(self):
        """
        Gets the height of this RadioButtonField.
        Gets or sets height of the field.

        :return: The height of this RadioButtonField.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this RadioButtonField.
        Gets or sets height of the field.

        :param height: The height of this RadioButtonField.
        :type: float
        """

        self._height = height

    @property
    def width(self):
        """
        Gets the width of this RadioButtonField.
        Gets or sets width of the field.

        :return: The width of this RadioButtonField.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this RadioButtonField.
        Gets or sets width of the field.

        :param width: The width of this RadioButtonField.
        :type: float
        """

        self._width = width

    @property
    def z_index(self):
        """
        Gets the z_index of this RadioButtonField.
        Z index.

        :return: The z_index of this RadioButtonField.
        :rtype: int
        """
        return self._z_index

    @z_index.setter
    def z_index(self, z_index):
        """
        Sets the z_index of this RadioButtonField.
        Z index.

        :param z_index: The z_index of this RadioButtonField.
        :type: int
        """

        self._z_index = z_index

    @property
    def is_group(self):
        """
        Gets the is_group of this RadioButtonField.
        Is group.

        :return: The is_group of this RadioButtonField.
        :rtype: bool
        """
        return self._is_group

    @is_group.setter
    def is_group(self, is_group):
        """
        Sets the is_group of this RadioButtonField.
        Is group.

        :param is_group: The is_group of this RadioButtonField.
        :type: bool
        """

        self._is_group = is_group

    @property
    def parent(self):
        """
        Gets the parent of this RadioButtonField.
        Gets field parent.

        :return: The parent of this RadioButtonField.
        :rtype: FormField
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this RadioButtonField.
        Gets field parent.

        :param parent: The parent of this RadioButtonField.
        :type: FormField
        """

        self._parent = parent

    @property
    def is_shared_field(self):
        """
        Gets the is_shared_field of this RadioButtonField.
        Property for Generator support. Used when field is added to header or footer. If true, this field will created once and it's appearance will be visible on all pages of the document. If false, separated field will be created for every document page.

        :return: The is_shared_field of this RadioButtonField.
        :rtype: bool
        """
        return self._is_shared_field

    @is_shared_field.setter
    def is_shared_field(self, is_shared_field):
        """
        Sets the is_shared_field of this RadioButtonField.
        Property for Generator support. Used when field is added to header or footer. If true, this field will created once and it's appearance will be visible on all pages of the document. If false, separated field will be created for every document page.

        :param is_shared_field: The is_shared_field of this RadioButtonField.
        :type: bool
        """

        self._is_shared_field = is_shared_field

    @property
    def flags(self):
        """
        Gets the flags of this RadioButtonField.
        Gets Flags of the field.

        :return: The flags of this RadioButtonField.
        :rtype: list[AnnotationFlags]
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """
        Sets the flags of this RadioButtonField.
        Gets Flags of the field.

        :param flags: The flags of this RadioButtonField.
        :type: list[AnnotationFlags]
        """

        self._flags = flags

    @property
    def color(self):
        """
        Gets the color of this RadioButtonField.
        Color of the annotation.

        :return: The color of this RadioButtonField.
        :rtype: Color
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this RadioButtonField.
        Color of the annotation.

        :param color: The color of this RadioButtonField.
        :type: Color
        """

        self._color = color

    @property
    def contents(self):
        """
        Gets the contents of this RadioButtonField.
        Get the field content.

        :return: The contents of this RadioButtonField.
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """
        Sets the contents of this RadioButtonField.
        Get the field content.

        :param contents: The contents of this RadioButtonField.
        :type: str
        """

        self._contents = contents

    @property
    def margin(self):
        """
        Gets the margin of this RadioButtonField.
        Gets or sets a outer margin for paragraph (for pdf generation)

        :return: The margin of this RadioButtonField.
        :rtype: MarginInfo
        """
        return self._margin

    @margin.setter
    def margin(self, margin):
        """
        Sets the margin of this RadioButtonField.
        Gets or sets a outer margin for paragraph (for pdf generation)

        :param margin: The margin of this RadioButtonField.
        :type: MarginInfo
        """

        self._margin = margin

    @property
    def highlighting(self):
        """
        Gets the highlighting of this RadioButtonField.
        Field highlighting mode.

        :return: The highlighting of this RadioButtonField.
        :rtype: LinkHighlightingMode
        """
        return self._highlighting

    @highlighting.setter
    def highlighting(self, highlighting):
        """
        Sets the highlighting of this RadioButtonField.
        Field highlighting mode.

        :param highlighting: The highlighting of this RadioButtonField.
        :type: LinkHighlightingMode
        """

        self._highlighting = highlighting

    @property
    def horizontal_alignment(self):
        """
        Gets the horizontal_alignment of this RadioButtonField.
        Gets HorizontalAlignment of the field.

        :return: The horizontal_alignment of this RadioButtonField.
        :rtype: HorizontalAlignment
        """
        return self._horizontal_alignment

    @horizontal_alignment.setter
    def horizontal_alignment(self, horizontal_alignment):
        """
        Sets the horizontal_alignment of this RadioButtonField.
        Gets HorizontalAlignment of the field.

        :param horizontal_alignment: The horizontal_alignment of this RadioButtonField.
        :type: HorizontalAlignment
        """

        self._horizontal_alignment = horizontal_alignment

    @property
    def vertical_alignment(self):
        """
        Gets the vertical_alignment of this RadioButtonField.
        Gets VerticalAlignment of the field.

        :return: The vertical_alignment of this RadioButtonField.
        :rtype: VerticalAlignment
        """
        return self._vertical_alignment

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """
        Sets the vertical_alignment of this RadioButtonField.
        Gets VerticalAlignment of the field.

        :param vertical_alignment: The vertical_alignment of this RadioButtonField.
        :type: VerticalAlignment
        """

        self._vertical_alignment = vertical_alignment

    @property
    def border(self):
        """
        Gets the border of this RadioButtonField.
        Gets or sets annotation border characteristics.

        :return: The border of this RadioButtonField.
        :rtype: Border
        """
        return self._border

    @border.setter
    def border(self, border):
        """
        Sets the border of this RadioButtonField.
        Gets or sets annotation border characteristics.

        :param border: The border of this RadioButtonField.
        :type: Border
        """

        self._border = border

    @property
    def multi_select(self):
        """
        Gets the multi_select of this RadioButtonField.
        Gets or sets multiselection flag.

        :return: The multi_select of this RadioButtonField.
        :rtype: bool
        """
        return self._multi_select

    @multi_select.setter
    def multi_select(self, multi_select):
        """
        Sets the multi_select of this RadioButtonField.
        Gets or sets multiselection flag.

        :param multi_select: The multi_select of this RadioButtonField.
        :type: bool
        """

        self._multi_select = multi_select

    @property
    def selected(self):
        """
        Gets the selected of this RadioButtonField.
        Gets or sets index of selected item. Numbering of items is started from 1.

        :return: The selected of this RadioButtonField.
        :rtype: int
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """
        Sets the selected of this RadioButtonField.
        Gets or sets index of selected item. Numbering of items is started from 1.

        :param selected: The selected of this RadioButtonField.
        :type: int
        """

        self._selected = selected

    @property
    def options(self):
        """
        Gets the options of this RadioButtonField.
        Gets collection of options of the radio button.

        :return: The options of this RadioButtonField.
        :rtype: list[Option]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this RadioButtonField.
        Gets collection of options of the radio button.

        :param options: The options of this RadioButtonField.
        :type: list[Option]
        """

        self._options = options

    @property
    def radio_button_options_field(self):
        """
        Gets the radio_button_options_field of this RadioButtonField.
        Gets collection of radio button options field.

        :return: The radio_button_options_field of this RadioButtonField.
        :rtype: list[RadioButtonOptionField]
        """
        return self._radio_button_options_field

    @radio_button_options_field.setter
    def radio_button_options_field(self, radio_button_options_field):
        """
        Sets the radio_button_options_field of this RadioButtonField.
        Gets collection of radio button options field.

        :param radio_button_options_field: The radio_button_options_field of this RadioButtonField.
        :type: list[RadioButtonOptionField]
        """

        self._radio_button_options_field = radio_button_options_field

    @property
    def style(self):
        """
        Gets the style of this RadioButtonField.
        Style of field box.

        :return: The style of this RadioButtonField.
        :rtype: BoxStyle
        """
        return self._style

    @style.setter
    def style(self, style):
        """
        Sets the style of this RadioButtonField.
        Style of field box.

        :param style: The style of this RadioButtonField.
        :type: BoxStyle
        """

        self._style = style

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
        if not isinstance(other, RadioButtonField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
