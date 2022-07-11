import os
import jinja2
from datetime import datetime as dt, timedelta
import time


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


def get_jeun(date_block="", heur_block='', heure_conf_jeun='', heure_conf_jeune_boisson=''):
    print()
    block = ('{} {}').format(date_block, heur_block)
    dt_block = dt.strptime(block, "%Y-%m-%d %H:%M")

    dt_jeun = dt.strptime(heure_conf_jeun, "%H:%M")
    dt_boisson = dt.strptime(heure_conf_jeune_boisson, "%H:%M")

    td_jeun = timedelta(hours=dt_jeun.hour, minutes=dt_jeun.minute)
    td_boisson = timedelta(hours=dt_boisson.hour, minutes=dt_boisson.minute)

    x = dt_block - td_jeun
    y = dt_block - td_boisson

    print(('Il faudra etre a jeun a partir de {} le {} pour la nourriture et de {} le {} pour les boissons').format(
        x.time(), x.date(), y.time(), y.date()))
    print('-------')
    test = condition_jeun('00:00', '06:00', 'Minuit', '6h', x, y)
    print(test[0])
    print(test[1])


def condition_jeun(param_ecart_debut, param_ecart_fin, valeur_jeun_si_vrai, valeur_boisson_si_vrai, h_jeun, h_boisson):
    ret_tuple = ()
    # Placer dans une fonction
    ped = dt.strptime(param_ecart_debut, "%H:%M").time()
    pef = dt.strptime(param_ecart_fin, "%H:%M").time()

    h_jeun_a_verifier = h_jeun.time()
    h_boisson_a_verifier = h_boisson.time()

    # retour minuit si entre 0 et 6 sinon x 
    h_jeun_verifier = valeur_jeun_si_vrai if ped <= h_jeun_a_verifier <= pef else h_jeun.time()
    h_boisson_verifier = valeur_boisson_si_vrai if ped <= h_boisson_a_verifier <= pef else h_boisson.time()

    ret_tuple = (h_jeun_verifier, h_boisson_verifier)
    return ret_tuple


if __name__ == "__main__":
    get_jeun('2022-07-11', '09:30', '08:00', '01:45')
