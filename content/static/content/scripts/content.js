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

async function fetch_posts(post_type) {
    try {
        const response = await fetch(`/content/fetch_${post_type}/`);
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
                <a href='/content/${post.category}/${post.id}/' class="post-card">
                    <img src="${post.thumbnail}" alt="${post.title}">
                    <div class="content">
                        <h4>${post.title}</h4>
                    </div>
                </a>
            `;
        });
    } catch (error) {
        console.error(error.message)
    }
}

async function fetch_all_posts() {
    try {
        const response = await fetch(`/content/fetch_posts/`);
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
                <a href='/content/${post.category}/${post.id}/' class="post-card">
                    <img src="${post.thumbnail}" alt="${post.title}">
                    <div class="content">
                        <h4>${post.title}</h4>
                    </div>
                </a>
            `;
        });
    } catch (error) {
        console.error(error.message)
    }
}

switch (location.href) {
    case  'http://127.0.0.1:8000/content/facts/':
        fetch_posts('facts')
        break;
    case 'http://127.0.0.1:8000/content/leaks/':
        fetch_posts('leaks')
        break;
    case 'http://127.0.0.1:8000/content/stories/':
        fetch_posts('stories')
        break;
    default:
        fetch_all_posts()
        break;
}

// setInterval(() => {
//     fetch_posts()
// }, 10000);