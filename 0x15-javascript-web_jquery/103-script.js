/* global $ */
$(document).ready(function() {
    $('INPUT#btn_translate').on('click', function() {
        const languageCode = $('INPUT#language_code').val();

        // Fetch translation from the API
        $.getJSON(`https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`, function(data) {
            const translation = data.hello;

            // Display the translation in the #hello div
            $('DIV#hello').text(translation);
        });
    });

    // Listen for Enter key press in the input field
    $('INPUT#language_code').on('keypress', function(e) {
        if (e.key === 'Enter') {
            $('INPUT#btn_translate').click();
        }
    });
});
