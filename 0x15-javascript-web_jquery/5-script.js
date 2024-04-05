/* global $ */
if (typeof $ !== 'undefined') {
  const head = $('DIV#add_item');
  head.click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
}
