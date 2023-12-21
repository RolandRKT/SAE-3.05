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
