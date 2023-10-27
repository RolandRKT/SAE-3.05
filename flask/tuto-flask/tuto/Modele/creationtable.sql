CREATE TABLE PARCOURS (
    id_parcours INT PRIMARY KEY,
    nom_parcours VARCHAR(20),
    date_debut DATETIME,
    date_fin DATETIME,
    description_parcours VARCHAR(200),
    id_image int,
    CHECK(date_debut < date_fin)
)

CREATE TABLE PARTICIPANT (
    id_participant int primary key,
    email varchar(200),
    mdp varchar(200)
)

CREATE TABLE INSCRIPTION (
    id_parcours INT,
    id_participant INT,
    date_inscription DATE,
    PRIMARY KEY (id_parcours, id_participant)
)

create table IMAGE (
    id_image int primary key,
    nom_image varchar(200),
    img_data varchar(200),
    nom_fic varchar(200)
)

create table INTERETETAPE (
    id_interet int primary key,
    nom_interet varchar(200),
    description_interet varchar(200)
)

create table ETAPE (
    id_etape int primary key,
    nom_etape varchar(200),
    localisation varchar(200),
    id_image int 
)

create table SUIVRE (
    id_participant int,
    id_parcours int,
    note decimal(2,1),
    comm varchar(200),
    primary key(id_parcours,id_participant),
    CHECK(0 <= note and 5 >= note)
)

create table POSSEDER (
    id_etape int,
    id_interet int,
    primary key(id_interet,id_etape)
)

create table COMPOSER (
    id_parcours int,
    id_etape int,
    primary key (id_parcours,id_etape)
)

-- ALTER TABLE pour attribuer les foreign key

ALTER TABLE PARCOURS ADD UNIQUE (nom_parcours);

ALTER TABLE PARCOURS ADD FOREIGN KEY (id_image) REFERENCES IMAGE(id_image);

ALTER TABLE PARTICIPANT ADD UNIQUE (email);

ALTER TABLE INSCRIPTION ADD FOREIGN KEY (id_parcours) REFERENCES PARCOURS(id_parcours);

ALTER TABLE INSCRIPTION ADD FOREIGN KEY (id_participant) REFERENCES PARTICIPANT(id_participant);

ALTER TABLE ETAPE ADD FOREIGN KEY (id_image) REFERENCES IMAGE(id_image);

ALTER TABLE SUIVRE ADD FOREIGN KEY (id_parcours) REFERENCES PARCOURS(id_parcours);

ALTER TABLE SUIVRE ADD FOREIGN KEY (id_participant) REFERENCES PARTICIPANT(id_participant);

ALTER TABLE POSSEDER ADD FOREIGN KEY (id_interet) REFERENCES INTERETETAPE(id_interet);

ALTER TABLE POSSEDER ADD FOREIGN KEY (id_etape) REFERENCES ETAPE(id_etape);

ALTER TABLE COMPOSER ADD FOREIGN KEY (id_parcours) REFERENCES PARCOURS(id_parcours);

ALTER TABLE COMPOSER ADD FOREIGN KEY (id_etape) REFERENCES ETAPE(id_etape);

-- Fonctions
DELIMITER |
CREATE FUNCTION CalculerDureeParcours(parcours_id INT) RETURNS TIME
BEGIN
    DECLARE debut DATETIME;
    DECLARE fin DATETIME;
    DECLARE duree TIME;

    SELECT date_debut, date_fin INTO debut, fin
    FROM PARCOURS
    WHERE id_parcours = parcours_id;

    SET duree = TIMEDIFF(fin, debut);

    RETURN duree;
END |
DELIMITER ;


-- Déclencheur pour empêcher que les parcours se chevauchent
CREATE TRIGGER beforeInsertParcours BEFORE INSERT ON PARCOURS FOR EACH ROW
BEGIN
    DECLARE existing_count INT;
    
    -- Comptez les parcours existants dont la date de fin est après la nouvelle date de début
    SET existing_count = (
        SELECT COUNT(*)
        FROM PARCOURS
        WHERE (new.date_debut between date_debut AND date_fin) OR (new.date_fin between date_debut and date_fin) 
        OR (new.date_debut < date_debut and new.date_fin > date_fin)
    );
    
    -- Si des parcours se chevauchent, l'insertion est interdite
    IF existing_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Les dates du parcours se chevauchent avec un parcours existant';
    END IF;
END;


-- Déclencheur pour empêcher que les parcours se chevauchent
CREATE TRIGGER beforeUpdateParcours BEFORE UPDATE ON PARCOURS FOR EACH ROW
BEGIN
    DECLARE existing_count INT;
    
    -- Comptez les parcours existants dont la date de fin est après la nouvelle date de début
    SET existing_count = (
        SELECT COUNT(*)
        FROM PARCOURS
        WHERE (new.date_debut between date_debut AND date_fin) OR (new.date_fin between date_debut and date_fin)
        OR (new.date_debut < date_debut and new.date_fin > date_fin)
    );
    
    -- Si des parcours se chevauchent, l'insertion est interdite
    IF existing_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Les dates du parcours se chevauchent avec un parcours existant';
    END IF;
END;

