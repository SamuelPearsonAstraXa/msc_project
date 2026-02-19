const posts = [
    {
        title: "Marvel Announces New Superhero Film",
        image: "core/static/core/scripts/image.jpg",
        // image: "../images/image.jpg",
        description: "Marvel Studios surprises fans with a brand new hero entering the MCU."
    },
    {
        title: "Exclusive Leak From Upcoming Sci-Fi Movie",
        image: "core/static/core/scripts/image.jpg",
        // image: "../images/image.jpg",
        description: "Set photos reveal shocking twist scenes ahead of release."
    },
    {
        title: "Did You Know? Hidden Details in Classic Films",
        image: "core/static/core/scripts/image.jpg",
        // image: "../images/image.jpg",
        description: "These small movie details changed cinema history."
    },
    {
        title: "Actor Spotlight: Rising Star of 2026",
        image: "core/static/core/scripts/image.jpg",
        // image: "../images/image.jpg",
        description: "This breakout actor is dominating the big screen."
    },
    {
        title: "Actor Spotlight: Rising Star of 2026",
        image: "core/static/core/scripts/image.jpg",
        // image: "../images/image.jpg",
        description: "This breakout actor is dominating the big screen."
    },
    {
        title: "Actor Spotlight: Rising Star of 2026",
        image: "core/static/core/scripts/image.jpg",
        // image: "../images/image.jpg",
        description: "This breakout actor is dominating the big screen."
    },
];

const posts_container = document.getElementById("posts_container");

// function display_posts(postArray) {
//     posts_container.innerHTML = "";

//     postArray.forEach((post, index) => {

//         // Insert ad after 3rd post
//         if (index === 3) {
//             posts_container.innerHTML += `
//                 <div class="ad ad-infeed">
//                     <p>Advertisement</p>
//                 </div>
//             `;
//         }

//         posts_container.innerHTML += `
//             <a href='' class="post-card">
//                 <img src="${post.image}" alt="${post.title}">
//                 <div class="content">
//                     <h4>${post.title}</h4>
//                     <p>${post.description}</p>
//                 </div>
//             </a>
//         `;
//     });
// }


// display_posts(posts);

const faders = document.querySelectorAll(".post-card");

window.addEventListener("scroll", () => {
    faders.forEach(card => {
        const rect = card.getBoundingClientRect();
        if (rect.top < window.innerHeight - 50) {
            card.classList.add("active");
        }
    });
});

async function fetch_posts() {
    try {
        const response = await fetch('/fetch_posts/');
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const results = await response.json();
        const posts = results.posts
        // const container = document.getElementById("categoryPosts");
        posts_container.innerHTML = "";

        posts.forEach((post, index) => {
            // Insert ad after 3rd post
            if (index === 3) {
                posts_container.innerHTML += `
                    <div class="ad ad-infeed">
                        <p>Advertisement</p>
                    </div>
                `;
            }

            posts_container.innerHTML += `
                <a href='/content/${post.post_type}/${post.id}/' class="post-card">
                    <img src="${post.thumbnail}" alt="${post.title}">
                    <div class="content">
                        <h4>${post.title}</h4>
                        <p>${post.content.slice(0,30)}...</p>
                    </div>
                </a>
            `;
        });
    } catch (error) {
        console.error(error.message)
    }
}

fetch_posts()

// setInterval(() => {
//     fetch_posts()
// }, 10000);