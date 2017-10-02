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


class Subscribers(object):
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
        'email': 'str',
        'name': 'str',
        'custom_fields': 'object'
    }

    attribute_map = {
        'email': 'Email',
        'name': 'Name',
        'custom_fields': 'CustomFields'
    }

    def __init__(self, email=None, name=None, custom_fields=None):
        """
        Subscribers - a model defined in Swagger
        """

        self._email = None
        self._name = None
        self._custom_fields = None

        self.email = email
        if name is not None:
          self.name = name
        if custom_fields is not None:
          self.custom_fields = custom_fields

    @property
    def email(self):
        """
        Gets the email of this Subscribers.
        

        :return: The email of this Subscribers.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Subscribers.
        

        :param email: The email of this Subscribers.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def name(self):
        """
        Gets the name of this Subscribers.
        

        :return: The name of this Subscribers.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Subscribers.
        

        :param name: The name of this Subscribers.
        :type: str
        """

        self._name = name

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this Subscribers.
        A list of name-value pairs that match the member's custom fields defined in the mailing list.  For example, if you have two custom fields named Age and Country, you should specify values for them as following example.

        :return: The custom_fields of this Subscribers.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this Subscribers.
        A list of name-value pairs that match the member's custom fields defined in the mailing list.  For example, if you have two custom fields named Age and Country, you should specify values for them as following example.

        :param custom_fields: The custom_fields of this Subscribers.
        :type: object
        """

        self._custom_fields = custom_fields

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
        if not isinstance(other, Subscribers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
