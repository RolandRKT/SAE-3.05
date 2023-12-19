// Récupérer la classe du premier élément ayant l'ID "num_parcours"
var num_parcours = document.getElementById("num_parcours").classList[0];

// Récupérer la classe du premier élément ayant l'ID "id_etape"
var nb_etape = document.getElementById("id_etape").classList[0];

// Construire les classes des éléments coordonnées X et Y basées sur "nb_etape"
var coord_X = document.getElementById("coord_X_" + nb_etape).classList[0];
var coord_Y = document.getElementById("coord_Y_" + nb_etape).classList[0];

// Initialiser une carte Leaflet avec les coordonnées X et Y
var parcours1 = L.map('map').setView([coord_X, coord_Y], 13);

// Ajouter une couche de tuiles OpenStreetMap à la carte
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(parcours1);

// Initialiser le contrôle des itinéraires Leaflet
var directionsControl = L.Routing.control({
    waypoints: [],
    lineOptions: {
        styles: [
            {
                color: 'deepskyblue',
                opacity: 0.6,
                weight: 6
            }
        ]
    },
    createMarker: function () {
        return null;
    }
}).addTo(parcours1);

// Fonction pour masquer le guidage
function hideGuidage() {
    const guidage = document.querySelector(".leaflet-routing-container");
    guidage.classList.add('hidden-content');
}

// Fonction pour afficher le guidage
function showGuidage() {
    const guidage = document.querySelector(".leaflet-routing-container");
    guidage.classList.remove('hidden-content');
}

// Fonction pour ajouter un marqueur à la carte
function addMarker(map, coordX, coordY, messagePopUp = "", desc = "", depart = false) {
    var marker = L.marker([coordX, coordY]).addTo(map);
    if (messagePopUp !== "") {
        if (desc !== "") {
            marker.bindPopup("<b>" + messagePopUp + "</b><br>" + desc);
            if (depart) {
                marker.openPopup();
            }
        } else {
            marker.bindPopup("<b>" + messagePopUp + "</b><br>Aucune description").openPopup();
        }
    }
    return marker;
}

// Fonction pour ajouter une direction entre deux marqueurs
function addDirection(departure, destination, guidage = true, couleur = "") {
    var waypoints = [];

    var departureLatLng = departure.getLatLng();
    var destinationLatLng = destination.getLatLng();

    var waypoint1 = L.latLng(departureLatLng.lat, departureLatLng.lng);
    var waypoint2 = L.latLng(destinationLatLng.lat, destinationLatLng.lng);

    waypoints.push(waypoint1);
    waypoints.push(waypoint2);

    var lineOptions = {
        styles: [{
            color: couleur || 'deepskyblue',
            opacity: 0.6,
            weight: 6
        }]
    };

    directionsControl.setWaypoints(waypoints, lineOptions);

    if (!guidage) {
        hideGuidage();
    }
}

// Liste pour stocker les étapes et les identifiants
var listeEtape = [];
var liste_id = [];
var fait = false;

// Fonction pour ajouter un marqueur et une direction entre les marqueurs
function addMarkerAndDirection(map, coordX, coordY, messagePopUp = "", desc = "", id, depart = false) {
    var marker = L.marker([coordX, coordY]).addTo(map);

    if (messagePopUp !== "") {
        if (desc !== "") {
            marker.bindPopup("<b>" + messagePopUp + "</b><br>" + desc);
            if (depart) {
                marker.openPopup();
            }
        } else {
            marker.bindPopup("<b>" + messagePopUp + "</b><br>Aucune description").openPopup();
        }
    }

    listeEtape.push(marker);
    liste_id.push(id);

    if (listeEtape.length > 1) {
        if (liste_id[liste_id.length - 2] > nb_etape - 1 && fait == false) {
            var previousMarker = listeEtape[listeEtape.length - 2];
            addDirection(previousMarker, marker, false);
            fait = true;
        }
    }

    return marker;
}

// Fonction pour appeler une fonction Python via une requête HTTP
function appelerFonctionPython() {
    fetch('http://127.0.0.1:5000/appel-fonction-python')
        .then(response => response.json())
        .then(data => {
            listeEtape = data.resultat;
            alert(data.resultat);

            var tableauSansIndices = listeEtape.map(function(element) {
                return {
                    coordonneX: element.coordonneX,
                    coordonneY: element.coordonneY,
                    id_etape: element.id_etape
                };
            });

            for (var i = 0; i < tableauSansIndices.length; i++) {
                var etape_actu = listeEtape[i];
                addMarker(parcours1, etape_actu.coordonneX, etape_actu.coordonneY, etape_actu.nom_etape, "Point de départ");
            }
        })
        .catch(error => console.error('Erreur :', error));
}

// Écouteur d'événement pour le chargement du DOM
document.addEventListener('DOMContentLoaded', function () {
    // Récupérer la liste des étapes depuis l'attribut de données
    var listeEtapes = JSON.parse(document.body.getAttribute('data-liste-etapes'));

    // Utiliser la liste dans votre code JavaScript
    for (var i = 0; i < listeEtapes.length; i++) {
        var etape = listeEtapes[i];
        addMarkerAndDirection(parcours1, etape.coordonneX, etape.coordonneY, etape.nom, "Description de l'étape", etape.id);
    }
});
