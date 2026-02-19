async function fetch_movies() {
    try {
        const response = await fetch('/movies/fetch-data');
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const results = await response.json();
        const movies = results.movies
        const container = document.getElementById("categoryPosts");
        container.innerHTML = "";

        movies.forEach((movie, index) => {
            console.log(index)
            if (index === 3) {
                container.innerHTML += `
                    <div class="ad ad-infeed">
                        <p>Advertisement</p>
                    </div>
                `;
            }

            container.innerHTML += `
                <a href="/movies/${movie.id}/" class="post-card">
                    <img src="${movie.thumbnail}">
                    <div class="content">
                        <h4>${movie.title}</h4>
                        <p>${movie.description.slice(0, 45)}...</p>
                    </div>
                </a>
            `;
        });
    } catch (error) {
        console.error(error.message)
    }
}

fetch_movies()

setInterval(() => {
    fetch_movies()
}, 10000);