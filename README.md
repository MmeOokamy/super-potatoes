*Mes projets ne sont pas souvent détaillés dans la partie readme. Je suis une adepte du cahier ! J'ai toujours un cahier pour noter mes idées et ma conception. Que cela soit professionnel ou personnel. C'est un peu ma méthode de suivi.*


# Super-Potatoes

C'est avant tout une envie de travailler avec Flask et React mais aussi de réaliser un projet qui pourra être utile.
Un Kanban, un **tableau de bord** qui me permettra de suivre mes futurs projets et de pouvoir y accéder partout.

**Super-Potatoes** sera personnalisable avec l'utilisation de paramétrage custom.

La base de données n'est pas encore finie, le Modèle Conceptuel de Donnée change souvent en ce moment. Merci, les stylos effaçables.

Bref pour l'instant le back end est en construction. Quand le mcd sera dans une version stable avec les Modèles et crud créer je passerais au développement de la partie authentification. Utiliser Flask JWT extends me semble une bonne idée pour géré les tokens de session.

Évidemment, j'essayais de faire du python POO, mais sans utiliser les bons outils, j'ai oublié SQLAlchemy pour faire les modèles ... Du coup le mystère du pourquoi ça ne veut pas est résolu.

## La Conception Générale

Un User peut créer :
* Un ou plusieurs projets (*pas pour tout de suite mais la table est presente dans le MCD*)
* Le projet aura une ou plusieurs taches
* une tache aura 0 ou plusieurs items.

**React va me permettre de faire du drag'N drop !**

Les taches seront :
* triées par module (personnalisable)
* triées par étape (personnalisable)
* triées par statut (personnalisable)
* trièes pas ordre (personnalisable)

## Les Views
 * **login/logout**
 * **Vue Global des projets**
 * **Dashbord**
   * **Modale :**
        * Ajout de taches
        * Detail de la tache
        * Ajout des items dans la tache


### Mhé
Le readme sera modifier au fur et a mesure. Pour les commandes, elles seront dans le fichier ***start_project.md***

