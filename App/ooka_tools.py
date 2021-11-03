import os


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
