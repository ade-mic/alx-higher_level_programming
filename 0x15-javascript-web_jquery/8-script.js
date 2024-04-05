/* global $ */
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(url, function (data) {
    // Extract movue titles
    const titles = data.results.map(movie => `<li>${movie.title}</li>`);
    $('UL#list_movies').html(titles);
  });
});
