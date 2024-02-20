drop table TERMINE;
drop table SUIVRE;
drop table POSSEDER;
drop table COMPOSER;
drop table INTERETETAPE;
drop table ETAPE;
drop table PARCOURS;
drop table PARTICIPANT;
drop table IMAGE;


CREATE TABLE PARCOURS (
    id_parcours INT PRIMARY KEY,
    nom_parcours VARCHAR(20),
    duree TIME,
    description_parcours VARCHAR(200),
    id_image int,
    CHECK('00:05:00' < duree )
);

CREATE TABLE PARTICIPANT (
    id_participant int PRIMARY KEY,
    pseudo varchar(200),
    email varchar(200),
    mdp varchar(200)
);

create table IMAGE (
    id_image int primary key,
    nom_image varchar(200),
    img_data varchar(200),
    nom_fic varchar(200)
);

create table ETAPE (
    id_etape int primary key,
    nom_etape varchar(200),
    id_image int,
    coordonneX float,
    coordonneY float,
    interet varchar(200),
    question varchar(200),
    reponse varchar(200)
);

create table SUIVRE (
    id_participant int,
    id_parcours int,
    num_etape int,
    primary key(id_parcours,id_participant)
);

create table COMPOSER (
    id_parcours int,
    id_etape int,
    numero int,
    primary key (id_parcours,id_etape)
);

create table ADMIN(
    id_admin int,
    pseudo varchar(200),
    mdp varchar(200),
    primary key(id_admin)
);

create table TERMINE(
    id_parcours int,
    id_participant int,
    note decimal(2,1),
    comm varchar(500),
    CHECK(0 <= note and 5 >= note),
    primary key(id_parcours,id_participant)
);

-- ALTER TABLE pour attribuer les foreign key

ALTER TABLE PARCOURS ADD UNIQUE (nom_parcours);

ALTER TABLE PARCOURS ADD FOREIGN KEY (id_image) REFERENCES IMAGE(id_image);

ALTER TABLE TERMINE ADD FOREIGN KEY (id_parcours) REFERENCES PARCOURS(id_parcours);

ALTER TABLE TERMINE ADD FOREIGN KEY (id_participant) REFERENCES PARTICIPANT(id_participant);

ALTER TABLE IMAGE ADD UNIQUE (nom_image);

ALTER TABLE IMAGE ADD UNIQUE (nom_fic);

ALTER TABLE PARTICIPANT ADD UNIQUE (email);

ALTER TABLE PARTICIPANT ADD UNIQUE (pseudo);

ALTER TABLE ETAPE ADD FOREIGN KEY (id_image) REFERENCES IMAGE(id_image);

ALTER TABLE SUIVRE ADD FOREIGN KEY (id_parcours) REFERENCES PARCOURS(id_parcours);

ALTER TABLE SUIVRE ADD FOREIGN KEY (id_participant) REFERENCES PARTICIPANT(id_participant);

ALTER TABLE COMPOSER ADD FOREIGN KEY (id_parcours) REFERENCES PARCOURS(id_parcours);

ALTER TABLE COMPOSER ADD FOREIGN KEY (id_etape) REFERENCES ETAPE(id_etape);

DELIMITER |
CREATE FUNCTION NombreEtapeParcours(parcours_id INT) RETURNS INT
BEGIN
    DECLARE num_steps INT;
    
    SELECT COUNT(*) INTO num_steps
    FROM COMPOSER
    WHERE id_parcours = parcours_id;
    
    RETURN num_steps;
END;
|
DELIMITER ;


DELIMITER |
CREATE TRIGGER BeforeUpdateSuivre BEFORE UPDATE ON SUIVRE FOR EACH ROW
BEGIN
    DECLARE total_steps INT;
    
    -- Utilisez la fonction pour obtenir le nombre total d'étapes pour le parcours en question
    SET total_steps = NombreEtapeParcours(NEW.id_parcours);
    
    IF NEW.num_etape > total_steps THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le numéro d''étape dépasse le nombre total d''étapes du parcours.';
    END IF;
END;
|
DELIMITER ;
