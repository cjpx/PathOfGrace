// instantly update the profile picture preview after selecting a file
document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.getElementById("id_image");
    const profileImage = document.querySelector(".profile-image");

    fileInput.addEventListener("change", function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                profileImage.src = e.target.result; // Update image preview
            };
            reader.readAsDataURL(file);
        }
    });
});