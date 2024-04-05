/* global $ */
if (typeof $ !== 'undefined') {
  const head = $('DIV#red_header');
  head.click(() => {
    $('header').addClass('red');
  });
}
