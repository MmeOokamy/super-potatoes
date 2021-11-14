*Mes projets ne sont pas souvent détaillés dans la partie readme. Je suis une adepte du cahier ! J'ai toujours un cahier pour noter mes idées et ma conception. Que cela soit professionnel ou personnel. C'est un peu ma méthode de suivi.*


# Super-Potatoes:
*****************************************************
Good News! le site est en prod xD  => ***https://mme.ookamy.fr/*** 
 * Il a fallut que je modiffi la base de donnée qui etait pour postgreSQL en MySQL friendly xD 
*****************************************************

Changement de direction avec **Super-Potatoes**, le but c'est de mettre en ligne un site avec ma doc et un tableau de bord de gestion de projet. 
Un Kanban, un **tableau de bord** qui me permettra de suivre mes futurs projets et de pouvoir y accéder partout.

**Super-Potatoes** sera personnalisable avec l'utilisation de paramétrage custom.

La base de données n'est pas encore finie, le Modèle Conceptuel de Donnée change souvent en ce moment. Merci, les stylos effaçables.

Le MCD a completement changer de tête -> **schema.sql**

Évidemment, j'essayais de faire du python POO, mais sans utiliser les bons outils, j'ai oublié SQLAlchemy pour faire les modèles ... Du coup, le mystère du' pourquoi ça ne veut pas' est résolu.

D'ailleurs la manipulation des tasks dans les colonne pourront etre geré avec le **drag'n drop**

Ah et j'aime bien ce petit guide *https://hackersandslackers.com/your-first-flask-application* c'est sur onze chapitres.

## La Conception Générale

 * Flask, jinja, postgresql, token, javascript/jquery(ou autre)
 * Framework CSS => on va tester Semantic UI (NO WAY) => On va vers **Bulma**!!

# todo
 - revoir tout les chemins  static / template
 - refaire la connexion a la bdd postgresql psycopg2
 - revoir la maquette du site et les different chemins

# LES MODULES
*divers modif: debut d'ajout des blueprint avec template et static dans le meme module comme ça chaque module sera independant*
### Module Authentification - loggin / loggout
### Module Logs - suivre les modifs de la bdd (trigger?)
### Module Parameters - Personnalisation de l'appli - couleurs - nom des champs-
### Module Ookamanager - Project Management - Tableau de bord - Gestion de projet -
### Module Ookarchyves - Mes docs - archives -

### Mhé
Le readme sera modifier au fur et a mesure. Pour les commandes, elles seront dans le fichier ***start_project.md***

