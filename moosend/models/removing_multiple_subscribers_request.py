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


class RemovingMultipleSubscribersRequest(object):
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
        'emails': 'str'
    }

    attribute_map = {
        'emails': 'Emails'
    }

    def __init__(self, emails=None):
        """
        RemovingMultipleSubscribersRequest - a model defined in Swagger
        """

        self._emails = None

        self.emails = emails

    @property
    def emails(self):
        """
        Gets the emails of this RemovingMultipleSubscribersRequest.
        A list of email addresses to be removed, separated with a comma (,).

        :return: The emails of this RemovingMultipleSubscribersRequest.
        :rtype: str
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this RemovingMultipleSubscribersRequest.
        A list of email addresses to be removed, separated with a comma (,).

        :param emails: The emails of this RemovingMultipleSubscribersRequest.
        :type: str
        """
        if emails is None:
            raise ValueError("Invalid value for `emails`, must not be `None`")

        self._emails = emails

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
        if not isinstance(other, RemovingMultipleSubscribersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
