import requests
import os

from settings import TOKEN    #В файлике settings содержиться токен )



class YaUploader:

    host = "https://cloud-api.yandex.net/"

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "applicac:\tion/json",
            "Authorization": f"OAuth {self.token}",
        }

    
    #  Получение ссылки для загрузки
    def get_upload_link(self, file_name):
        uri = "v1/disk/resources/upload/"
        url = self.host + uri
        params = {"path": f"/{file_name}"}
        response = requests.get(url, headers=self.get_headers(), params=params)
        print(response.json())
        return response.json()["href"]


    # Метод загрузки файла
    def upload(self, user_path):
        upload_link = self.get_upload_link(file_name)
        response = requests.put(
            upload_link, headers=self.get_headers(), data=open(user_path, "rb")
        )
        print(response.status_code)
        if response.status_code == 201:
            print("Загрузка прошла успешно")





if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    
    user_path = input("Введите путь до файла ")
    file_name = os.path.basename(user_path)
    uploader = YaUploader(TOKEN)
    result = uploader.upload(user_path)