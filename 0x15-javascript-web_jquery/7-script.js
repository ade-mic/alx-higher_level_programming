/* global $ */
// script that fetches the character name from
// this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
if (typeof $ !== 'undefined') {
  $(function () {
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.get(url, (data, textStatus) => {
      if (textStatus === 'success') {
        const name = data.name;
        $('DIV#character').text(name);
      }
    });
  });
}
