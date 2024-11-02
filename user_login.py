from populate_edi855_data import get_database
import string

edi855_json_db = get_database("edi855_edi_json_data")

def create_or_login_user(username, password, action):
    if action == 'CREATE':
        return create_user(username, password)
    else:
        return login_user(username, password)

def create_user(username, password):
    model_collection = edi855_json_db["user_details"]
    user_count = model_collection.count_documents({ "username": username })
    if user_count > 0:
        message = "User already exists with username : "+username
        output = '{"status":"FAILURE","message":\"' + message + '\"}'
        return output
    else:
        user_details = {
            "_id" : username,
            "username" : username,
            "password" : password
        }
        model_collection.insert_one(user_details)
        message = "User successfully with username : " + username
        output = '{"status":"SUCCESS","message":\"' + message + '\"}'
        return output

def login_user(username, password):
    model_collection = edi855_json_db["user_details"]
    user_count = model_collection.count_documents({ "username": username })

    if user_count > 0:
        user_rows = model_collection.find({ "username": username })
        for row in user_rows:
            if row.get("password") == password:
                user_exists_message = "Login successful with username : "+username
                user_exists_output = '{"status":"SUCCESS","message":\"' + user_exists_message + '\"}'
                return user_exists_output

        invalid_password_message = "Invalid Password for username :"+username
        invalid_password_output = '{"status":"FAILURE","message":\"' + invalid_password_message + '\"}'
        return invalid_password_output

    else:
        message = "Username doesn't exists : " + username
        output = '{"status":"FAILURE","message":\"' + message + '\"}'
        return output
