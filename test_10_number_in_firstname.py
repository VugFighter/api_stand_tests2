from create_user_test import get_user_body
from data import user_body
from test_8_no_firstname import negative_assert_no_first_name

def negative_assert_number_type_first_name(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Nombre de usuario o usuaria incorrecto." \
                                              "El nombre solo puede contener letras latinas" \
                                              "y la longitud debe ser de 2 a 15 caracteres"
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400