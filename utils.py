from constants import SUPERVISOR_CREDENTIALS


def check_credentials(user_credentials):
    if len(user_credentials):
        username_check = bool(
            SUPERVISOR_CREDENTIALS[0]['username'] == user_credentials[1]
        )
        password_check = bool(
            SUPERVISOR_CREDENTIALS[0]['password'] == user_credentials[2]
        )
        return username_check and password_check
    return False
