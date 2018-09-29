if($(window).width()>750){$('#body').each(function(){'use strict';var link=$(`<div class="option">
							<div class="option-switcher ">
	    					<div class="option-switcher-btn icon-option"><i class="fa fa-gear"></i></div>
								<div class="themes-dropdown">
									<div class="dropdown">
										<a class="btn dropdown-toggle" href="#" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Premium Themes
											<span class="badge badge-warning">categories</span>
										</a>
										<div class="dropdown-menu" id="ajaxContent" aria-labelledby="dropdownMenuLink"></div>
									</div>
								</div>
								<div class="option-swticher-header">
									<div class="option-switcher-heading">Theme Option</div>
								</div>
								<div class="option-swticher-body">
									<span class="subtitle">Color Options</span>
									<ul class="list-unstyled color-options">
										<li class="theme-default theme-active" data-color="default"></li>
										<li class="theme-color1" data-color="color-option1"></li>
										<li class="theme-color2" data-color="color-option2"></li>
										<li class="theme-color3" data-color="color-option3"></li>
										<li class="theme-color4" data-color="color-option4"></li>
									</ul>

									<span class="subtitle">Layout Options</span>
									<div class="no-col-space layoutStyle">
										<a href="javascript:void(0);" class="btn-u active-switcher-btn wide-layout-btn">Wide</a>
										<a href="javascript:void(0);" class="btn-u boxed-layout-btn">Boxed</a>
									</div>
									<div class="bg-patern">
										<h3>Background pattern</h3>
										<ul class="list-unstyled">
										<li class="pattern-default pattern-active"></li>
										<li class="pattern1"></li>
										<li class="pattern2"></li>
										<li class="pattern3"></li>
										<li class="pattern4"></li>
										</ul>
									</div>

									<span class="subtitle">Header style</span>
									<div class="no-col-space header-opns">
										<a href="javascript:void(0);" class="btn-u fixed-header">Fixed</a>
										<a href="javascript:void(0);" class="btn-u static-header">Static</a>
									</div>

									<a href="https://goo.gl/DPjZnJ" class="btn-purchase"><i class="fa fa-shopping-cart"></i> Buy This Theme</a>

								</div>
							</div>
						</div>`);$('#body').prepend(link);});$(window).on('load',function(){'use strict';var url='http://themes.iamabdus.com/options/data.json';var dataformat={format:'json'};function getContent(data){var htmlString='';var promo='';$.each(data,function(key,value){$.each(value.themes,function(k,val){htmlString+='<a class="dropdown-item" href="'+val.link+'" target="_blank">'+val.title+' <span class="badge badge-category">'+val.category+'</span>';htmlString+='<div class="project-promo">';htmlString+='<img class="img-full" src="'+val.thumbnail+'" alt="project">';htmlString+='</div>';htmlString+='</a>';});$.each(value.advertisement,function(k,v){promo+='<a href="'+v.link+'">';promo+='<img class="card-img" src="'+v.image+'" alt="'+v.title+'">';promo+='</a>';});});$('#ajaxContent').append(htmlString);$('#adv').append(promo);}
$.getJSON(url,dataformat,getContent);});}
var panel=jQuery('.option-switcher');$('.option-switcher-btn').on('click',function(){'use strict';$(this).toggleClass('cross');jQuery('.option-switcher').toggleClass('option-visible');});jQuery('.color-options li').click(function(){'use strict';var color=jQuery(this).attr('data-color');var data_logo=jQuery(this).attr('data-logo');setColor(color,data_logo);jQuery('.color-options li').removeClass('theme-active');jQuery(this).addClass('theme-active');});var setColor=function(color){'use strict';jQuery('#option_color').attr('href','css/'+color+'.css');}
var boxed=jQuery('.boxed-layout-btn');var wide=jQuery('.wide-layout-btn');if(jQuery('body').hasClass('boxed')){boxed.addClass('active-switcher-btn');jQuery('.bg-patern').css({'display':'block'});wide.removeClass('active-switcher-btn');}else{boxed.removeClass('active-switcher-btn');jQuery('.bg-patern').css({'display':'none'});wide.addClass('active-switcher-btn');}
jQuery('.boxed-layout-btn').click(function(){'use strict';jQuery(this).addClass('active-switcher-btn');jQuery('.wide-layout-btn').removeClass('active-switcher-btn');jQuery('body').addClass('boxed default');if(!jQuery('.main-wrapper').hasClass('home_transparent-wrapper')){jQuery('.main-slider').addClass('container');}
jQuery('.bg-patern').css({'display':'block'});});jQuery('.wide-layout-btn').click(function(){'use strict';jQuery(this).addClass('active-switcher-btn');jQuery('.boxed-layout-btn').removeClass('active-switcher-btn');jQuery('body').removeClass('boxed default');jQuery('.main-slider').removeClass('container');jQuery('.bg-patern').css({'display':'none'});});jQuery('.bg-patern li.pattern-default').click(function(){'use strict';jQuery('.bg-patern li').removeClass('pattern-active');jQuery('.bg-patern li.pattern-default').addClass('pattern-active');jQuery('body').addClass('default').removeClass('pattern-01 pattern-02 pattern-03 pattern-04 pattern-05 pattern-06 pattern-07');});jQuery('.bg-patern li.pattern1').click(function(){'use strict';jQuery('.bg-patern li').removeClass('pattern-active');jQuery('.bg-patern li.pattern1').addClass('pattern-active');jQuery('body').addClass('pattern-01').removeClass('default pattern-02 pattern-03 pattern-04 pattern-05 pattern-06 pattern-07');});jQuery('.bg-patern li.pattern2').click(function(){'use strict';jQuery('.bg-patern li').removeClass('pattern-active');jQuery('.bg-patern li.pattern2').addClass('pattern-active');jQuery('body').addClass('pattern-02').removeClass('default pattern-01 pattern-03 pattern-04 pattern-05 pattern-06 pattern-07');});jQuery('.bg-patern li.pattern3').click(function(){'use strict';jQuery('.bg-patern li').removeClass('pattern-active');jQuery('.bg-patern li.pattern3').addClass('pattern-active');jQuery('body').addClass('pattern-03').removeClass('default pattern-01 pattern-02 pattern-04 pattern-05 pattern-06 pattern-07');});jQuery('.bg-patern li.pattern4').click(function(){'use strict';jQuery('.bg-patern li').removeClass('pattern-active');jQuery('.bg-patern li.pattern4').addClass('pattern-active');jQuery('body').addClass('pattern-04').removeClass('default pattern-01 pattern-02 pattern-03 pattern-05 pattern-06 pattern-07');});jQuery('.bg-patern li.pattern5').click(function(){'use strict';jQuery('.bg-patern li').removeClass('pattern-active');jQuery('.bg-patern li.pattern5').addClass('pattern-active');jQuery('body').addClass('pattern-05').removeClass('default pattern-01 pattern-02 pattern-03 pattern-04 pattern-06 pattern-07');});jQuery('.bg-patern li.pattern6').click(function(){'use strict';jQuery('.bg-patern li').removeClass('pattern-active');jQuery('.bg-patern li.pattern6').addClass('pattern-active');jQuery('body').addClass('pattern-06').removeClass('default pattern-01 pattern-02 pattern-03 pattern-04 pattern-05 pattern-07');});jQuery('.bg-patern li.pattern7').click(function(){'use strict';jQuery('.bg-patern li').removeClass('pattern-active');jQuery('.bg-patern li.pattern7').addClass('pattern-active');jQuery('body').addClass('pattern-07').removeClass('default pattern-01 pattern-02 pattern-03 pattern-04 pattern-05 pattern-06');});var fixed=jQuery('.fixed-header');var stat=jQuery('.static-header');var scroll_up=jQuery('.scrollUp-header');if(jQuery('body').hasClass('static')){fixed.removeClass('active-switcher-btn');scroll_up.removeClass('active-switcher-btn ');stat.addClass('active-switcher-btn');}else if(jQuery('body').hasClass('up-scroll')){stat.removeClass('active-switcher-btn');fixed.removeClass('active-switcher-btn');scroll_up.addClass('active-switcher-btn ');}else{stat.removeClass('active-switcher-btn');scroll_up.removeClass('active-switcher-btn');fixed.addClass('active-switcher-btn ');}
jQuery('.fixed-header').click(function(){'use strict';jQuery(this).addClass('active-switcher-btn');jQuery('.static-header, .scrollUp-header').removeClass('active-switcher-btn');jQuery('body').removeClass('static up-scroll');jQuery('nav').removeClass('navbar-scrollUp');});jQuery('.scrollUp-header').click(function(){'use strict';jQuery(this).addClass('active-switcher-btn');jQuery('.fixed-header, .static-header').removeClass('active-switcher-btn');jQuery('body').removeClass('static').addClass('up-scroll');jQuery('nav').addClass('navbar-scrollUp');});jQuery('.static-header').click(function(){'use strict';jQuery(this).addClass('active-switcher-btn');jQuery('.fixed-header, .scrollUp-header').removeClass('active-switcher-btn');jQuery('body').removeClass('up-scroll').addClass('static');jQuery('nav').removeClass('navbar-scrollUp');});