// Simulating data update for the dashboard
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        // Simulate data for the metrics
        document.getElementById('temperature').innerHTML = "<p>Temperature: ?°C</p>";
        document.getElementById('humidity').innerHTML = "<p>Humidity: ?%</p>";
        document.getElementById('wind').innerHTML = "<p>Wind Speed: ? km/h</p>";
    }, 100); // Simulate data load with a delay of 1 second
});

function onLoad() {
    console.log("Page is Loaded")
    fetch('http://127.0.0.1:5000/weather')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        const temp = data.temperature
        const city = data.city
        const humidity = data.humidity
        fetch(`http://127.0.0.1:5000/recommendation_data?temperature=${temp}&city=${city}&humidity=${humidity}`)
        .then(response => response.json())
        .then(data => {
        // Get the text from the API response
        const text = data;
        console.log("This is the data response text" ,data.response)
        // Get the div container by ID and populate it with the text

        storedData = data.response
        })
    })
    .catch(error => {
        console.error('Error fetching the text:', error);
    });
}

async function showWeatherData() {
    fetch('http://127.0.0.1:5000/info')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
    
}

async function fetchRecommendation2() {
    const weather_data = (await fetch('http://127.0.0.1:5000/weather'));
    const recommendation_response = await fetch('http://127.0.0.1:5000/recommendation');
    // alert(weather_data)
    console.log(weather_data.json().city)
    fetch('http://127.0.0.1:5000/recommendation')
        .then(response => response.json())
        .then(data => {
            alert("Did it work?")
            console.log('Assistant response:', data["response"]);
            alert(data["response"])
        })
        .catch(error => {
            console.error(' error fetching REC data:', error);
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
            alert("Failed to fetch weather data. Please try again later.");
        });
        alert("success")
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
document.getElementById('updateButton').addEventListener('click', fetchWeatherData);
document.getElementById('updateRecommendationButton').addEventListener('click', fetchRecommendation2);
document.getElementById('weatherDataInfo').addEventListener('click', showWeatherData)
document.addEventListener("DOMContentLoaded", onLoad)