#! bin/bash
#Script permettant d'installer les modules nécessaire à l'éxécution du flask.

read -p " Voulez-vous installer le dossier venv (seulement si vous ne l'avez pas) ? o/n " venv

if [ "$venv" = "o" ]; then
    echo "--------------------"
    echo "Installation du dossier venv"
    virtualenv -p python3 venv
    echo "--------------------"
    echo "VEUILLEZ entrer 'n' pour les installations suivantes si vous souhaitez installer les autres modules dans l'environnement venv."
    echo "Effectuez la commande 'source venv/bin/activate' et relancez le script pour installer dans cet environnement les modules."
    echo "Sinon continuez avec 'o' mais dans ce cas, le dossier venv est inutile."
    echo "--------------------"
fi

read -p " Voulez-vous installer le module flask ? o/n " reponse0

if [ "$reponse0" = "o" ]; then
    echo "--------------------"
    echo "Installation du module flask"
    pip install flask
    echo "--------------------"
    echo "Installation de python-dotenv"
    pip install python-dotenv
    echo "--------------------"
fi

read -p " Voulez-vous installer le module yaml ? o/n " reponse1

if [ "$reponse1" = "o" ]; then
    echo "Installation du package Yaml"
    pip install pyyaml
    echo "--------------------"
fi

read -p " Voulez-vous installer le module bootstrap-flask ? o/n " reponse2

if [ "$reponse2" = "o" ]; then
    echo "Installation du package Yaml"
    pip install bootstrap-flask
    echo "--------------------"
fi

read -p " Voulez-vous installer le module SQL-ALCHEMY ? o/n " reponse3

if [ "$reponse3" = "o" ]; then
    echo "--------------------"
    echo "Installation du module SQL-ALCHEMY"
    pip install flask-sqlalchemy
    echo "--------------------"
fi

read -p " Voulez-vous installer le module flask-wtf ? o/n " reponse4

if [ "$reponse4" = "o" ]; then
    echo "--------------------"
    echo "Installation du module flask-wtf"
    pip install flask-wtf
    echo "--------------------"
fi

read -p " Voulez-vous installer le module flask-login ? o/n " reponse5

if [ "$reponse5" = "o" ]; then
    echo "--------------------"
    echo "Installation du module flask-login"
    pip install flask-login
    echo "--------------------"
fi

read -p " Voulez-vous installer le module mysql-connector-python ? o/n " reponse6

if [ "$reponse6" = "o" ]; then
    echo "--------------------"
    echo "Installation du module mysql-connector-python"
    pip install mysql-connector-python
    echo "--------------------"
fi