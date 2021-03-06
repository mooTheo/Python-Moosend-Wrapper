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


class SchedulingACampaignRequest(object):
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
        'date_time': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'date_time': 'DateTime',
        'timezone': 'Timezone'
    }

    def __init__(self, date_time=None, timezone=None):
        """
        SchedulingACampaignRequest - a model defined in Swagger
        """

        self._date_time = None
        self._timezone = None

        self.date_time = date_time
        if timezone is not None:
          self.timezone = timezone

    @property
    def date_time(self):
        """
        Gets the date_time of this SchedulingACampaignRequest.
        The date and time at which the campaign will be delivered.

        :return: The date_time of this SchedulingACampaignRequest.
        :rtype: str
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """
        Sets the date_time of this SchedulingACampaignRequest.
        The date and time at which the campaign will be delivered.

        :param date_time: The date_time of this SchedulingACampaignRequest.
        :type: str
        """
        if date_time is None:
            raise ValueError("Invalid value for `date_time`, must not be `None`")

        self._date_time = date_time

    @property
    def timezone(self):
        """
        Gets the timezone of this SchedulingACampaignRequest.
        The timezone the specified date and time refers to. By default the timezone in your settings panel will be used. If specified, one of the following values must be used. * Dateline Standard Time * Samoa Standard Time * Hawaiian Standard Time * Alaskan Standard Time * Pacific Standard Time * Pacific Standard Time (Mexico) * US Mountain Standard Time * Mountain Standard Time (Mexico) * Mountain Standard Time * Central Standard Time * Central Standard Time (Mexico) * Canada Central Standard Time * SA Pacific Standard Time * US Eastern Standard Time * Eastern Standard Time * Venezuela Standard Time * Atlantic Standard Time * SA Western Standard Time * Central Brazilian Standard Time * Pacific SA Standard Time * Newfoundland Standard Time * E. South America Standard Time * Argentina Standard Time * SA Eastern Standard Time * Greenland Standard Time * Montevideo Standard Time * Mid-Atlantic Standard Time * Azores Standard Time * Cape Verde Standard Time * Greenwich Standard Time * GMT Standard Time * Morocco Standard Time * W. Central Africa Standard Time * Central European Standard Time * Romance Standard Time * W. Europe Standard Time * Namibia Standard Time * E. Europe Standard Time * Israel Standard Time * FLE Standard Time * South Africa Standard Time * Egypt Standard Time * Middle East Standard Time * GTB Standard Time * Jordan Standard Time * Iran Standard Time * Georgian Standard Time * E. Africa Standard Time * Russian Standard Time * Arab Standard Time * Arabic Standard Time * Caucasus Standard Time * Mauritius Standard Time * Azerbaijan Standard Time * Arabian Standard Time * Afghanistan Standard Time * West Asia Standard Time * Pakistan Standard Time * Ekaterinburg Standard Time * Sri Lanka Standard Time * India Standard Time * Nepal Standard Time * N. Central Asia Standard Time * Central Asia Standard Time * Myanmar Standard Time * North Asia Standard Time * SE Asia Standard Time * Taipei Standard Time * W. Australia Standard Time * Singapore Standard Time * North Asia East Standard Time * China Standard Time * Yakutsk Standard Time * Korea Standard Time * Tokyo Standard Time * AUS Central Standard Time * Cen. Australia Standard Time * AUS Eastern Standard Time * West Pacific Standard Time * Tasmania Standard Time * Vladivostok Standard Time * Central Pacific Standard Time * New Zealand Standard Time * Tonga Standard Time

        :return: The timezone of this SchedulingACampaignRequest.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this SchedulingACampaignRequest.
        The timezone the specified date and time refers to. By default the timezone in your settings panel will be used. If specified, one of the following values must be used. * Dateline Standard Time * Samoa Standard Time * Hawaiian Standard Time * Alaskan Standard Time * Pacific Standard Time * Pacific Standard Time (Mexico) * US Mountain Standard Time * Mountain Standard Time (Mexico) * Mountain Standard Time * Central Standard Time * Central Standard Time (Mexico) * Canada Central Standard Time * SA Pacific Standard Time * US Eastern Standard Time * Eastern Standard Time * Venezuela Standard Time * Atlantic Standard Time * SA Western Standard Time * Central Brazilian Standard Time * Pacific SA Standard Time * Newfoundland Standard Time * E. South America Standard Time * Argentina Standard Time * SA Eastern Standard Time * Greenland Standard Time * Montevideo Standard Time * Mid-Atlantic Standard Time * Azores Standard Time * Cape Verde Standard Time * Greenwich Standard Time * GMT Standard Time * Morocco Standard Time * W. Central Africa Standard Time * Central European Standard Time * Romance Standard Time * W. Europe Standard Time * Namibia Standard Time * E. Europe Standard Time * Israel Standard Time * FLE Standard Time * South Africa Standard Time * Egypt Standard Time * Middle East Standard Time * GTB Standard Time * Jordan Standard Time * Iran Standard Time * Georgian Standard Time * E. Africa Standard Time * Russian Standard Time * Arab Standard Time * Arabic Standard Time * Caucasus Standard Time * Mauritius Standard Time * Azerbaijan Standard Time * Arabian Standard Time * Afghanistan Standard Time * West Asia Standard Time * Pakistan Standard Time * Ekaterinburg Standard Time * Sri Lanka Standard Time * India Standard Time * Nepal Standard Time * N. Central Asia Standard Time * Central Asia Standard Time * Myanmar Standard Time * North Asia Standard Time * SE Asia Standard Time * Taipei Standard Time * W. Australia Standard Time * Singapore Standard Time * North Asia East Standard Time * China Standard Time * Yakutsk Standard Time * Korea Standard Time * Tokyo Standard Time * AUS Central Standard Time * Cen. Australia Standard Time * AUS Eastern Standard Time * West Pacific Standard Time * Tasmania Standard Time * Vladivostok Standard Time * Central Pacific Standard Time * New Zealand Standard Time * Tonga Standard Time

        :param timezone: The timezone of this SchedulingACampaignRequest.
        :type: str
        """

        self._timezone = timezone

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
        if not isinstance(other, SchedulingACampaignRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
