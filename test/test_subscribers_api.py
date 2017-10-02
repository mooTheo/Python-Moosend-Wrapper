# coding: utf-8

"""
    Moosend API

    TODO: Add a description

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import Moosend.Wrappers.PythonWrapper
from Moosend.Wrappers.PythonWrapper.rest import ApiException
from Moosend.Wrappers.PythonWrapper.apis.subscribers_api import SubscribersApi


class TestSubscribersApi(unittest.TestCase):
    """ SubscribersApi unit test stubs """

    def setUp(self):
        self.api = Moosend.Wrappers.PythonWrapper.apis.subscribers_api.SubscribersApi()

    def tearDown(self):
        pass

    def test_adding_multiple_subscribers(self):
        """
        Test case for adding_multiple_subscribers

        Adding multiple subscribers
        """
        pass

    def test_adding_subscribers(self):
        """
        Test case for adding_subscribers

        Adding subscribers
        """
        pass

    def test_get_subscriber_by_email_address(self):
        """
        Test case for get_subscriber_by_email_address

        Get subscriber by email address
        """
        pass

    def test_get_subscriber_by_id(self):
        """
        Test case for get_subscriber_by_id

        Get subscriber by id
        """
        pass

    def test_getting_subscribers(self):
        """
        Test case for getting_subscribers

        Getting subscribers
        """
        pass

    def test_removing_a_subscriber(self):
        """
        Test case for removing_a_subscriber

        Removing a subscriber
        """
        pass

    def test_removing_multiple_subscribers(self):
        """
        Test case for removing_multiple_subscribers

        Removing multiple subscribers
        """
        pass

    def test_unsubscribing_subscribers_from_account(self):
        """
        Test case for unsubscribing_subscribers_from_account

        Unsubscribing subscribers from account
        """
        pass

    def test_unsubscribing_subscribers_from_mailing_list(self):
        """
        Test case for unsubscribing_subscribers_from_mailing_list

        Unsubscribing subscribers from mailing list
        """
        pass

    def test_unsubscribing_subscribers_from_mailing_list_and_a_specified_campaign(self):
        """
        Test case for unsubscribing_subscribers_from_mailing_list_and_a_specified_campaign

        Unsubscribing subscribers from mailing list and a specified campaign
        """
        pass

    def test_updating_a_subscriber(self):
        """
        Test case for updating_a_subscriber

        Updating a subscriber
        """
        pass


if __name__ == '__main__':
    unittest.main()