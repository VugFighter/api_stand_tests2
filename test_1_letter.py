import sender_stand_request
import data
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Nombre de usuario o usuaria incorrecto." \
                                              "El nombre solo puede contener letras latinas" \
                                              "y la longitud debe ser de 2 a 15 caracteres"

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

def test_create_user_1_letter_in_first_name_get_success_response():
    negative_assert_symbol("A")