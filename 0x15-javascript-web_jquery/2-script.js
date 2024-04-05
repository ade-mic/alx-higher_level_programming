/* global $ */
if (typeof $ !== 'undefined') {
  const head = $('DIV#red_header');
  head.click(() => {
    $('header').css('color', '#FF0000');
  });
}
