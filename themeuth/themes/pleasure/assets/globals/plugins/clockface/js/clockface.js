(function($){var Clockface=function(element,options){this.$element=$(element);this.options=$.extend({},$.fn.clockface.defaults,options,this.$element.data());this.init();};Clockface.prototype={constructor:Clockface,init:function(){this.$clockface=$($.fn.clockface.template);this.$clockface.find('.l1 .cell, .left.cell').html('<div class="outer"></div><div class="inner"></div>');this.$clockface.find('.l5 .cell, .right.cell').html('<div class="inner"></div><div class="outer"></div>');this.$clockface.hide();this.$outer=this.$clockface.find('.outer');this.$inner=this.$clockface.find('.inner');this.$ampm=this.$clockface.find('.ampm');this.ampm=null;this.hour=null;this.minute=null;this.$ampm.click($.proxy(this.clickAmPm,this));this.$clockface.on('click','.cell',$.proxy(this.click,this));this.parseFormat();this.prepareRegexp();this.ampmtext=this.is24?{am:'12-23',pm:'0-11'}:{am:'AM',pm:'PM'};this.isInline=this.$element.is('div');if(this.isInline){this.$clockface.addClass('clockface-inline').appendTo(this.$element);}else{this.$clockface.addClass('dropdown-menu').appendTo('body');if(this.options.trigger==='focus'){this.$element.on('focus.clockface',$.proxy(function(e){this.show();},this));}
$(document).off('click.clockface').on('click.clockface',$.proxy(function(e){var $target=$(e.target);if($target.closest('.clockface').length){return;}
$('.clockface-open').each(function(){if(this===e.target){return;}
$(this).clockface('hide');});},this));}
this.fill('minute');},show:function(value){if(this.$clockface.is(':visible')){return;}
if(!this.isInline){if(value===undefined){value=this.$element.val();}
this.$element.addClass('clockface-open');this.$element.on('keydown.clockface',$.proxy(this.keydown,this));this.place();$(window).on('resize.clockface',$.proxy(this.place,this));}
this.$clockface.show();this.setTime(value);this.$element.triggerHandler('shown.clockface',this.getTime(true));},hide:function(){this.$clockface.hide();if(!this.isInline){this.$element.removeClass('clockface-open');this.$element.off('keydown.clockface');$(window).off('resize.clockface');}
this.$element.triggerHandler('hidden.clockface',this.getTime(true));},toggle:function(value){if(this.$clockface.is(':visible')){this.hide();}else{this.show(value);}},setTime:function(value){var res,hour,minute,ampm='am';if(value===undefined){if(this.ampm===null){this.setAmPm('am');}
return;}
if(value instanceof Date){hour=value.getHours();minute=value.getMinutes();}
if(typeof value==='string'&&value.length){res=this.parseTime(value);if(res.hour===24){res.hour=0;}
hour=res.hour;minute=res.minute;ampm=res.ampm;}
if(hour>11&&hour<24){ampm='pm';if(!this.is24&&hour>12){hour-=12;}}else if(hour>=0&&hour<11){if(this.is24||hour===0){ampm='am';}}
this.setAmPm(ampm);this.setHour(hour);this.setMinute(minute);},setAmPm:function(value){if(value===this.ampm){return;}else{this.ampm=value==='am'?'am':'pm';}
this.$ampm.text(this.ampmtext[this.ampm]);this.fill('hour');this.highlight('hour');},setHour:function(value){value=parseInt(value,10);value=isNaN(value)?null:value;if(value<0||value>23){value=null;}
if(value===this.hour){return;}else{this.hour=value;}
this.highlight('hour');},setMinute:function(value){value=parseInt(value,10);value=isNaN(value)?null:value;if(value<0||value>59){value=null;}
if(value===this.minute){return;}else{this.minute=value;}
this.highlight('minute');},highlight:function(what){var index,values=this.getValues(what),value=what==='minute'?this.minute:this.hour,$cells=what==='minute'?this.$outer:this.$inner;$cells.removeClass('active');index=$.inArray(value,values);if(index>=0){$cells.eq(index).addClass('active');}},fill:function(what){var values=this.getValues(what),$cells=what==='minute'?this.$outer:this.$inner,leadZero=what==='minute';$cells.each(function(i){var v=values[i];if(leadZero&&v<10){v='0'+v;}
$(this).text(v);});},getValues:function(what){var values=[11,0,1,10,2,9,3,8,4,7,6,5],result=values.slice();if(what==='minute'){$.each(values,function(i,v){result[i]=v*5;});}else{if(!this.is24){result[1]=12;}
if(this.is24&&this.ampm==='pm'){$.each(values,function(i,v){result[i]=v+12;});}}
return result;},click:function(e){var $target=$(e.target),value=$target.hasClass('active')?null:$target.text();if($target.hasClass('inner')){this.setHour(value);}else{this.setMinute(value);}
if(!this.isInline){this.$element.val(this.getTime());}
this.$element.triggerHandler('pick.clockface',this.getTime(true));},clickAmPm:function(e){e.preventDefault();this.setAmPm(this.ampm==='am'?'pm':'am');if(!this.isInline&&!this.is24){this.$element.val(this.getTime());}
this.$element.triggerHandler('pick.clockface',this.getTime(true));},place:function(){var zIndex=parseInt(this.$element.parents().filter(function(){return $(this).css('z-index')!='auto';}).first().css('z-index'),10)+10,offset=this.$element.offset();this.$clockface.css({top:offset.top+this.$element.outerHeight(),left:offset.left,zIndex:zIndex});},keydown:function(e){if(/^(9|27|13)$/.test(e.which)){this.hide();return;}
clearTimeout(this.timer);this.timer=setTimeout($.proxy(function(){this.setTime(this.$element.val());},this),500);},parseFormat:function(){var format=this.options.format,hFormat='HH',mFormat='mm';$.each(['HH','hh','H','h'],function(i,f){if(format.indexOf(f)!==-1){hFormat=f;return false;}});$.each(['mm','m'],function(i,f){if(format.indexOf(f)!==-1){mFormat=f;return false;}});this.is24=hFormat.indexOf('H')!==-1;this.hFormat=hFormat;this.mFormat=mFormat;},parseTime:function(value){var hour=null,minute=null,ampm='am',parts=[],digits;value=$.trim(value);if(this.regexpSep){parts=value.match(this.regexpSep);}
if(parts&&parts.length){hour=parts[1]?parseInt(parts[1],10):null;minute=parts[2]?parseInt(parts[2],10):null;ampm=(!parts[3]||parts[3].toLowerCase()==='a')?'am':'pm';}else{value=value.split('').reverse().join('').replace(/\s/g,'');parts=value.match(this.regexpNoSep);if(parts&&parts.length){ampm=(!parts[1]||parts[1].toLowerCase()==='a')?'am':'pm';digits=parts[2].split('').reverse().join('');switch(digits.length){case 1:hour=parseInt(digits,10);break;case 2:hour=parseInt(digits,10);if(hour>24){hour=parseInt(digits[0],10);minute=parseInt(digits[1],10);}
break;case 3:hour=parseInt(digits[0],10);minute=parseInt(digits[1]+digits[2],10);if(minute>59){hour=parseInt(digits[0]+digits[1],10);minute=parseInt(digits[2],10);if(hour>24){hour=null;minute=null;}}
break;case 4:hour=parseInt(digits[0]+digits[1],10);minute=parseInt(digits[2]+digits[3],10);if(hour>24){hour=null;}
if(minute>59){minute=null;}}}}
return{hour:hour,minute:minute,ampm:ampm};},prepareRegexp:function(){var sep=this.options.format.match(/h\s*([^hm]?)\s*m/i);if(sep&&sep.length){sep=sep[1];}
this.separator=sep;this.regexpSep=(this.separator&&this.separator.length)?new RegExp('(\\d\\d?)\\s*\\'+this.separator+'\\s*(\\d?\\d?)\\s*(a|p)?','i'):null;this.regexpNoSep=new RegExp('(a|p)?\\s*(\\d{1,4})','i');},getTime:function(asObject){if(asObject===true){return{hour:this.hour,minute:this.minute,ampm:this.ampm};}
var hour=this.hour!==null?this.hour+'':'',minute=this.minute!==null?this.minute+'':'',result=this.options.format;if(!hour.length&&!minute.length){return '';}
if(this.hFormat.length>1&&hour.length===1){hour='0'+hour;}
if(this.mFormat.length>1&&minute.length===1){minute='0'+minute;}
if(!minute.length&&this.separator){result=result.replace(this.separator,'');}
result=result.replace(this.hFormat,hour).replace(this.mFormat,minute);if(!this.is24){if(result.indexOf('A')!==-1){result=result.replace('A',this.ampm.toUpperCase());}else{result=result.replace('a',this.ampm);}}
return result;},destroy:function(){this.hide();this.$clockface.remove();if(!this.isInline&&this.options.trigger==='focus'){this.$element.off('focus.clockface');}}};$.fn.clockface=function(option){var d,args=Array.apply(null,arguments);args.shift();if(option==='getTime'&&this.length&&(d=this.eq(0).data('clockface'))){return d.getTime.apply(d,args);}
return this.each(function(){var $this=$(this),data=$this.data('clockface'),options=typeof option=='object'&&option;if(!data){$this.data('clockface',(data=new Clockface(this,options)));}
if(typeof option=='string'&&typeof data[option]=='function'){data[option].apply(data,args);}});};$.fn.clockface.defaults={format:'H:mm',trigger:'focus'};$.fn.clockface.template=''+
'<div class="clockface">'+
'<div class="l1">'+
'<div class="cell"></div>'+
'<div class="cell"></div>'+
'<div class="cell"></div>'+
'</div>'+
'<div class="l2">'+
'<div class="cell left"></div>'+
'<div class="cell right"></div>'+
'</div>'+
'<div class="l3">'+
'<div class="cell left"></div>'+
'<div class="cell right"></div>'+
'<div class="center"><a href="#" class="ampm"></a></div>'+
'</div>'+
'<div class="l4">'+
'<div class="cell left"></div>'+
'<div class="cell right"></div>'+
'</div>'+
'<div class="l5">'+
'<div class="cell"></div>'+
'<div class="cell"></div>'+
'<div class="cell"></div>'+
'</div>'+
'</div>';}(window.jQuery));