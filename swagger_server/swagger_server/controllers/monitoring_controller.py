import subprocess

import connexion
import six

from swagger_server.models.video import Video  # noqa: E501
from swagger_server import util


def add_video_to_playlist(video_name):  # noqa: E501
    """Add a video to the playlist

     # noqa: E501

    :param video_name: Name of the video to be added to the playlist
    :type video_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_playlist(video_name):  # noqa: E501
    """Delete the playlist

     # noqa: E501

    :param video_name: Video name to remove from playlist
    :type video_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_playlist():  # noqa: E501
    """Finds playlist

     # noqa: E501


    :rtype: List[Video]
    """
    return 'do some magic!'
