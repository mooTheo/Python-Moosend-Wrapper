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


class Context64(object):
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
        'emails_ignored': 'float',
        'emails_processed': 'float'
    }

    attribute_map = {
        'emails_ignored': 'EmailsIgnored',
        'emails_processed': 'EmailsProcessed'
    }

    def __init__(self, emails_ignored=None, emails_processed=None):
        """
        Context64 - a model defined in Swagger
        """

        self._emails_ignored = None
        self._emails_processed = None

        if emails_ignored is not None:
          self.emails_ignored = emails_ignored
        if emails_processed is not None:
          self.emails_processed = emails_processed

    @property
    def emails_ignored(self):
        """
        Gets the emails_ignored of this Context64.
        

        :return: The emails_ignored of this Context64.
        :rtype: float
        """
        return self._emails_ignored

    @emails_ignored.setter
    def emails_ignored(self, emails_ignored):
        """
        Sets the emails_ignored of this Context64.
        

        :param emails_ignored: The emails_ignored of this Context64.
        :type: float
        """

        self._emails_ignored = emails_ignored

    @property
    def emails_processed(self):
        """
        Gets the emails_processed of this Context64.
        

        :return: The emails_processed of this Context64.
        :rtype: float
        """
        return self._emails_processed

    @emails_processed.setter
    def emails_processed(self, emails_processed):
        """
        Sets the emails_processed of this Context64.
        

        :param emails_processed: The emails_processed of this Context64.
        :type: float
        """

        self._emails_processed = emails_processed

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
        if not isinstance(other, Context64):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
