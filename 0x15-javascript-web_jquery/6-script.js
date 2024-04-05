/* global $ */
if (typeof $ !== 'undefined') {
  const head = $('DIV#update_header');
  head.click(() => {
    $('header').text('New Header!!!');
  });
}
