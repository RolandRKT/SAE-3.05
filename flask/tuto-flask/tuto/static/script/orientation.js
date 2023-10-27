window.addEventListener("orientationchange", function() {
    if (window.orientation === 90 || window.orientation === -90) {
      // L'appareil est en mode paysage, forcer le mode portrait
      if (window.orientation === 90) {
        document.body.style.transform = "rotate(-90deg)";
      } else {
        document.body.style.transform = "rotate(90deg)";
      }
    } else {
      // L'appareil est en mode portrait, remettre à zéro la transformation
      document.body.style.transform = "none";
    }
  });
  