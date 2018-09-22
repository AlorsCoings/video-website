# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.video import Video  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVideoController(BaseTestCase):
    """VideoController integration test stubs"""

    def test_add_video(self):
        """Test case for add_video

        Add a new video to the store
        """
        query_string = [('url', 'url_example')]
        response = self.client.open(
            '/api/video',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_videos_by_age(self):
        """Test case for find_videos_by_age

        Finds Videos by age
        """
        query_string = [('age', 8.14)]
        response = self.client.open(
            '/api/video/findByAge',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_videos(self):
        """Test case for get_all_videos

        Finds all Videos
        """
        response = self.client.open(
            '/api/video',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_video_watched(self):
        """Test case for update_video_watched

        Mark an existing video as watched
        """
        response = self.client.open(
            '/api/video',
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
