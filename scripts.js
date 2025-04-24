document.addEventListener("DOMContentLoaded", function() {
    const scrapeButton = document.getElementById("scrape-button");
    const processButton = document.getElementById("process-button");
    const predictButton = document.getElementById("predict-button");
    const resultContainer = document.getElementById("result-container");

    scrapeButton.addEventListener("click", function() {
        fetch("/scrape")
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    resultContainer.innerHTML = "<p>Data scraped successfully!</p>";
                } else {
                    resultContainer.innerHTML = "<p>Error scraping data.</p>";
                }
            })
            .catch(error => {
                console.error("Error:", error);
                resultContainer.innerHTML = "<p>Error occurred while scraping data.</p>";
            });
    });

    processButton.addEventListener("click", function() {
        fetch("/process")
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    resultContainer.innerHTML = "<p>Data processed successfully!</p>";
                } else {
                    resultContainer.innerHTML = "<p>Error processing data.</p>";
                }
            })
            .catch(error => {
                console.error("Error:", error);
                resultContainer.innerHTML = "<p>Error occurred while processing data.</p>";
            });
    });

    predictButton.addEventListener("click", function() {
        fetch("/predict")
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    resultContainer.innerHTML = `<p>Predicted outcomes: ${data.predictions}</p>`;
                } else {
                    resultContainer.innerHTML = "<p>Error predicting outcomes.</p>";
                }
            })
            .catch(error => {
                console.error("Error:", error);
                resultContainer.innerHTML = "<p>Error occurred while predicting outcomes.</p>";
            });
    });
});