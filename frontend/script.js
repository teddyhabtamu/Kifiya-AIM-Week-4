document
  .getElementById("predictionForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    // Show loading spinner
    const resultCard = document.getElementById("result");
    resultCard.classList.add("hidden");
    document.getElementById("predictionValue").innerText = "";
    const loader = document.createElement("div");
    loader.className = "loader";
    resultCard.parentNode.insertBefore(loader, resultCard);

    // Get form data
    const store = document.getElementById("store").value;
    const date = document.getElementById("date").value;
    const promo = document.getElementById("promo").value;

    // Prepare input data
    const inputData = {
      store: parseInt(store),
      date: date,
      promo: parseInt(promo),
    };

    console.log("Sending request to backend:", inputData); // Log the request data

    // Send a POST request to the API
    fetch("http://127.0.0.1:8002/predict/", {
      // Updated URL
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        // Remove loader and display result
        loader.remove();
        document.getElementById(
          "predictionValue"
        ).innerText = `€${data.prediction.toFixed(2)}`;
        resultCard.classList.remove("hidden");
      })
      .catch((error) => {
        console.error("Error:", error);
        loader.remove();
        alert("Error making prediction. Please try again.");
      });
  });
