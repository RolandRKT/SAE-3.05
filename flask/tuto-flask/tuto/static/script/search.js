function search() {
    var query = document.querySelector('input[name="query"]').value.toLowerCase(); 
    var parcoursElements = document.querySelectorAll('.box-parcours');
    parcoursElements.forEach(function(element) {
        var h3Text = element.querySelector('h3').textContent.toLowerCase();
        if (h3Text.includes(query)) {
            element.style.display = 'flex';
        } else {
            element.style.display = 'none';
        }
    });
}