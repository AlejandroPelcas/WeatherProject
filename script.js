// Simple JavaScript to display a welcome message on page load
window.onload = function() {
    // alert('Welcome to my simple website!');
  };

let pushButton = document.querySelectorAll(".button"); 

pushButton.forEach(btn => {
    btn.addEventListener('click', () => {
        alert('You clicked on {btn.textCoentent} button!')
    });
});

fetch('https://api.weather.gov/points/')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse the JSON data from the response
  })
  .then(data => {
    console.log(data); // Log the fetched data
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });

let SingButtonUp = document.getElementById('SignButtonUp')
let SingButtonIn = document.getElementById('SignButtonIn')

SingButtonIn.onclick = function() {
    console.log("Clicked Sign in Button")
}