const posts_container = document.getElementById("posts_container");

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

            if (post.category === 'leaks') {
                posts_container.innerHTML += `
                    <a href='/content/${post.category}/${post.id}/' class="post-card">
                        <img src="${post.thumbnail}" alt="${post.title}">
                        <div class="content">
                            <h4>${post.title}</h4>
                        </div>
                        <p class='post-type'>Leak</p>
                    </a>
                `;
            } else if (post.category === 'stories') {
                posts_container.innerHTML += `
                    <a href='/content/${post.category}/${post.id}/' class="post-card">
                        <img src="${post.thumbnail}" alt="${post.title}">
                        <div class="content">
                            <h4>${post.title}</h4>
                        </div>
                        <p class='post-type'>Story</p>
                    </a>
                `;
            } else {
                posts_container.innerHTML += `
                    <a href='/content/${post.category}/${post.id}/' class="post-card">
                        <img src="${post.thumbnail}" alt="${post.title}">
                        <div class="content">
                            <h4>${post.title}</h4>
                        </div>
                        <p class='post-type'>Fact</p>
                    </a>
                `;
            }

            
        });
    } catch (error) {
        console.error(error.message)
    }
}

fetch_posts()

// setInterval(() => {
//     fetch_posts()
// }, 10000);