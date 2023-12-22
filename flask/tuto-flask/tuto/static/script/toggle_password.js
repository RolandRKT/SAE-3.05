function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var togglePassword = document.getElementById("togglePassword");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.src = "../static/images/oeilOuvert.png";
    } else {
        passwordInput.type = "password";
        togglePassword.src = "../static/images/oeilFerme.png";
    }
}
