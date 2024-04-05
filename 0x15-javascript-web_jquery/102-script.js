/* global $ */
$(document).ready(() => {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(() => {
    const lang_var = $('INPUT#language_code').val();
    // fetch API
    $.getJSON(`${url}?lang=${lang_var}`, (data) => {
      const translation = data.hello;
      $('DIV#hello').text(translation);
    });
  });
});
