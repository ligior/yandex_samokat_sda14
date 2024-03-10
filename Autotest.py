import Sender_stand_request as Sender
import Data
import pytest

def test_get_order_by_track():
    created_order = Sender.post_create_order(Data.create_order_body)
    order_track = str(created_order.json()["track"])
    order_request = Sender.get_order_by_track(order_track)
    assert order_request.status_code == 200

    # Стручинский Дмитрий, 14-я когорта — Финальный проект. Инженер по тестированию плюс