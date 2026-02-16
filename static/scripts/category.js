const allPosts = [
    { category: "news", title: "Major Studio Announces Sequel", image: "../images/image.jpg", description: "Breaking movie news update." },
    { category: "leaks", title: "Leaked Scene Revealed", image: "../images/image.jpg", description: "Confidential set leak." },
    { category: "actors", title: "Rising Actor Interview", image: "../images/image.jpg", description: "Exclusive actor spotlight." },
    { category: "celebrities", title: "Celebrity Wedding Rumors", image: "../images/image.jpg", description: "Hollywood buzz." },
    { category: "celebrities", title: "Celebrity Wedding Rumors", image: "../images/image.jpg", description: "Hollywood buzz." },
    { category: "didyouknow", title: "Hidden Detail in Classic Film", image: "../images/image.jpg", description: "Trivia fans love." },
    { category: "series", title: "New Netflix Series Announced", image: "../images/image.jpg", description: "Streaming platform reveals new hit series." },
    { category: "movies", title: "Blockbuster Movie Trailer Drops", image: "../images/image.jpg", description: "Fans excited for upcoming release." },
    { category: "movies", title: "Blockbuster Movie Trailer Drops", image: "../images/image.jpg", description: "Fans excited for upcoming release." },
    { category: "movies", title: "Blockbuster Movie Trailer Drops", image: "../images/image.jpg", description: "Fans excited for upcoming release." },
    { category: "movies", title: "Blockbuster Movie Trailer Drops", image: "../images/image.jpg", description: "Fans excited for upcoming release." },
    { category: "movies", title: "Blockbuster Movie Trailer Drops", image: "../images/image.jpg", description: "Fans excited for upcoming release." },
    { category: "movies", title: "Blockbuster Movie Trailer Drops", image: "../images/image.jpg", description: "Fans excited for upcoming release." },
    { category: "movies", title: "Blockbuster Movie Trailer Drops", image: "../images/image.jpg", description: "Fans excited for upcoming release." },
    { category: "movies", title: "Blockbuster Movie Trailer Drops", image: "../images/image.jpg", description: "Fans excited for upcoming release." },
    { category: "behind", title: "Behind The Scenes Secrets", image: "../images/image.jpg", description: "Hidden filming stories revealed." },
    { category: "reviews", title: "Movie Review: 9/10 Rating", image: "../images/image.jpg", description: "Critical analysis and breakdown." },
    { category: "reviews", title: "Movie Review: 9/10 Rating", image: "../images/image.jpg", description: "Critical analysis and breakdown." },
];


function loadCategory(categoryName) {

    const container = document.getElementById("categoryPosts");
    container.innerHTML = "";

    const filtered = allPosts.filter(post => post.category === categoryName);

    filtered.forEach((post, index) => {

        if (index === 3) {
            container.innerHTML += `
                <div class="ad ad-infeed">
                    <p>Advertisement</p>
                </div>
            `;
        }
        if (index === 15) {
            container.innerHTML += `
                <div class="ad ad-infeed">
                    <p>Advertisement</p>
                </div>
            `;
        }

        container.innerHTML += `
            <div class="post-card">
                <img src="${post.image}">
                <div class="content">
                    <h4>${post.title}</h4>
                    <p>${post.description}</p>
                </div>
            </div>
        `;
    });
}
