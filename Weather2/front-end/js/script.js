// Simulating data update for the dashboard
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        // Simulate data for the metrics
        document.getElementById('temperature').innerHTML = "<p>Temperature: 22°C</p>";
        document.getElementById('humidity').innerHTML = "<p>Humidity: 58%</p>";
        document.getElementById('wind').innerHTML = "<p>Wind Speed: 14 km/h</p>";
    }, 1000); // Simulate data load with a delay of 1 second
});


// Function to simulate weather data loading
function loadWeatherData() {
    // Simulate data for the metrics
    setTimeout(function() {
        document.getElementById('temperature').innerHTML = "<p>Temperature: 22°C</p>";
        document.getElementById('humidity').innerHTML = "<p>Humidity: 58%</p>";
        document.getElementById('wind').innerHTML = "<p>Wind Speed: 14 km/h</p>";
    }, 1000); // Simulate data load with a delay of 1 second
}