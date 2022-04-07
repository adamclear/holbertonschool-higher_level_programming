$(document).ready(() => {
  jQuery.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', (char) => {
    $('#character').text(char.name);
  });
});