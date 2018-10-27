/*!
 * jQuery Cookie Plugin v1.4.1
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2006, 2014 Klaus Hartl
 * Released under the MIT license
 */

!function(a){"function"==typeof define&&define.amd?define(["jquery"],a):"object"==typeof exports?a(require("jquery")):a(jQuery)}(function(a){function c(a){return h.raw?a:encodeURIComponent(a)}function d(a){return h.raw?a:decodeURIComponent(a)}function e(a){return c(h.json?JSON.stringify(a):String(a))}function f(a){0===a.indexOf('"')&&(a=a.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\"));try{return a=decodeURIComponent(a.replace(b," ")),h.json?JSON.parse(a):a}catch(c){}}function g(b,c){var d=h.raw?b:f(b);return a.isFunction(c)?c(d):d}var b=/\+/g,h=a.cookie=function(b,f,i){if(arguments.length>1&&!a.isFunction(f)){if(i=a.extend({},h.defaults,i),"number"==typeof i.expires){var j=i.expires,k=i.expires=new Date;k.setTime(+k+864e5*j)}return document.cookie=[c(b),"=",e(f),i.expires?"; expires="+i.expires.toUTCString():"",i.path?"; path="+i.path:"",i.domain?"; domain="+i.domain:"",i.secure?"; secure":""].join("")}for(var l=b?void 0:{},m=document.cookie?document.cookie.split("; "):[],n=0,o=m.length;o>n;n++){var p=m[n].split("="),q=d(p.shift()),r=p.join("=");if(b&&b===q){l=g(r,f);break}b||void 0===(r=g(r))||(l[q]=r)}return l};h.defaults={},a.removeCookie=function(b,c){return void 0===a.cookie(b)?!1:(a.cookie(b,"",a.extend({},c,{expires:-1})),!a.cookie(b))}});


/* Switch Style */

jQuery(document).ready(function($) {

    /* Left Panel */
    
    style_switcher = $('.style-customizer'),
    panelWidth = style_switcher.outerWidth(true);
    $('.style-customizer .opener').on("click", function(){
        var $this = $(this);
        if ($(".style-customizer.closed").length>0) { 
                style_switcher.animate({"left" : "0px"});
                $(".style-customizer.closed").removeClass("closed");
                $(".style-customizer").addClass("opened");
        } else {
                $(".style-customizer.opened").removeClass("opened");
                $(".style-customizer").addClass("closed");
                style_switcher.animate({"left" : '-' + panelWidth});
        }
        return false;
    });
		
		
    /* Resume from last selected style */
    var link = $('link[data-style="styles"]');
        //link_no_cookie = $('link[data-style="styles-no-cookie"]');
 
    var tp_stylesheet = $.cookie('tp_stylesheet'),
        layout_mode = $.cookie('layout_mode'),
        header = $.cookie('header'),
        background = $.cookie('background');

    $(".style-customizer .selected").removeClass("selected");
    if (!($.cookie('tp_stylesheet'))) {
        $.cookie('tp_stylesheet', 'skin-default', 30);
        tp_stylesheet = $.cookie('tp_stylesheet');
        $('.style-customizer .styleChange li[data-style="'+tp_stylesheet+'"]').addClass("selected");
    } else {
        if (link.length>0) {
            link.attr('href','assets/css/color/' + tp_stylesheet + '.css');
            $('.style-customizer .styleChange li[data-style="'+tp_stylesheet+'"]').addClass("selected");			 	
        };
    };	
    $("body").addClass(header); 
    $('.style-customizer .headerChange li[data-style="'+header+'"]').addClass("selected");
    if ($("body").hasClass("header-0")){
        document.getElementById("logo_img").src="assets/images/logo/logo.png";
    } else {
        document.getElementById("logo_img").src="assets/images/logo/logo-white.png";
    }
    
    if (!($.cookie('layout_mode'))) {
        $.cookie('layout_mode', 'wide-layout', 30);
        layout_mode = $.cookie('layout_mode');
        $("body").addClass(layout_mode);
        $('.style-customizer .layoutstyle li[data-style="'+layout_mode+'"]').addClass("selected");
    } else {
        if (layout_mode=="boxed-layout") {
            $("body").addClass(layout_mode);
            $("body").removeClass("wide-layout");
            $('.style-customizer .layoutstyle li[data-style="boxed-layout"]').addClass("selected");
            $('.style-customizer .layoutstyle li[data-style="wide-layout"]').removeClass("selected");
        } else { 
            $("body").addClass(layout_mode);
            $("body").removeClass("boxed-layout ");
            $('.style-customizer .layoutstyle li[data-style="boxed-layout"]').removeClass("selected");
            $('.style-customizer .layoutstyle li[data-style="wide-layout"]').addClass("selected");
        };
    }; 
    
    if ((layout_mode =="boxed-layout") && $.cookie('background')) {
        $('.style-customizer .backgroundChange li[data-style="'+background+'"]').addClass("selected");
        $("body").removeClass("main-bg-1 main-bg-2 main-bg-3 main-bg-4 main-bg-5 main-bg-6 main-bg-7 main-bg-8");
        $("body").addClass(background); 
    } else if (layout_mode =="boxed-layout") {
        $("body").removeClass("main-bg-1 main-bg-2 main-bg-3 main-bg-4 main-bg-5 main-bg-6 main-bg-7 main-bg-8");
         $('.style-customizer .backgroundChange li.selected').removeClass("selected");
        //$('.style-customizer .backgroundChange li[data-style=""]').addClass("selected");
    } else {
        $('.style-customizer .backgroundChange li.selected').removeClass("selected");
        $("body").removeClass("main-bg-1 main-bg-2 main-bg-3 main-bg-4 main-bg-5 main-bg-6 main-bg-7 main-bg-8");
    };
    
    
    

     /* Color Changer */
    $('.style-customizer .styleChange li').on('click',function(){
        if (link.length>0) {
            var $this = $(this),
                tp_stylesheet = $this.data('style');
                
            $(".style-customizer .styleChange .selected").removeClass("selected");
            $this.addClass("selected");
            link.attr('href', 'assets/css/color/' + tp_stylesheet + '.css');
            $.cookie('tp_stylesheet', tp_stylesheet, 30);
        } else {
            var $this = $(this),
                tp_stylesheet_no_cookie = $this.data('style');
            
            $(".style-customizer .styleChange .selected").removeClass("selected");
            $this.addClass("selected");
            //link_no_cookie.attr('href', 'assets/css/color/' + tp_stylesheet_no_cookie + '.css');
        };
    });
    
    
    /* Header Changer  */
    $('.style-customizer .headerChange li').on('click',function(){
        var $this = $(this),
        header = $this.data('style');
        $(".style-customizer .headerChange .selected").removeClass("selected");
        $this.addClass("selected");
        $("body").removeClass("header-0 header-1 header-2");
        $("body").addClass(header);
        $.cookie('header', header, 30);

        if ($("body").hasClass("header-0")){
                document.getElementById("logo_img").src="assets/images/logo/logo.png";
        } else {
            document.getElementById("logo_img").src="assets/images/logo/logo-white.png";
        }


    });


    /* layout Change  */
    $('.style-customizer .layoutstyle li').on('click',function(){
        var $this = $(this),
        layout = $this.data('style');
        $("body").removeClass("wide-layout boxed-layout");
        $("body").addClass(layout);
        $('.style-customizer .layoutstyle .selected').removeClass("selected");
        $this.addClass("selected");
        $.cookie('layout_mode', layout, 30);
        $(window).trigger('resize');
    });
    
    /* Background Change  */
    $('.style-customizer .backgroundChange li').on('click',function(){
        var $this = $(this),
            background = $this.data('style');
        $(".style-customizer .backgroundChange .selected").removeClass("selected");
        $this.addClass("selected");
        $("body").removeClass("wide-layout main-bg-1 main-bg-2 main-bg-3 main-bg-4 main-bg-5 main-bg-6 main-bg-7 main-bg-8");

        $("body").addClass(background);
        $("body").addClass("boxed-layout");
        $('.style-customizer .layoutstyle li[data-style="boxed-layout"]').addClass("selected");
        $('.style-customizer .layoutstyle li[data-style="wide-layout"]').removeClass("selected");
        
        $.cookie('background', background, 30);
        $.cookie('customizer_mode', 'boxed-layout', 30);
        $(window).trigger('resize');
    });
    

		
    /* Reset all customize  */
    $('.style-customizer .resetAll li a.button-reset').on('click',function() { 
        $.cookie('layout_mode', 'wide-layout', 30);
        $("body").addClass("wide-layout");
        $("body").removeClass("boxed-layout");
        $('.style-customizer .layoutstyle .selected').removeClass("selected");
        $('.style-customizer .layoutstyle li[data-style="wide-layout"]').addClass("selected");
        
        $.cookie('tp_stylesheet', 'skin-default', 30);
        var tp_stylesheet = 'skin-default';
        $('.style-customizer .styleChange li.selected').removeClass("selected");
        $('.style-customizer .styleChange li[data-style="'+tp_stylesheet+'"]').addClass("selected");
        link.attr('href', 'css/color/' + tp_stylesheet + '.css');
        
        $.cookie('header', 'header-0', 30);
        $("body").removeClass("header-0 header-1 header-2");
        $("body").addClass(header);
        $(".style-customizer .headerChange .selected").removeClass("selected");
        $('.style-customizer .headerChange li[data-style="'+header+'"]').addClass("selected");
        document.getElementById("logo_img").src="assets/images/logo/logo.png";
        
       	$.cookie('background', '', 30);
	$("body").removeClass("main-bg-1 main-bg-2 main-bg-3 main-bg-4 main-bg-5 main-bg-6 main-bg-7 main-bg-8");
	$(".style-customizer .backgroundChange .selected").removeClass("selected");
        
    });

});
