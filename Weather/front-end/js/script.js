// Simulating data update for the dashboard
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        // Simulate data for the metrics
        document.getElementById('temperature').innerHTML = "<p>Temperature: 22°C</p>";
        document.getElementById('humidity').innerHTML = "<p>Humidity: 58%</p>";
        document.getElementById('wind').innerHTML = "<p>Wind Speed: 14 km/h</p>";
    }, 1000); // Simulate data load with a delay of 1 second
});


// Function to fetch weather data from Flask backend
function fetchWeatherData() {
    fetch('http://127.0.0.1:5000/weather')  // URL of your Flask API endpoint
        .then(response => response.json())
        .then(data => {
            // Update the UI with the fetched data
            document.getElementById('temperature').innerHTML = `<p>Temperature: ${response.main.temp}</p>`;
            document.getElementById('city').innerHTML = `<p>Humidity: ${response.name}</p>`;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            alert("Failed to fetch weather data. Please try again later.");
        });
}

// Add event listener to the update button
document.getElementById('updateButton').addEventListener('click', fetchWeatherData);

// Fetch data when the page loads (optional)
// document.addEventListener("DOMContentLoaded", fetchWeatherData);