/* global $ */
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.getJSON(url, function (data) {
    // Extract movue titles
    const hello = data.hello;
    $('DIV#hello').text(hello);
  });
});
