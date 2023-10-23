// Récupérez l'élément du DOM
const animatedImage = document.getElementById('animation-button');
const animatedImage1 = document.getElementById('animation-button1');

// Gérez le clic sur l'image
animatedImage.addEventListener('click', function() {
  animatedImage.style.transform = 'translateX(100vw)'; // Déclenche l'animation
  // mettre un délai de 2s avant de faire la suite
  setTimeout(function() {
    animatedImage1.style.transform = 'translateX(-8vw) scaleX(-1)';
  }, 2000); // 2 secondes de délai
});
