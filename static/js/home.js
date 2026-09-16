

function toggleSearch() {
    const searchBox = document.getElementById("searchBox");

    if (searchBox) {
        searchBox.classList.toggle("active");

        if (searchBox.classList.contains("active")) {
            const input = document.getElementById("searchInput");

            if (input) {
                input.focus();
            }
        }
    }
}


// -------------------------
// MOBILE MENU
// -------------------------

function toggleMenu() {

    const navbar = document.querySelector(".navbar");

    if (!navbar) {
        return;
    }

    if (navbar.style.display === "flex") {

        navbar.style.display = "";

    } else {

        navbar.style.display = "flex";

        navbar.style.position = "absolute";
        navbar.style.top = "76px";
        navbar.style.left = "0";
        navbar.style.right = "0";
        navbar.style.flexDirection = "column";
        navbar.style.alignItems = "flex-start";
        navbar.style.padding = "20px 4%";
        navbar.style.background = "#ffffff";
        navbar.style.borderBottom = "1px solid #e5e9f2";
        navbar.style.boxShadow = "0 10px 30px rgba(0,0,0,0.08)";
    }
}


// -------------------------
// SEARCH ENTER KEY
// -------------------------

const searchInput = document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keypress", function(event) {

        if (event.key === "Enter") {

            const searchValue = searchInput.value.trim();

            if (searchValue !== "") {

                window.location.href =
                    "/laptops/?search=" +
                    encodeURIComponent(searchValue);

            }

        }

    });

}


// -------------------------
// CLOSE SEARCH WITH ESC
// -------------------------

document.addEventListener("keydown", function(event) {

    if (event.key === "Escape") {

        const searchBox = document.getElementById("searchBox");

        if (searchBox) {
            searchBox.classList.remove("active");
        }

    }

});


// -------------------------
// CLOSE MOBILE MENU
// -------------------------

document.querySelectorAll(".navbar a").forEach(function(link) {

    link.addEventListener("click", function() {

        if (window.innerWidth <= 1000) {

            const navbar = document.querySelector(".navbar");

            if (navbar) {
                navbar.style.display = "";
            }

        }

    });

});


// -------------------------
// SIMPLE SCROLL ANIMATION
// -------------------------

const animatedElements = document.querySelectorAll(
    ".product-card, .why-card, .service-card, .review-card, .brand-card"
);

const observer = new IntersectionObserver(

    function(entries) {

        entries.forEach(function(entry) {

            if (entry.isIntersecting) {

                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";

            }

        });

    },

    {
        threshold: 0.1
    }

);


animatedElements.forEach(function(element) {

    element.style.opacity = "0";
    element.style.transform = "translateY(20px)";
    element.style.transition = "opacity 0.5s ease, transform 0.5s ease";

    observer.observe(element);

});

