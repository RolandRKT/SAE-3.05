const menu = document.getElementById("menu");
const burgMenu = document.getElementById("burg-menu");
const documentBody = document.body;

function triggerRotationAnimation() {
    // Ajoutez la classe d'animation pour la rotation
    burgMenu.classList.add("rotate-animation");
    menu.classList.add("fixed-element");
  
    // Supprimez la classe d'animation après un certain délai (1 seconde dans cet exemple)
    setTimeout(function() {
      burgMenu.classList.remove("rotate-animation");
    }, 1000);
}

// Fonction pour afficher le menu
function showMenu() {
    menu.style.display = "block";
    burgMenu.src = "../static/images/fermer.png";
    documentBody.addEventListener("click", closeMenuOnClickOutside);
}

// Fonction pour cacher le menu
function hideMenu() {
    menu.style.display = "none";
    burgMenu.src = "../static/images/menu.png";
    documentBody.removeEventListener("click", closeMenuOnClickOutside);
}

// Gestionnaire d'événement pour le clic sur l'image "burg-menu"
burgMenu.addEventListener("click", function (event) {
    event.stopPropagation(); // Empêche la propagation de l'événement de clic à l'élément parent (document)
    if (menu.style.display === "block") {
        triggerRotationAnimation();
        hideMenu();
    } else {
        triggerRotationAnimation();
        showMenu();
    }
});

// Fonction pour fermer le menu lors d'un clic en dehors du menu
function closeMenuOnClickOutside(event) {
    if (!menu.contains(event.target) && menu.style.display === "block") {
        hideMenu();
    }
}

// Au chargement de la page, assurez-vous que le menu est caché
hideMenu();

