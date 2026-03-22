const posts_container = document.getElementById("posts_container");
const movies_container = document.getElementById("movies_container");
const series_container = document.getElementById("series_container");
const facts_container = document.getElementById("facts_container");
const leaks_container = document.getElementById("leaks_container");
const stories_container = document.getElementById("stories_container");
const loader = document.querySelector('.loader');

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
        // posts_container.innerHTML = "";

        // posts.forEach((post, index) => {
        //     // if (index === 3) {
        //     //     posts_container.innerHTML += `
        //     //         <div class="ad ad-infeed">
        //     //             <p>Advertisement</p>
        //     //         </div>
        //     //     `;
        //     // }

        //     if (post.category === 'leaks') {
        //         leaks_container.innerHTML += `
        //             <a href='/content/${post.category}/${post.id}/' class="post-card">
        //                 <img src="${post.thumbnail}" alt="${post.title}">
        //                 <div class="content">
        //                     <h4>${post.title}</h4>
        //                 </div>
        //                 <p class='post-type'>Leak</p>
        //             </a>
        //         `;
        //     } else if (post.category === 'stories') {
        //         stories_container.innerHTML += `
        //             <a href='/content/${post.category}/${post.id}/' class="post-card">
        //                 <img src="${post.thumbnail}" alt="${post.title}">
        //                 <div class="content">
        //                     <h4>${post.title}</h4>
        //                 </div>
        //                 <p class='post-type'>Story</p>
        //             </a>
        //         `;
        //     } else if (post.category === 'movies') {
        //         movies_container.innerHTML += `
        //             <a href='/content/${post.category}/${post.id}/' class="post-card">
        //                 <img src="${post.thumbnail}" alt="${post.title}">
        //                 <div class="content">
        //                     <h4>${post.title}</h4>
        //                 </div>
        //                 <p class='post-type'>Story</p>
        //             </a>
        //         `;
        //     } else if (post.category === 'series') {
        //         series_container.innerHTML += `
        //             <a href='/content/${post.category}/${post.id}/' class="post-card">
        //                 <img src="${post.thumbnail}" alt="${post.title}">
        //                 <div class="content">
        //                     <h4>${post.title}</h4>
        //                 </div>
        //                 <p class='post-type'>Story</p>
        //             </a>
        //         `;
        //     } else {
        //         facts_container.innerHTML += `
        //             <a href='/content/${post.category}/${post.id}/' class="post-card">
        //                 <img src="${post.thumbnail}" alt="${post.title}">
        //                 <div class="content">
        //                     <h4>${post.title}</h4>
        //                 </div>
        //                 <p class='post-type'>Fact</p>
        //             </a>
        //         `;
        //     }

            
        // });
    } catch (error) {
        console.error(error.message)
    }
}

fetch_posts()

document.getElementById("newsletterForm").addEventListener("submit", function(e){

    e.preventDefault();
    loader.style.display = 'inline-block';

    const formData = new FormData();
    formData.append("email", document.getElementById("subscriberEmail").value);
    formData.append("csrfmiddlewaretoken",
        document.querySelector('[name=csrfmiddlewaretoken]').value
    );

    fetch("/newsletter/subscribe/", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        loader.style.display = 'none';
        document.getElementById("newsletterMessage").innerHTML =
            `<p>${data.message}</p>`;
        document.getElementById("subscriberEmail").value = '';
        setTimeout(() => {
            document.getElementById("newsletterMessage").style.display = 'none';
        }, 10000);
    });

});