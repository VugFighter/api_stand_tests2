import data
import sender_stand_request
from data import user_body

def negative_assert_no_first_name(user_body):
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"
def test_create_user_empty_firstname_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_first_name(user_body)
