import sender_stand_request
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Nombre de usuario o usuaria incorrecto." \
                                              "El nombre solo puede contener letras latinas" \
                                              "y la longitud debe ser de 2 a 15 caracteres"



def test_create_user_16_letter_in_first_name_get_success_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")