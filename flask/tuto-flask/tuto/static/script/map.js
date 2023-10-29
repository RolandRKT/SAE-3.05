var parcours1 = L.map('map').setView([47.8432, 1.92661], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(parcours1);

function hideGuidage(){
    document.addEventListener('DOMContentLoaded', function(){
        const guidage = document.querySelector(".leaflet-routing-container");
        guidage.classList.add('hidden-content');
    })
}

function showGuidage(){
    document.addEventListener('DOMContentLoaded', function(){
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
            marker.bindPopup("<b>" + messagePopUp + "</b><br>Aucune description");
        }
    }
    return marker;
}

function addDirection(map, departure, destination, guidage = true, couleur = "") {
    var lineOptions = {
        styles: [
            {
                color: 'deepskyblue',
                opacity: 0.6,
                weight: 6
            }
        ]
    };

    if (couleur !== "") {
        lineOptions.styles[0].color = couleur;
    }

    var directions = L.Routing.control({
        waypoints: [
            departure.getLatLng(),
            destination.getLatLng()
        ],
        lineOptions: lineOptions
    }).addTo(map);

    if (!guidage) {
        hideGuidage();
    }
    return directions;
}


step = addMarker(parcours1, 47.8432, 1.92661, "BUT Informatique", "Point de départ", true);
step1 = addMarker(parcours1, 47.84395, 1.93274, "Restaurant Universitaire", "Étape 1");

addDirection(parcours1, step, step1, false);