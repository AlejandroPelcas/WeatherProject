
// Simulating data update for the dashboard
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        // Simulate data for the metrics
        document.getElementById('temperature').innerHTML = "<p>Temperature: ?°C</p>";
        document.getElementById('humidity').innerHTML = "<p>Humidity: ?%</p>";
        document.getElementById('city').innerHTML = "<p>City: ?</p>";
    }, 100); // Simulate data load with a delay of 1 second
});

function onLoad() {
// Check if geolocation is supported by the browser
if (navigator.geolocation) {
    // Get the user's current position
    navigator.geolocation.getCurrentPosition(function(position) {
        // Success callback: the position object contains the latitude and longitude
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        
        // Log the user's latitude and longitude to the console
        console.log("Latitude: " + latitude);
        console.log("Longitude: " + longitude);

        fetch(`http://127.0.0.1:5000/weather?lat=${latitude}&lon=${longitude}`)
        .then(response => response.json())
        .then(data => {
            console.log("The data inside lat lon fetch", data)
            const temp = data.temperature
            const city = data.city
            const weather_description = data.weather_description
            console.log("City = ", city)
            const humidity = data.humidity
            fetch(`http://127.0.0.1:5000/recommendation_data?temperature=${temp}&city=${city}&humidity=${humidity}&weather_description=${weather_description}`)
            .then(response => response.json())
            .then(data => {
            // Get the text from the API response
            const text = data;
            console.log("This is the data response text" ,data.response)
            // Get the div container by ID and populate it with the text
            document.getElementById('temperature').innerHTML =  `<p>Temperature: ${temp}°F</p>`;
            document.getElementById('humidity').innerHTML = `<p> Humidity: ${humidity}%`;
            document.getElementById('city').innerHTML = `<p> City: ${city}</p>`;
            storedData = data.response
            })
        })
        .catch(error => {
            console.error('Error fetching the text:', error);
        });
        
        // You can now use the latitude and longitude for further operations (e.g., pass them to an API)
    }, function(error) {
        // Error callback: handles any error that occurs
        console.error("Error getting location: ", error);
    });
    } else {
        // Geolocation is not supported by the browser
        console.log("Geolocation is not supported by this browser.");
    }
    console.log("Page is Loaded")
}

function autoResize() {
    const textarea = document.getElementById('dynamic-textbox');
    textarea.style.height = 'auto'; // Reset height to auto before calculating
    textarea.style.height = textarea.scrollHeight + 'px'; //
    textarea.value = storedData
}

function updateTextBox() {
    console.log("Update Text Box")
    if (storedData) {
        setTimeout(() => {
            autoResize();
                  }, 1000); // Small delay to allow DOM update
        
        console.log("There was an API response")
    } else {
        textarea.value = "Value hasn't been fetched yet. Please try again!"
        console.log("No text yet")
    }
}

document.getElementById('UpdateTextBox').addEventListener('click', updateTextBox);
document.addEventListener("DOMContentLoaded", onLoad)