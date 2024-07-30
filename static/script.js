document.addEventListener("DOMContentLoaded", function() {
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const slideMenu = document.getElementById("slide-menu");

    hamburgerMenu.addEventListener("click", function() {
        slideMenu.classList.toggle("open");
    });
});