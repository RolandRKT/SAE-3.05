var path = window.location.pathname;  // Récupère la route actuelle du navigateur
console.log("a");
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    console.log("b");
    if (path === '/') {  // Compare avec la route racine
        console.log("c");
        // Demande au serveur Python de rediriger vers la nouvelle route
        axios.get('/redirect_home_mobile')
          .then(function (response) {
            console.log("Redirection effectuée.");
          })
          .catch(function (error) {
            console.error(error);
          });
    }
    if (path.endsWith("?")) {
        window.location.href = path.slice(0, -1);
    } else if (!(path.endsWith("_mobile"))) {
        console.log("d");
        window.location.href = path + '_mobile';
    }
} else {
    console.log("e");
    if (path.endsWith("_mobile")) {
        console.log("f");
        window.location.href = path.slice(0, -7);
    }
}