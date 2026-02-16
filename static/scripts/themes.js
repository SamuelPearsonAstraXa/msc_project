document.addEventListener("DOMContentLoaded", function () {

    const body = document.body;
    const toggleBtn = document.getElementById("themeToggle");
    body.classList.add("dark");
    
    // Detect saved theme
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme) {
        body.classList.add(savedTheme);
    } else {
        // Detect system preference
        if (window.matchMedia("(prefers-color-scheme: light)").matches) {
            body.classList.add("light");
        } else {
            body.classList.add("dark");
        }
    }

    updateIcon();

    toggleBtn.addEventListener("click", function () {
        if (body.classList.contains("dark")) {
            body.classList.replace("dark", "light");
            localStorage.setItem("theme", "light");
        } else {
            body.classList.replace("light", "dark");
            localStorage.setItem("theme", "dark");
        }

        updateIcon();
    });

    function updateIcon() {
        if (body.classList.contains("dark")) {
            toggleBtn.innerHTML = "<i class='fas fa-moon'></i>";
        } else {
            toggleBtn.innerHTML = "<i class='fas fa-sun'></i>";
        }
    }

});
