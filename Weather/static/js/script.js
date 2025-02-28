// Simulating data update for the dashboard
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        // Simulate data for the metrics
        document.getElementById('temperature').innerHTML = "<p>Temperature: 22°C</p>";
        document.getElementById('humidity').innerHTML = "<p>Humidity: 58%</p>";
        document.getElementById('wind').innerHTML = "<p>Wind Speed: 14 km/h</p>";
    }, 1000); // Simulate data load with a delay of 1 second
});

function fetchRecommendation() {
    console.log("You pushed the right button")
    console.debug("TRYING TO FETCH RECS")
    alert("Inside the fetch")
    fetch('http://127.0.0.1:5000/recommendation')
        .then(response => response.json())
        .then(data => {
            alert("Did it work?")
            console.log('Assistant response:', data["response"]);
            alert(data["response"])
        })
        .catch(error => {
            console.error('NOOOO fetching REC data:', error);
            alert("Failed to REC  data. Please try again later.");
        });
}


// Function to fetch weather data from Flask backend
function fetchWeatherData() {
    console.log("You pushed the left button")
    console.debug("Trying to fetch weather")

    fetch('http://127.0.0.1:5000/weather')  // URL of your Flask API endpoint
        .then(response => response.json())
        .then(data => {
            // Update the UI with the fetched data
            // Get all the keys
            const keys = Object.keys(data);

            // Print the keys
            console.debug(keys);
            document.getElementById('temperature').innerHTML = `<p>Temperature: ${data["temperature"]}°F</p>`;
            document.getElementById('city').innerHTML = `<p>City: ${data["city"]}</p>`;

        })
        .catch(error => {
            console.debug("We suck")
            console.error('NOOOO fetching weather data:', error);
            alert("Failed to fetch weather data. Please try again later.");
        });
        alert("success")
}

// Add event listener to the update button
document.getElementById('updateButton').addEventListener('click', fetchWeatherData);

// THIS IS THE CORRECT FILE DON'T DELETE 
// Add event listener to update LLM callback for req
document.getElementById('updateRecommendationButton').addEventListener('click', fetchRecommendation);
// Fetch data when the page loads (optional)
// document.addEventListener("DOMContentLoaded", fetchWeatherData);