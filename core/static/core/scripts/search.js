document.addEventListener("DOMContentLoaded", function () {

    const resultsContainer = document.getElementById("resultsContainer");
    const filters = document.querySelectorAll(".filter");
    const searchInput = document.getElementById("searchInput");
    const searchBtn = document.getElementById("searchBtn");
    const queryText = document.getElementById("searchQueryText");

    searchBtn.addEventListener("click", function () {
        const query = searchInput.value.trim();
        queryText.innerHTML = `Showing results for: <strong>${query}</strong>`;
    });


    // Example Dummy Data
//     const results = [
//         { type: "movie", title: "Avengers: Secret Wars", image: "images/image.jpg", link: "movie-details.html" },
//         { type: "series", title: "Loki Season 2", image: "images/image.jpg", link: "series-details.html" },
//         { type: "news", title: "Marvel Announces Phase 6", image: "images/image.jpg", link: "news-details.html" },
//         { type: "actor", title: "Robert Downey Jr.", image: "images/image.jpg", link: "actor-details.html" }
//     ];

//     function renderResults(filterType = "all") {
//         resultsContainer.innerHTML = "";

//         const filtered = filterType === "all"
//             ? results
//             : results.filter(item => item.type === filterType);

//         filtered.forEach(item => {
//             const card = document.createElement("div");
//             card.classList.add("result-card");

//             card.innerHTML = `
//                 <img src="${item.image}" alt="${item.title}">
//                 <div class="result-content">
//                     <h3>${item.title}</h3>
//                     <span>${item.type.toUpperCase()}</span>
//                 </div>
//             `;

//             card.addEventListener("click", () => {
//                 window.location.href = item.link;
//             });

//             resultsContainer.appendChild(card);
//         });
//     }

//     filters.forEach(button => {
//         button.addEventListener("click", function () {
//             filters.forEach(btn => btn.classList.remove("active"));
//             this.classList.add("active");
//             renderResults(this.dataset.type);
//         });
//     });

//     searchBtn.addEventListener("click", function () {
//         const query = searchInput.value.trim();
//         queryText.innerHTML = `Showing results for: <strong>${query}</strong>`;
//     });

//     renderResults();
});
