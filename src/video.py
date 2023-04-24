import os

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:
    def __init__(self, video_id: str) -> None:
        """
        Инициализация реальными данными следующих атрибутов экземпляра класса `Video`:
            - id видео
            - название видео
            - ссылка на видео
            - количество просмотров
            - количество лайков
        """
        self.__video_id = video_id
        self.url = f'https://www.youtube.com/channel/{self.__video_id}'
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title = video_response['items'][0]['snippet']['title']
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """Выводит данные в формате: <название_видео>"""
        return self.video_title


class PLVideo:
    """
    Класс для видео `PLVideo`, который инициализируется 'id видео' и 'id плейлиста',
    Инициализация реальными данными следующих атрибутов экземпляра класса `PLVideo`:
        - id видео
        - название видео
        - ссылка на видео
        - количество просмотров
        - количество лайков
        - id плейлиста
    """

    def __init__(self, video_id, playlist_id):
        self.playlist_id = playlist_id
        self.video_id = video_id
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title = video_response['items'][0]['snippet']['title']
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """Выводит данные в формате: <название_видео>"""
        return self.video_title
