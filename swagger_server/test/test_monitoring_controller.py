# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.video import Video  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMonitoringController(BaseTestCase):
    """MonitoringController integration test stubs"""

    def test_add_video_to_playlist(self):
        """Test case for add_video_to_playlist

        Add a video to the playlist
        """
        query_string = [('video_name', 'video_name_example')]
        response = self.client.open(
            '/api/add_video_to_playlist',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_playlist(self):
        """Test case for delete_playlist

        Delete the playlist
        """
        query_string = [('video_name', 'video_name_example')]
        response = self.client.open(
            '/api/delete-playlist',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_playlist(self):
        """Test case for get_playlist

        Finds playlist
        """
        response = self.client.open(
            '/api/get_playlist',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
