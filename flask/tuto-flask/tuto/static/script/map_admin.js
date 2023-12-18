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

var listeEtape = [];

function onMapClick(event) {
    alert("Coordonnées cliquées : " + event.latlng.lat + ", " + event.latlng.lng);
    var nomEtape = prompt("Nom de l'étape :");
    console.log("Vous avez entré : " + nomEtape);
    x += 1;
    nom += 1;
    var nom = addMarkerAndDirection(parcours1, event.latlng.lat, event.latlng.lng, nomEtape, "Étape " + x);

    nom.on('click', function () {
        removeMarker(nom);
    });
}

parcours1.on('click', onMapClick);

// Créez la fonction pour supprimer un marqueur
function removeMarker(marker) {
    marker.removeFrom(parcours1); // Supprimez le marqueur de la carte
}


function addMarkerAndDirection(map, coordX, coordY, messagePopUp = "", desc = "", depart = false) {
    var marker = L.marker([coordX, coordY]).addTo(map);
    
    // Ajouter le popup au marqueur
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

    listeEtape.push(marker) 
    // Créer la direction avec le point actuel et le précédent
    if (listeEtape.length > 1) {
        var previousMarker = listeEtape[listeEtape.length - 2];
        addDirection(previousMarker, marker, false);
    }

    return marker;
}

// Utilisation de la nouvelle fonction
addMarkerAndDirection(parcours1, coord_X, coord_Y, "hmmmm", "Etape " + nb_etape);