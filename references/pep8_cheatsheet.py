"""Ceci est la ligne de résumé du module.

Ceci est une docstring à lignes multiples. Les paragraphes sont séparés
par des lignes vides. Les lignes se limitent à 79 caractères.

Le nom du module et des packages doivent être courts, en minuscules_soulignees.

Utiliser un linter comme flake8. Ceci devrait être mis en place dans Jupyter.

Se reporter à http://www.python.org/dev/peps/pep-0008/ pour d'autres détails.

Remarque : lire le nom des identifiants pour comprendre certains remarques.
"""


import os  # les imports de la lib standard d'abord
import sys  # en ordre alphabétique

import some_third_party_lib  # les modules tiers ensuite (pandas, pyspark, ...)
import some_third_party_other_lib  # en ordre alphabétique

import local_stuff  # les modules "locaux" en dernier
import more_local_stuff
import dont_import_two, modules_in_one_line  # IMPORTANT!
from pyflakes_cannot_handle import *  # ceci devrait aussi être évité # noqa
# Utiliser # noqa dans la ligne ci-dessous pour éviter les alertes du linter !


_a_global_var = 2  # _ avant pour éviter l'import par 'from foo import *'
_b_global_var = 3

A_CONSTANT = 'ugh.'


# 2 lignes vides entre les imports et fonctions principales puis les classes
def naming_convention():
    """Ajouter des docstrings à TOUTE fonction, classe et méthode publique.

    Les fonctions utilisent la convention snake_case pour leur nom.
    """
    if x == 4:  # x est blue <= commentaire 1 ligne UTILE (2 espaces avant #)
        x, y = y, x  # inverse x et y <= commentaire inutile (1 espace après #)
    c = (a + b) * (a - b)  # espace entre opérations pour la lisibilité.
    dict['key'] = dict[0] = {'x': 2, 'cat': 'not a dog'}

class NamingConvention(object):
    """La première ligne d'une docstring est courte, à la suite des quotes.

    Les noms de Class et d'Exception sont en CapWords.

    Les quotes fermantes de la docstring sont sur une ligne à part :
    """

    a = 2
    b = 4
    _internal_variable = 3
    class_ = 'foo'  # _ en suffixe pour éviter les conflits avec les builtin

    # Les _ découragent aussi l'utilisation hors de la classe de la variable
    # C'est aussi très utile si la classe doit être sous-classée, et
    # si les descendants utilisent le même nom pour quelque chose d'autre, ex.:
    # pour des variables comme 'a' ci-dessus. Ce "name mangling" assure que
    # *votre* a et un a dans la classe fille ne seront pas en conflit.
    # Utiliser donc les soulignés pour ces cas.
    __internal_var = 4

    # ne JAMAIS utiliser le _ double avant ou après pour vos identifiants
    __nooooooodontdoit__ = 0

    # ne pas utiliser l O I comme identifiants car difficiles à distinguer :
    l = 1
    O = 2
    I = 3

    # quelques exemples pour aller à la ligne pour respecter la limite de 79
    # nous préférons le "truc de la parenthèse" au caractère de continuation \
    def __init__(self, width, height,
                 color='black', emphasis=None, highlight=0):
        if width == 0 and height == 0 and \
           color == 'red' and emphasis == 'strong' or \
           highlight > 100:
            raise ValueError('sorry, you lose')
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" %
                             (width, height))
        Blob.__init__(self, width, height,
                      color, emphasis, highlight)

    # mettre des lignes vides pour améliorer la lisibilité dans le code
    short_foo_dict = {'loooooooooooooooooooong_element_name': 'cat',
                      'other_element': 'dog'}

    long_foo_dict_with_many_elements = {
        'foo': 'cat',
        'bar': 'dog'
    }

    # 1 ligne vide entre les def au sein d'une classe
    def foo_method(self, x, y=None):
        """Noms de méthodes & fonctions en minuscules_avec_soulignement.

        Toujours mettre self en premier argument d'une méthode.
        """
        pass

    @classmethod
    def bar(cls):
        """Utiliser cls ! plutôt que klass, et surtout pas class..."""
        pass

# une règle de 79 caractères pour se caler si pas d'outils dans l'éditeur :
# 34567891123456789212345678931234567894123456789512345678961234567897123456789

"""
Nom des conventions de nommage :
snake_case
MACRO_CASE
camelCase
CapWords
"""

# Ligne vide à la fin du fichier
