import connexion
import six

from swagger_server.models.video import Video  # noqa: E501
from swagger_server import util


def add_video(url):  # noqa: E501
    """Add a new video to the store

     # noqa: E501

    :param url: Youtube url of a video to be added to the database
    :type url: str

    :rtype: None
    """
    return 'do some magic!'


def find_videos_by_age(age):  # noqa: E501
    """Finds Videos by age

    Multiple age values can be provided with comma separated strings # noqa: E501

    :param age: Age values that need to be considered for filter
    :type age: 

    :rtype: List[Video]
    """
    return 'do some magic!'


def get_all_videos():  # noqa: E501
    """Finds all Videos

     # noqa: E501


    :rtype: List[Video]
    """
    return 'do some magic!'


def update_video_watched():  # noqa: E501
    """Mark an existing video as watched

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
