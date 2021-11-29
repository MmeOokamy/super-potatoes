import os
import jinja2
from datetime import datetime as dt


def get_env_variable(name):
   """[summary]

   Args:
       name ([type]): [description]

   Raises:
       Exception: [description]

   Returns:
       [type]: [description]
   """
   try:
      return os.environ[name]
   except KeyError:
      message = "Expected environment variable '{}' not set.".format(name)
      raise Exception(message)

def get_year():
   # pour le copyright
    currentDateTime = dt.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    return year

