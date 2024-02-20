function showPopup(message) {
    alert(message);
}

document.querySelector('.form-inscription').addEventListener('submit', function (event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    fetch('{{url_for("inscription")}}', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error === 'exists') {
            showPopup('Votre pseudo ou mail est déjà enregistrer.');
            window.location.href = '{{url_for("inscription")}}';
        } else if (data.success === 'registered') {
            showPopup('Vérifiez votre boîte mail pour le code de vérification.');
            window.location.href = `{{url_for("get_token", email=${data.email})}}`;
        }
    })
    .catch(error => {
        console.error('Erreur lors de la requête fetch:', error);
        // Gérer les erreurs, par exemple afficher un message d'erreur à l'utilisateur
    });
});
