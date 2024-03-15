// Function to set a cookie
function setCookie(name, value, days) {
  var expires = "";
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days*24*60*60*1000));
    expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

// Function to get a cookie
function getCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for(var i=0;i < ca.length;i++) {
    var c = ca[i];
    while (c.charAt(0)==' ') c = c.substring(1,c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
  }
  return null;
}

// Get the dark mode toggle element
var darkModeToggle = document.getElementById('darkModeToggle');

// Check the cookie when the page loads
document.body.classList.toggle('dark-mode', getCookie('darkMode') === 'true');
darkModeToggle.checked = getCookie('darkMode') === 'true';

// Add the event listener to the toggle
darkModeToggle.addEventListener('change', function(event) {
  document.body.classList.toggle('dark-mode', event.target.checked);
  setCookie('darkMode', event.target.checked, 30); // Store the state in a cookie
});