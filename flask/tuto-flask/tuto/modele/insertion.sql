-- Insertion des données dans la table PARCOURS
INSERT INTO PARCOURS (id_parcours, nom_parcours, duree, description_parcours, id_image)
VALUES (1, 'Parcours A', '00:30:00', 'Description du parcours A', 1),
       (2, 'Parcours B', '01:15:00', 'Description du parcours B', 2),
       (3, 'Parcours C', '01:15:00', 'Description du parcours C', 1),
       (4, 'Parcours D', '01:15:00', 'Description du parcours D', 2);
-- Insertion des données dans la table PARTICIPANT
INSERT INTO PARTICIPANT (id_participant, pseudo, email, mdp)
VALUES (1, 'test', 'test@example.com', 'test'),
       (2, 'Utilisateur2', 'utilisateur2@example.com', 'motdepasse2');

-- Insertion des données dans la table IMAGE
INSERT INTO IMAGE (id_image, nom_image, img_data, nom_fic)
VALUES (1, 'Image1', '', 'image1.jpg'),
       (2, 'Image2', '', 'image2.jpg'),
       (3, 'Image3', '', 'image3.jpg');

-- Insertion des données dans la table ETAPE
INSERT INTO ETAPE (id_etape, nom_etape, id_image, coordonneX, coordonneY, interet)
VALUES (1, 'Monument', 1, 10.5, 20.3, 'permet de visite un monument'),
       (2, 'Stade', 2, 15.2, 25.8, 'permet de visite un stade'),
       (3, 'Parc', 3, 15.2, 25.8, 'permet de visite un parc'),
       (4, 'Musee', 3, 15.2, 25.8, 'permet de visite un musee');
       
-- Insertion des données dans la table SUIVRE
INSERT INTO SUIVRE (id_participant, id_parcours, num_etape)
VALUES (2, 2, 2),
       (1,3,1);

-- Insertion des données dans la table COMPOSER
INSERT INTO COMPOSER (id_parcours, id_etape, numero)
VALUES (1, 1, 1),
       (1, 2, 2),
       (2, 2, 1),
       (2, 3, 2),
       (2, 4, 3),
       (3, 1, 1),
       (3, 2, 2),
       (3, 3, 3);



-- Insertion des données dans la table ADMIN
INSERT INTO ADMIN (id_admin, pseudo, mdp)
VALUES (1, 'adm', 'adm');

-- Insertion des données dans la table TERMINE
INSERT INTO TERMINE (id_parcours, id_participant, note, comm)
VALUES (1, 1, 4.5, 'Très bon parcours !');
