import os


"""
 pour remplacer le os.environement et cree un message d'erreur
"""
def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


