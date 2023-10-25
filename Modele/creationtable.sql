CREATE TABLE PARCOURS (
    id_parcours INT PRIMARY KEY,
    nom_parcours VARCHAR(20),
    date_debut DATETIME,
    date_fin DATETIME,
    description_parcours VARCHAR(200),
    id_image int 
)

CREATE TABLE PARTICIPANT (
    id_participant int primary key,
    email varchar(200),
    mdp varchar(200)
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
    description_etape varchar(320),
    localisation varchar(200),
    id_image int 
)

create table SUIVRE (
    id_participant int,
    id_parcours int,
    note int,
    comm varchar(200),
    primary key(id_parcours,id_participant)
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

ALTER TABLE PARCOURS ADD FOREIGN KEY (id_image) REFERENCES IMAGE(id_image);

ALTER TABLE ETAPE ADD FOREIGN KEY (id_image) REFERENCES IMAGE(id_image);

ALTER TABLE SUIVRE ADD FOREIGN KEY (id_parcours) REFERENCES PARCOURS(id_parcours);

ALTER TABLE SUIVRE ADD FOREIGN KEY (id_participant) REFERENCES PARTICIPANT(id_participant);

ALTER TABLE POSSEDER ADD FOREIGN KEY (id_interet) REFERENCES INTERETETAPE(id_interet);

ALTER TABLE POSSEDER ADD FOREIGN KEY (id_etape) REFERENCES ETAPE(id_etape);

ALTER TABLE COMPOSER ADD FOREIGN KEY (id_parcours) REFERENCES PARCOURS(id_parcours);

ALTER TABLE COMPOSER ADD FOREIGN KEY (id_etape) REFERENCES ETAPE(id_etape);

