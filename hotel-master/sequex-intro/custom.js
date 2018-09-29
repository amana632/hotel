jQuery("#main-left-overlay").hover(function(){
    jQuery("#main-icon").attr("src", "princess-leia.png");
    jQuery('#main-title span').text('LIGHT VERSION');
    jQuery('#main-title').css('left', '75%');
    jQuery('#main-right-overlay').toggleClass("disabled");
    }, function(){
    jQuery("#main-icon").attr("src", "luke-skywalker.png");
    jQuery('#main-title span').text('CHOOSE YOUR SIDE');
    jQuery('#main-title').css('left', '50%');
    jQuery('#main-right-overlay').toggleClass("disabled");
});
jQuery("#main-right-overlay").hover(function(){
    jQuery("#main-icon").attr("src", "darth-vader.png");
    jQuery('#main-title span').text('DARK VERSION');
    jQuery('#main-title').css('left', '25%');
    jQuery('#main-left-overlay').toggleClass("disabled");
    }, function(){
    jQuery("#main-icon").attr("src", "luke-skywalker.png");
    jQuery('#main-title span').text('CHOOSE YOUR SIDE');
    jQuery('#main-title').css('left', '50%');
    jQuery('#main-left-overlay').toggleClass("disabled");
});
jQuery(window).on('load', function () {
    jQuery('#main-right-loading').hide();
    jQuery('#main-left-loading').hide();
});