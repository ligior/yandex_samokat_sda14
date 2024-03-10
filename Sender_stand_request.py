import Configuration
import Data
import requests


def post_create_order(body):
    return requests.post(Configuration.SERVER_URL+Configuration.CREATE_ORDER_URL,json=body,headers=Data.headers)


def get_order_by_track(trackid):
    return requests.get(Configuration.SERVER_URL+Configuration.GET_ORDER_BY_TRACK_URL+trackid)




