import configuration
import requests
import data
def post_new_order(body): #post-запрос на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=body,
                        headers=data.headers)
def get_order(track_number): #get-запрос на получение информации о заказе
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER + "?t=" + str(track_number),
                        headers=data.headers)