$(document).ready(function () {
    "use strict";

    $('#menu a, .page-scroll').on('click', function (e) {
        e.preventDefault();

        var $anchor = $(this);

        var offset = $('body').attr('data-offset');

        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - (offset - 1)
        }, 1500);
    });
});