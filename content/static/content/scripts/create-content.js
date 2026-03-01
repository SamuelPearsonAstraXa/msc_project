let blocksContainer = document.getElementById("blocksContainer");
const create_content_form = document.getElementById("create-content-form");

function addTextBlock() { createBlock("text"); }
function addImageBlock() { createBlock("image"); }
function addQuoteBlock() { createBlock("quote"); }

createBlock("text");

function createBlock(type) {

    const block = document.createElement("div");
    block.classList.add("block");
    block.dataset.type = type;

    let contentHTML = "";

    if (type === "text") {
        contentHTML = `
        <h5>Paragraph</h5>
        <textarea placeholder="Write paragraph..."></textarea>
        `;
    }

    if (type === "image") {
        contentHTML = `
        <h5>Image</h5>
        <input type="file" accept="image/*">
        `;
    }

    if (type === "quote") {
        contentHTML = `
        <h5>Quote</h5>
        <textarea placeholder="Write quote..."></textarea>
        `;
    }

    block.innerHTML = `
        <div class="block-controls">
            <button type="button" onclick="moveUp(this)"><i class="fas fa-arrow-up"></i></button>
            <button type="button" onclick="moveDown(this)"><i class="fas fa-arrow-down"></i></button>
            <button type="button" onclick="removeBlock(this)"><i class="fas fa-xmark"></i></button>
        </div>
        ${contentHTML}
    `;

    blocksContainer.appendChild(block);
}

function removeBlock(btn) {
    btn.closest(".block").remove();
}

function moveUp(btn) {
    const block = btn.closest(".block");
    const prev = block.previousElementSibling;
    if (prev) blocksContainer.insertBefore(block, prev);
}

function moveDown(btn) {
    const block = btn.closest(".block");
    const next = block.nextElementSibling;
    if (next) blocksContainer.insertBefore(next, block);
}


document.getElementById("publishBtn").addEventListener("click", function (e) {

    e.preventDefault();

    const formData = new FormData();

    // Basic fields
    formData.append("title", document.getElementById("postTitle").value);
    formData.append("category", document.getElementById("postCategory").value);

    const thumbnail = document.getElementById("postThumbnail");
    if(thumbnail.files.length > 0){
        formData.append("thumbnail", thumbnail.files[0]);
    }

    

    // CSRF token
    formData.append("csrfmiddlewaretoken",
        document.querySelector('[name=csrfmiddlewaretoken]').value
    );

    document.querySelectorAll(".block").forEach((block, index) => {

        const type = block.dataset.type;

        formData.append(`blocks[${index}][type]`, type);
        formData.append(`blocks[${index}][order]`, index);

        if (type === "text" || type === "quote") {
            const text = block.querySelector("textarea").value;
            formData.append(`blocks[${index}][text]`, text);
        }

        if (type === "image") {
            const fileInput = block.querySelector("input[type='file']");
            if (fileInput.files.length > 0) {
                formData.append(`blocks[${index}][image]`, fileInput.files[0]);
            }
        }
    });

    fetch(create_content_form.action, {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {

        if (data.success) {
            document.getElementById("response_msg").innerHTML =
                `<p style='color:green;'>Post uploaded successfully.</p>`;

            setTimeout(() => {
                window.location = data.success_url;
            }, 1500);
        } else {
            document.getElementById("response_msg").innerHTML =
                `<p style='color:red;'>${data.error}</p>`;
        }

    })
    .catch(error => {
        console.error(error);
        document.getElementById("response_msg").innerHTML =
            `<p style='color:red;'>Upload failed.</p>`;
    });
});