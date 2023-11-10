function togglePassword() {
    var passwordInput = document.getElementById("passwordInput");
    var toggleButton = document.querySelector(".show-password-btn");

    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      toggleButton.textContent = "Cacher";
    } else {
      passwordInput.type = "password";
      toggleButton.textContent = "Afficher";
    }
  }