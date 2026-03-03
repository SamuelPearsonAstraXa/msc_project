const form = document.getElementById("edit-content-form");


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

document.getElementById("updateBtn").addEventListener("click", function(e){

    e.preventDefault();

    const formData = new FormData();

    formData.append("csrfmiddlewaretoken",
        document.querySelector('[name=csrfmiddlewaretoken]').value
    );

    formData.append("title",
        document.getElementById("postTitle").value
    );

    const thumbnailInput = document.getElementById("thumbnailInput");

    if (thumbnailInput.files.length > 0) {
        formData.append("thumbnail", thumbnailInput.files[0]);
    }

    document.querySelectorAll(".block").forEach((block, index) => {

        const id = block.dataset.id || "";
        const type = block.dataset.type;

        formData.append(`blocks[${index}][id]`, id);
        formData.append(`blocks[${index}][type]`, type);
        formData.append(`blocks[${index}][order]`, index);

        if (type === "text" || type === "quote") {
            formData.append(
                `blocks[${index}][text]`,
                block.querySelector("textarea").value
            );
        }

        if (type === "image") {
            const fileInput = block.querySelector("input[type='file']");
            if (fileInput.files.length > 0) {
                formData.append(
                    `blocks[${index}][image]`,
                    fileInput.files[0]
                );
            }
        }

    });

    fetch(window.location.href, {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {

        if (data.success) {
            window.location = data.success_url;
        } else {
            document.getElementById("response_msg").innerHTML =
                `<p style="color:red">${data.error}</p>`;
        }

    });
});