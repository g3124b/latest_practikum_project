import requests
import configuration
import data
import scooter_get_order_test

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_AN_ORDER,
                         json=order_body,
                         headers=data.headers)

def get_order():
    return requests.get(configuration.URL_SERVICE \
                        + configuration.GET_ORDER \
                        + str(scooter_get_order_test.post_order_response.json()["track"]))