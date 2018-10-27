

$(function () {
    "use strict";

    $(window).on('load', function (e) {
        //$('body').addClass('loaded');
        $('.loader').fadeOut("slow");;
    });

    loadscroler();
    
    

});


/*Function for Add Go to up arrow Start */
function loadscroler() {
    $('body').prepend('<a href="#" class="bottom-top"><i class="icofont icofont-bubble-up"></i></a>');
    var amountScrolled = 300;
    $(window).on('scroll', function () {
        if ($(window).scrollTop() > amountScrolled) {
            $('a.bottom-top').fadeIn('slow');
        } else {
            $('a.bottom-top').fadeOut('slow');
        }
    });
    $('a.bottom-top').on('click', function () {
        $('html, body').animate({
            scrollTop: 0
        }, 700);
        return false;
    });
}
/*Function for Add Go to up arrow End */

