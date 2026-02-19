async function fetch_series() {
    try {
        const response = await fetch('/series/fetch-data');
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const results = await response.json();
        const series = results.series
        const container = document.getElementById("categoryPosts");
        container.innerHTML = "";

        series.forEach((series, index) => {
            console.log(index)
            if (index === 3) {
                container.innerHTML += `
                    <div class="ad ad-infeed">
                        <p>Advertisement</p>
                    </div>
                `;
            }

            container.innerHTML += `
                <a href="/series/${series.id}/" class="post-card">
                    <img src="${series.thumbnail}">
                    <div class="content">
                        <h4>${series.title}</h4>
                        <p>${series.description.slice(0,45)}...</p>
                    </div>
                </a>
            `;
        });
    } catch (error) {
        console.error(error.message)
    }
}

fetch_series()

setInterval(() => {
    fetch_series()
}, 10000);