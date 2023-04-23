import json
import os
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build
import isodate

api_key: str = os.getenv('YT_API_KEY')

class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        for i in channel['items']:
            self.title = i['snippet']['title']
        for i in channel['items']:
            self.video_count = i['statistics']['videoCount']
        for i in channel['items']:
            self.description = i['snippet']['description']
        for i in channel['items']:
            self.view_count = i['statistics']['viewCount']
        for i in channel['items']:
            self.subscriber_count = int(i['statistics']['subscriberCount'])

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, name_json):
        """Метод, сохраняющий в файл значения атрибутов экземпляра `Channel`"""
        self.name_json = name_json
        self.channel_dict = {'id': self.__channel_id, "ссылка на канал": self.url, 'название канала': self.title,
                             'количество видео': self.video_count, 'описание канала': self.description,
                             'количество просмотров': self.view_count, 'количество подписчиков': self.subscriber_count}
        json_dict = json.dumps(self.channel_dict, indent=4, ensure_ascii=False)
        with open(self.name_json, 'w', encoding="utf-8") as file:
            print(json_dict, file=file)

    def __str__(self):
        """Метод, который выводит пользовательскую информацию в формате: название канала (ссылка на канал)"""
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        """Складывает количество подписчиков двух каналов"""
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        """Вычитает количество подписчиков двух каналов"""
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        """Сравнивает количество подписчиков. Возвращает True, если в первом их больше"""
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        """Сравнивает количество подписчиков. Возвращает True, если в первом их больше или равно количеству во втором"""
        return self.subscriber_count >= other.subscriber_count

