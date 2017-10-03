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

import moosend
from moosend.rest import ApiException
from moosend.apis.campaigns_api import CampaignsApi


class TestCampaignsApi(unittest.TestCase):
    """ CampaignsApi unit test stubs """

    def setUp(self):
        self.api = moosend.apis.campaigns_api.CampaignsApi()

    def tearDown(self):
        pass

    def test_a_b_test_campaign_summary(self):
        """
        Test case for a_b_test_campaign_summary

        AB Test Campaign Summary
        """
        pass

    def test_activity_by_location(self):
        """
        Test case for activity_by_location

        Activity By Location
        """
        pass

    def test_campaign_summary(self):
        """
        Test case for campaign_summary

        Campaign Summary
        """
        pass

    def test_cloning_an_existing_campaign(self):
        """
        Test case for cloning_an_existing_campaign

        Cloning An Existing Campaign
        """
        pass

    def test_creating_a_draft_campaign(self):
        """
        Test case for creating_a_draft_campaign

        Creating A Draft Campaign
        """
        pass

    def test_deleting_a_campaign(self):
        """
        Test case for deleting_a_campaign

        Deleting A Campaign
        """
        pass

    def test_get_all_campaigns(self):
        """
        Test case for get_all_campaigns

        Get All Campaigns
        """
        pass

    def test_get_campaign_statistics_with_paging__filtered(self):
        """
        Test case for get_campaign_statistics_with_paging__filtered

        Get Campaign Statistics With Paging & Filtered
        """
        pass

    def test_get_campaigns_by_page(self):
        """
        Test case for get_campaigns_by_page

        Get Campaigns By Page
        """
        pass

    def test_get_campaigns_by_page_and_pagesize(self):
        """
        Test case for get_campaigns_by_page_and_pagesize

        Get Campaigns By Page And Pagesize
        """
        pass

    def test_getting_all_your_senders(self):
        """
        Test case for getting_all_your_senders

        Getting All Your Senders
        """
        pass

    def test_getting_campaign_details(self):
        """
        Test case for getting_campaign_details

        Getting Campaign Details
        """
        pass

    def test_getting_sender_details(self):
        """
        Test case for getting_sender_details

        Getting Sender Details
        """
        pass

    def test_link_activity(self):
        """
        Test case for link_activity

        Link Activity
        """
        pass

    def test_scheduling_a_campaign(self):
        """
        Test case for scheduling_a_campaign

        Scheduling A Campaign
        """
        pass

    def test_sending_a_campaign(self):
        """
        Test case for sending_a_campaign

        Sending a campaign
        """
        pass

    def test_testing_a_campaign(self):
        """
        Test case for testing_a_campaign

        Testing a campaign
        """
        pass

    def test_unscheduling_a_campaign(self):
        """
        Test case for unscheduling_a_campaign

        Unscheduling a campaign
        """
        pass

    def test_updating_a_draft_campaign(self):
        """
        Test case for updating_a_draft_campaign

        Updating A Draft Campaign
        """
        pass


if __name__ == '__main__':
    unittest.main()
