"use strict";
/*! events.js | Friendkit | © Css Ninja. 2019-2020 */$((function(){$("#events-page").length&&$(".scroll-link").on("click",(function(t){t.preventDefault(),$(this).siblings(".scroll-link").removeClass("is-active"),$(this).addClass("is-active");var s=$(this).attr("data-event-id");$("#event-list");$("html, body").animate({scrollTop:$("#"+s).offset().top-58},500)}))}));