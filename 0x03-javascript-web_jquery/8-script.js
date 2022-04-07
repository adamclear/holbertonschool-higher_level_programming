$(document).ready(() => {
  jQuery.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (films) => {
    for (movie of films.results) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    }
  });
});
