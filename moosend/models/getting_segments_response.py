# coding: utf-8

"""
    Moosend API

    TODO: Add a description

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GettingSegmentsResponse(object):
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
        'code': 'float',
        'context': 'Context140',
        'error': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'context': 'Context',
        'error': 'Error'
    }

    def __init__(self, code=None, context=None, error=None):
        """
        GettingSegmentsResponse - a model defined in Swagger
        """

        self._code = None
        self._context = None
        self._error = None

        if code is not None:
          self.code = code
        if context is not None:
          self.context = context
        if error is not None:
          self.error = error

    @property
    def code(self):
        """
        Gets the code of this GettingSegmentsResponse.
        

        :return: The code of this GettingSegmentsResponse.
        :rtype: float
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this GettingSegmentsResponse.
        

        :param code: The code of this GettingSegmentsResponse.
        :type: float
        """

        self._code = code

    @property
    def context(self):
        """
        Gets the context of this GettingSegmentsResponse.

        :return: The context of this GettingSegmentsResponse.
        :rtype: Context140
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this GettingSegmentsResponse.

        :param context: The context of this GettingSegmentsResponse.
        :type: Context140
        """

        self._context = context

    @property
    def error(self):
        """
        Gets the error of this GettingSegmentsResponse.
        

        :return: The error of this GettingSegmentsResponse.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this GettingSegmentsResponse.
        

        :param error: The error of this GettingSegmentsResponse.
        :type: str
        """

        self._error = error

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
        if not isinstance(other, GettingSegmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
