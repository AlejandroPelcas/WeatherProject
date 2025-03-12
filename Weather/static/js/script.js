// Simulating data update for the dashboard
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        // Simulate data for the metrics
        document.getElementById('temperature').innerHTML = "<p>Temperature: 22°C</p>";
        document.getElementById('humidity').innerHTML = "<p>Humidity: 58%</p>";
        document.getElementById('wind').innerHTML = "<p>Wind Speed: 14 km/h</p>";
    }, 1000); // Simulate data load with a delay of 1 second
});

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
            console.debug("We suck")
            console.error('NOOOO fetching weather data:', error);
            alert("Failed to fetch weather data. Please try again later.");
        });
        alert("success")
}

function updateTextBox() {
    const responseBox = document.getElementById('responseBox');
    console.log("Update Text Box")
    if (storedData) {
        responseBox.value = storedData
        console.log("There was an API response")
    } else {
        responseBox.value = "No Text Val yet"
        console.log("No text yet")
    }
}

document.getElementById('UpdateTextBox').addEventListener('click', updateTextBox);

// Add event listener to the update button
document.getElementById('updateButton').addEventListener('click', fetchWeatherData);

// Add event listener to update LLM callback for req
document.getElementById('updateRecommendationButton').addEventListener('click', fetchRecommendation2);

// Fetch data when the page loads (optional)
// document.addEventListener("DOMContentLoaded", fetchWeatherData);
document.getElementById('weatherDataInfo').addEventListener('click', showWeatherData)

// When page is loaded fetch the data
document.addEventListener("DOMContentLoaded", function() {
    console.log("Page is Loaded")
    // Fetch the data 
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
        const textContainer = document.getElementById('textContainer');
        textContainer.innerText = text;  // Insert the text into the div
        storedData = data.response
        })
    })
    .catch(error => {
        console.error('Error fetching the text:', error);
    });
})