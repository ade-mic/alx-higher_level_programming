/* global $ */
if (typeof $ !== 'undefined') {
  const head = $('DIV#toggle_header');
  head.click(() => {
    $('header').toggleClass('red green');
  });
}
