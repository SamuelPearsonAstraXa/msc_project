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

async function fetch_actors() {
    try {
        const response = await fetch('/movies/fetch-actors/');
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const results = await response.json();
        const actors = results.actors
        const container = document.getElementById("categoryPosts");
        container.innerHTML = "";

        actors.forEach((actor, index) => {
            console.log(index)
            if (index === 3) {
                container.innerHTML += `
                    <div class="ad ad-infeed">
                        <p>Advertisement</p>
                    </div>
                `;
            }

            container.innerHTML += `
                <a href="/movies/actors/${actor.id}/" class="post-card">
                    <img src="${actor.thumbnail}">
                    <div class="content">
                        <h4>${actor.name}</h4>
                        <p>${actor.bio.slice(0, 45)}...</p>
                    </div>
                </a>
            `;
        });
    } catch (error) {
        console.error(error.message)
    }
}

switch (location.href) {
    case 'http://127.0.0.1:8000/movies/actors/':
        fetch_actors();
        break;
    default:
        fetch_movies();
        break;
}

// setInterval(() => {
//     fetch_movies()
// }, 10000);