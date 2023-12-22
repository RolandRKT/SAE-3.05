var nb_etape =  document.getElementById("id_etape").classList[0]
console.log(nb_etape)
var coord_X = document.getElementById("coord_X_" + nb_etape).classList[0];
console.log(coord_X);
var coord_Y = document.getElementById("coord_Y_" + nb_etape).classList[0];
console.log(coord_Y);


var parcours1 = L.map('map').setView([coord_X, coord_Y], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(parcours1);

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
    createMarker: function() {
        return null;
    }
}).addTo(parcours1);

function hideGuidage() {
    document.addEventListener('DOMContentLoaded', function () {
        const guidage = document.querySelector(".leaflet-routing-container");
        guidage.classList.add('hidden-content');
    })
}

function showGuidage() {
    document.addEventListener('DOMContentLoaded', function () {
        const guidage = document.querySelector(".leaflet-routing-container");
        guidage.classList.remove('hidden-content');
    })
}

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

// var step = addMarker(parcours1, 47.8432, 1.92661, "BUT Informatique", "Point de départ", true);
// var step1 = addMarker(parcours1, 47.84395, 1.93274, "Restaurant Universitaire", "Étape 1");
// var step2 = addMarker(parcours1, 50.84395, 1.93274, "Restaurant Universitaire", "Étape troll");

// addDirection(step, step1, false);

var x = 1;
var nom = 1;
var liste_id = []
var listeEtape = [];

// Créez la fonction pour supprimer un marqueur
function removeMarker(marker) {
    marker.removeFrom(parcours1); // Supprimez le marqueur de la carte
}


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

// Utilisation de la nouvelle fonction
addMarkerAndDirection(parcours1, coord_X, coord_Y, "hmmmm", "Etape " + nb_etape);

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
