// Récupérez tous les liens de la page
const links = document.querySelectorAll('a');
const animatedImage = document.getElementById('animation-button');
const animatedImage1 = document.getElementById('animation-button1');

// Fonction pour gérer le clic sur n'importe quel lien
function handleLinkClick(event) {
  event.preventDefault(); // Empêche le lien de déclencher la navigation par défaut

  animatedImage.style.transform = 'translateX(100vw)'; // Déclenche l'animation

  // Mettez un délai de 0.5s avant de naviguer vers le lien
  setTimeout(function () {
    window.location = event.target.href; // Navigue vers le lien
  }, 600); // 0.5 seconde de délai
}

// Ajoutez le gestionnaire d'événements à tous les liens
links.forEach(link => {
  link.addEventListener('click', handleLinkClick);
});
