document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const resultDiv = document.getElementById("result");
  const uploadedImage = document.getElementById("uploaded-image");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    resultDiv.innerHTML = "Classifying...";

    const formData = new FormData(form);
    const response = await fetch("/classify", {
      method: "POST",
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      resultDiv.innerHTML = `Predicted Class: ${data.prediction}`;
      uploadedImage.src = URL.createObjectURL(formData.get("image")); // Display the uploaded image
      uploadedImage.style.display = "block"; // Show the image
    } else {
      resultDiv.innerHTML = "Error classifying the image.";
      uploadedImage.style.display = "none"; // Hide the image if there's an error
    }
  });
});
