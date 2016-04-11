# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class FormatTest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FormatTest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'integer': 'int',
            'int32': 'int',
            'int64': 'int',
            'number': 'float',
            'float': 'float',
            'double': 'float',
            'string': 'str',
            'byte': 'str',
            'binary': 'str',
            'date': 'date',
            'date_time': 'str'
        }

        self.attribute_map = {
            'integer': 'integer',
            'int32': 'int32',
            'int64': 'int64',
            'number': 'number',
            'float': 'float',
            'double': 'double',
            'string': 'string',
            'byte': 'byte',
            'binary': 'binary',
            'date': 'date',
            'date_time': 'dateTime'
        }

        self._integer = None
        self._int32 = None
        self._int64 = None
        self._number = None
        self._float = None
        self._double = None
        self._string = None
        self._byte = None
        self._binary = None
        self._date = None
        self._date_time = None

    @property
    def integer(self):
        """
        Gets the integer of this FormatTest.


        :return: The integer of this FormatTest.
        :rtype: int
        """
        return self._integer

    @integer.setter
    def integer(self, integer):
        """
        Sets the integer of this FormatTest.


        :param integer: The integer of this FormatTest.
        :type: int
        """
        self._integer = integer

    @property
    def int32(self):
        """
        Gets the int32 of this FormatTest.


        :return: The int32 of this FormatTest.
        :rtype: int
        """
        return self._int32

    @int32.setter
    def int32(self, int32):
        """
        Sets the int32 of this FormatTest.


        :param int32: The int32 of this FormatTest.
        :type: int
        """
        self._int32 = int32

    @property
    def int64(self):
        """
        Gets the int64 of this FormatTest.


        :return: The int64 of this FormatTest.
        :rtype: int
        """
        return self._int64

    @int64.setter
    def int64(self, int64):
        """
        Sets the int64 of this FormatTest.


        :param int64: The int64 of this FormatTest.
        :type: int
        """
        self._int64 = int64

    @property
    def number(self):
        """
        Gets the number of this FormatTest.


        :return: The number of this FormatTest.
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this FormatTest.


        :param number: The number of this FormatTest.
        :type: float
        """
        self._number = number

    @property
    def float(self):
        """
        Gets the float of this FormatTest.


        :return: The float of this FormatTest.
        :rtype: float
        """
        return self._float

    @float.setter
    def float(self, float):
        """
        Sets the float of this FormatTest.


        :param float: The float of this FormatTest.
        :type: float
        """
        self._float = float

    @property
    def double(self):
        """
        Gets the double of this FormatTest.


        :return: The double of this FormatTest.
        :rtype: float
        """
        return self._double

    @double.setter
    def double(self, double):
        """
        Sets the double of this FormatTest.


        :param double: The double of this FormatTest.
        :type: float
        """
        self._double = double

    @property
    def string(self):
        """
        Gets the string of this FormatTest.


        :return: The string of this FormatTest.
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """
        Sets the string of this FormatTest.


        :param string: The string of this FormatTest.
        :type: str
        """
        self._string = string

    @property
    def byte(self):
        """
        Gets the byte of this FormatTest.


        :return: The byte of this FormatTest.
        :rtype: str
        """
        return self._byte

    @byte.setter
    def byte(self, byte):
        """
        Sets the byte of this FormatTest.


        :param byte: The byte of this FormatTest.
        :type: str
        """
        self._byte = byte

    @property
    def binary(self):
        """
        Gets the binary of this FormatTest.


        :return: The binary of this FormatTest.
        :rtype: str
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """
        Sets the binary of this FormatTest.


        :param binary: The binary of this FormatTest.
        :type: str
        """
        self._binary = binary

    @property
    def date(self):
        """
        Gets the date of this FormatTest.


        :return: The date of this FormatTest.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this FormatTest.


        :param date: The date of this FormatTest.
        :type: date
        """
        self._date = date

    @property
    def date_time(self):
        """
        Gets the date_time of this FormatTest.


        :return: The date_time of this FormatTest.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """
        Sets the date_time of this FormatTest.


        :param date_time: The date_time of this FormatTest.
        :type: str
        """
        self._date_time = date_time

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

