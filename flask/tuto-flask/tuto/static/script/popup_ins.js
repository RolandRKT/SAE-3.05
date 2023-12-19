function showPopup(message) {
    alert(message);
}

document.querySelector('.form-inscription').addEventListener('submit', function (event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    fetch('{{url_for("inscrire")}}', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error === 'exists') {
            showPopup('Votre pseudo ou mail est déjà enregistrer.');
            window.location.href = '{{url_for("login")}}';
        } else if (data.success === 'registered') {
            showPopup("Merci d'avoir rejoint Wade pour de nouveaux parcours.");
            window.location.href = '{{url_for("les_parcours")}}';
        }
    });
});