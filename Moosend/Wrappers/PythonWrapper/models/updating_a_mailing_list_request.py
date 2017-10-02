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


class UpdatingAMailingListRequest(object):
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
        'name': 'str',
        'confirmation_page': 'str',
        'redirect_after_unsubscribe_page': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'confirmation_page': 'ConfirmationPage',
        'redirect_after_unsubscribe_page': 'RedirectAfterUnsubscribePage'
    }

    def __init__(self, name=None, confirmation_page=None, redirect_after_unsubscribe_page=None):
        """
        UpdatingAMailingListRequest - a model defined in Swagger
        """

        self._name = None
        self._confirmation_page = None
        self._redirect_after_unsubscribe_page = None

        self.name = name
        if confirmation_page is not None:
          self.confirmation_page = confirmation_page
        if redirect_after_unsubscribe_page is not None:
          self.redirect_after_unsubscribe_page = redirect_after_unsubscribe_page

    @property
    def name(self):
        """
        Gets the name of this UpdatingAMailingListRequest.
        The name of the new mailing list.

        :return: The name of this UpdatingAMailingListRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdatingAMailingListRequest.
        The name of the new mailing list.

        :param name: The name of this UpdatingAMailingListRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def confirmation_page(self):
        """
        Gets the confirmation_page of this UpdatingAMailingListRequest.
        The URL of the page that will be displayed at the end of the subscription process.

        :return: The confirmation_page of this UpdatingAMailingListRequest.
        :rtype: str
        """
        return self._confirmation_page

    @confirmation_page.setter
    def confirmation_page(self, confirmation_page):
        """
        Sets the confirmation_page of this UpdatingAMailingListRequest.
        The URL of the page that will be displayed at the end of the subscription process.

        :param confirmation_page: The confirmation_page of this UpdatingAMailingListRequest.
        :type: str
        """

        self._confirmation_page = confirmation_page

    @property
    def redirect_after_unsubscribe_page(self):
        """
        Gets the redirect_after_unsubscribe_page of this UpdatingAMailingListRequest.
        The URL of the page that users will be redirected after unsubscribing from your mailing list.

        :return: The redirect_after_unsubscribe_page of this UpdatingAMailingListRequest.
        :rtype: str
        """
        return self._redirect_after_unsubscribe_page

    @redirect_after_unsubscribe_page.setter
    def redirect_after_unsubscribe_page(self, redirect_after_unsubscribe_page):
        """
        Sets the redirect_after_unsubscribe_page of this UpdatingAMailingListRequest.
        The URL of the page that users will be redirected after unsubscribing from your mailing list.

        :param redirect_after_unsubscribe_page: The redirect_after_unsubscribe_page of this UpdatingAMailingListRequest.
        :type: str
        """

        self._redirect_after_unsubscribe_page = redirect_after_unsubscribe_page

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
        if not isinstance(other, UpdatingAMailingListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
