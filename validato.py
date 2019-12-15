import logging
import time


def validator(password):
    length_ok = len(password) in range (8,21)
    lower_ok = bool(set (password) & set(password.lower()))
    number_ok = any(c.isdigit() for c in password)
    upper_ok = bool(set(password) & set(password.upper()))
    special_ok= bool(set(password) & set('!" $%^&*@(?)'))
    return length_ok and lower_ok and number_ok and upper_ok & special_ok
logging.basicConfig(level = logging.INFO, filename = time.strftime("my-%Y-%m-%d.log"))

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
