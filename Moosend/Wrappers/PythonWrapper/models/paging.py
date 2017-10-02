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


class Paging(object):
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
        'current_page': 'float',
        'page_size': 'float',
        'sort_expression': 'str',
        'sort_is_ascending': 'bool',
        'total_page_count': 'float',
        'total_results': 'float'
    }

    attribute_map = {
        'current_page': 'CurrentPage',
        'page_size': 'PageSize',
        'sort_expression': 'SortExpression',
        'sort_is_ascending': 'SortIsAscending',
        'total_page_count': 'TotalPageCount',
        'total_results': 'TotalResults'
    }

    def __init__(self, current_page=None, page_size=None, sort_expression=None, sort_is_ascending=None, total_page_count=None, total_results=None):
        """
        Paging - a model defined in Swagger
        """

        self._current_page = None
        self._page_size = None
        self._sort_expression = None
        self._sort_is_ascending = None
        self._total_page_count = None
        self._total_results = None

        if current_page is not None:
          self.current_page = current_page
        if page_size is not None:
          self.page_size = page_size
        if sort_expression is not None:
          self.sort_expression = sort_expression
        if sort_is_ascending is not None:
          self.sort_is_ascending = sort_is_ascending
        if total_page_count is not None:
          self.total_page_count = total_page_count
        if total_results is not None:
          self.total_results = total_results

    @property
    def current_page(self):
        """
        Gets the current_page of this Paging.
        

        :return: The current_page of this Paging.
        :rtype: float
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """
        Sets the current_page of this Paging.
        

        :param current_page: The current_page of this Paging.
        :type: float
        """

        self._current_page = current_page

    @property
    def page_size(self):
        """
        Gets the page_size of this Paging.
        

        :return: The page_size of this Paging.
        :rtype: float
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """
        Sets the page_size of this Paging.
        

        :param page_size: The page_size of this Paging.
        :type: float
        """

        self._page_size = page_size

    @property
    def sort_expression(self):
        """
        Gets the sort_expression of this Paging.
        

        :return: The sort_expression of this Paging.
        :rtype: str
        """
        return self._sort_expression

    @sort_expression.setter
    def sort_expression(self, sort_expression):
        """
        Sets the sort_expression of this Paging.
        

        :param sort_expression: The sort_expression of this Paging.
        :type: str
        """

        self._sort_expression = sort_expression

    @property
    def sort_is_ascending(self):
        """
        Gets the sort_is_ascending of this Paging.
        

        :return: The sort_is_ascending of this Paging.
        :rtype: bool
        """
        return self._sort_is_ascending

    @sort_is_ascending.setter
    def sort_is_ascending(self, sort_is_ascending):
        """
        Sets the sort_is_ascending of this Paging.
        

        :param sort_is_ascending: The sort_is_ascending of this Paging.
        :type: bool
        """

        self._sort_is_ascending = sort_is_ascending

    @property
    def total_page_count(self):
        """
        Gets the total_page_count of this Paging.
        

        :return: The total_page_count of this Paging.
        :rtype: float
        """
        return self._total_page_count

    @total_page_count.setter
    def total_page_count(self, total_page_count):
        """
        Sets the total_page_count of this Paging.
        

        :param total_page_count: The total_page_count of this Paging.
        :type: float
        """

        self._total_page_count = total_page_count

    @property
    def total_results(self):
        """
        Gets the total_results of this Paging.
        

        :return: The total_results of this Paging.
        :rtype: float
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """
        Sets the total_results of this Paging.
        

        :param total_results: The total_results of this Paging.
        :type: float
        """

        self._total_results = total_results

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
        if not isinstance(other, Paging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
