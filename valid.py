"""
validation
"""
from re import fullmatch
import base64
def email_validation(mail_id):
    """[This module provides validaions for the mail_id]

    Args:
        mail_id ([String]): [The unvalidated mail id]

    Returns:
        [string]: [Returns validated email in string format]
    """
    if fullmatch(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,3})",mail_id):
        return mail_id
    print('incorrect mail format ')
    return email_validation(input('enter mail '))

def password_validation(password):
    """[This module provides validations for the password]

    Args:
        password (string): [The unvalidated password]

    Returns:
        [string]: [Returns the validated password in string]
    """
    pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}"
    if fullmatch(pattern, password):
        return password
    text = 'password did not match the requirement (should contain atleast one capital letter, small letter, digit ,special character and length should be between 8 and 20 '
    print(text)
    return password_validation(input('enter password "'))

def decode(password):
    """[This module is custom made to decode the password based on base64 and ascii  encodings]

    Args:
        password (binary string): [The encoded binary string]

    Returns:
        [string]: [returns the decoded value of the string]
    """
    return (base64.b64decode(password)).decode('ascii')

def userid(uid):
    """[ This module is custom made to check if the user is from ojas ]

    Args:
        uid ( string ): [ The unvalidated user_id ]

    Returns:
        [ string ]: [ Returns the validated user_id ]
    """
    pattern = '^ojas\d{1,}'
    if fullmatch(pattern,uid):
        return uid
    return userid(input('Should start with ojas followed by numbers \n Re enter Uid'))
userid(input())