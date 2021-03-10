"""
validation
"""
from re import fullmatch
from base64 import b64decode

def email_validation(mail_id):
    """[This module provides validaions for the mail_id]

    Args:
        mail_id ([String]): [The unvalidated mail id]

    Returns:
        [string]: [Returns validated email in string format]
    """
    if fullmatch("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,3})",mail_id):
        return mail_id
    print('incorrect mail format ')
    return email_validation(input('enter valid mail : ').strip().lower())
#email_validation(input())
def password_validation(password):
    """[This module provides validations for the password]

    Args:
        password (string): [The unvalidated password]

    Returns:
        [string]: [Returns the validated password in string]
    """
    pattern = "(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$!%*#?&])[A-Za-z0-9@$!#%*?&]{8,16}"
    if fullmatch(pattern, password):
        return password
    text = 'password did not match the requirement\
    (should contain atleast one capital letter, small letter, digit ,\
    special character and length should be between 8 and 20 '
    print(text)
    return password_validation(input('enter password : ').strip())

def decode(password):
    """[This module is custom made to decode the password based on base64 and ascii  encodings]

    Args:
        password (binary string): [The encoded binary string]

    Returns:
        [string]: [returns the decoded value of the string]
    """
    return (b64decode(password)).decode('ascii')

def userid(uid):
    """[ This module is custom made to check if the user is from ojas ]

    Args:
        uid ( string ): [ The unvalidated user_id ]

    Returns:
        [ string ]: [ Returns the validated user_id ]
    """
    pattern = '^ojas[0-9]{1,}'
    if fullmatch(pattern,uid):
        return uid
    return userid(input('Should start with ojas followed by numbers \
        \n Re enter Uid : ').strip().lower())

def user_name_validation(user_name):
    """[summary]

    Args:
        user_name (string): [The username of the user]

    Returns:
        [strings]: [returns the validated user_name]
    """
    pattern = '^[a-zA-Z_0-9]{3,}\s?[a-zA-Z_0-9\s]*'
    if fullmatch(pattern,user_name):
        return user_name
    return user_name_validation(input('Should contain minimum 3 Characters \
        \n Re enter User Name : ').strip().lower())
