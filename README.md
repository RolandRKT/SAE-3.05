# SAE-3.05 - Projet 5

# Application générique pour la proposition de parcours

## Origine du projet
  Ce projet consiste à créer un site internet en flask qui va permettre au client (association, societé et institution) de choisir parmi les differents parcours (escape Game, course...)
  Ces différents parcours sont des enchaînements d'étapes.
  Le site internet devra contenir deux modules.
  En bref :  
    - Le module administrteur doit pouvoir créer des parcours ainsi que les consulter.  
    - Le module client doit pouvoir consulter les parcours, en choisir, choisir ses differentes étapes et autres.  
  
Nous avons choisi d'appeler l'application : Wade.  
  
## **_Équipe_**:
(AB) Ahmet BABA  
(MP) Maverick PREVOST  
(RDD) Rebson Dodji DAHOUEDE  
(RR) Roland RAKOTOMALALA  
(TSL) Thibault SAINT-LÉGER  

Back-End :  
Ahmet BABA  
Rebson Dodji DAHOUEDE  
Thibault SAINT-LÉGER

Front-End:  
Maverick PREVOST  
Roland RAKOTOMALALA  

Conception:  
Maverick PREVOST  
Rebson Dodji DAHOUEDE  
Thibault SAINT-LÉGER  

Completion du README:
Roland RAKOTOMALALA  
Thibault SAINT-LÉGER  

## **Travail effectué lors de la première semaine**:
### Jour 1 :
  - (MP, RR) Création et finition de la première version des CU
  - (AB, RDD, TSL) Conception du MCD
  - (AB, RDD) Implémentation de la BD
  - (MP, RR) Implémentation de la page login
  - (RR) Rédaction README

### Jour 2:
 (Thibault absence justifié)
  - (RDD) Conception de la maquette de la page home
  - (MP) Corrections de bug de fonctionnement sur les environnements de l'IUT
  - (MP, RR) Implémentation de la maquette de la page home
  - (AB, RDD) Conception MCD (suite)
  - (AB, RDD) Création des tables en SQLAlchemy (flask)
  - (RR) Rédaction README

### Jour 3:
  - (AB, RDD, TSL) Changement de l'implémentation des tables (python)
  - (RDD) Conception de trigger
  - (MP, RR) Problèmes régler au niveau des footers et animations
  - (MP, RR) Conception de la version mobile du site
  - (TSL) Rédaction README

### Jour 4:
  - (MP, RR) Responsivité de la page login sur PC
  - (TSL) CU textuelle (scénario nominal, alternatif, exception)
  - (TSL) Diagramme d'activité
  - (RDD) Maquettes
  - (AB) SQLAlchemy
  - (TSL) Rédaction README

### Jour 5:
  - (TSL) CU textuelle (scénario nominal, alternatif, exception)
  - (TSL) Diagramme d'activité
  - (AB, RDD) Modification de la BD et le python
  - (RR) Responivité de la page Inscription PC
  - (MP) Mode paysage
  - (AB, RR) Merge branche Front-End, Back-End
  - (RR) Nettoyage CSS, HTML
  - (TSL) Rédaction README

### Jour 6: 
  - (AB) Fonctionnalité Connexion / Inscription, recherche parcours
  - (RR) Implémentation MAP
  - (TSL) Correction BD
  - (RDD) Nouvelles maquettes, petites corrections BD (python)
  - (MP, RR) Implémentation de la page parcours
  - (AB, RDD, TSL) Modification BD
  - (MP) Version mobile de la page Parcours
  - (RR) Responsivité de la page Parcours version PC
  - (AB) Commencement de la page création Parcours
  - (TSL) Rédaction README

### Jour 7:
  - (AB, MP) Début pages des parcours 
  - (AB) Afficher les images, implémentation pages portails, docstring
  - (TSL) Implémentation connexion Admin, modification BD (Python, SQL) + correction BD
  - (RR) Correction des liens, Ajout de base Flask (Pour les extends), Responsivité page home et parcours, Début page profil
  - (MP) Page mobile vertical horizontal (Parcours)
  - (RDD) Nouvelles maquettes, rédaction README

### Jour 8:
  - (AB) Début page mon-profil, rédaction README
  - (RDD, MP) Page admin
  - (MP) Recherche sur la page les-parcours
  - (TSL) Sommaire page les-parcours, changement sur la localisations de l'étape sur la base de données et début de la map
  - (RR) menu burger, correction route, fixer le header base slogan

### Jour 9
  - (AB) fin page mon-profil, correction connection pour les mobils et rédaction README
  - (RDD) Fin page admin
  - (RR, TSL) Vue client parcours
  - (MP) version mobile

### Jour 10
  - (MP) version mobile, finalisation page admin
  - (RDD) Début page création parcours, rédaction README
  - (TSL) Implémentation de la Map et page HTML
  - (RR) Début page "Mes Parcours"
  - (AB) Début page Gestion des comptes (Admin)
### Jour 11
  - (RR) Correction BD, page "Mes parcours" finie, aider Ahmet
  - (RDD) page création parcours en cours, README
  - (AB) Page gestion de comptes et résolution du problème de la connexion
  - (TSL) Implémentation de la Map en cours
  - (MP) Page mobile login admin et portails
### Jour 12
  - (RDD) Finalisation de l'implémentation du design de la page parcours
  - (TSL) Finalisation de l'implémentation de la map (admin/client) + BD
  - (AB, TSL) Liaison de la map avec la page les_parcours.html
  - (AB) Refactoring du view.py et des fichiers BD
  - (MP) Implémentation de la page mon_profil et le côté admin ver mobile
  - (RR) Implémentation du darkmode, Implémentation de l'envoie de mail,  implémentation de la page mes_parcours (en cours et terminé), Readme
### Jour 13
  - (AB) Corrections des méthodes permettant d'obtenir la liste des parcours par utilisateur
  - (MP) Finalisation du landscape pour mobile + implémentation ver mobile de la page mes_parcours
  - (TSL) Ajout de la fonctionalitée supprimer étape + supprimer parcours
  - (RDD) Ajout de la possibilité d'ajouter une ou plusieurs étapes à un parcours et une durée.
  - (RR) Readme, Finalisation de la page pour le mot de passe oublié, création du fichier message.py, lien avec la BD pour l'envoie de message, correction du fichier bash pour l'installation de modules
### Jour 14
  - (RDD) Readme, La page de création de parcours est fini, Implémentation de la page liste Avis sur un parcours
  - (AB) Ajout d'une table supplémentaire à la BD (TERMINE) et tout les changement sur les pages concernant ce changement.
  - (RR) Ajout de la possibilité de modifier les étapes, et création de la page validation étape + lien avec la page admin et parcours
  - (MP)
  - (TSL) Liaison map client avec la classe SUIVRE dans la BD, Assiste Maverick dans la création de la page laisser un avis avec le lien à la BD, correction map côté admin
### Jour 15
  - (RDD) Readme, bilan collectif et individuel du rapport
  - (AB) bilan individuel
  - (RR) Correction de la map les parcours (la redirection sur la map ne fonctionnait plus), ajustement pour l'envoi de mail, Insertion de tests pour la soutenance, création de la BD en locale pour préparer la démonstrations
  - (MP) Diaporama soutenance
  - (TSL) Map sur parcours mobile rendu opérationnel, affichage de la description des étapes
