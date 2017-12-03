function toggleTheme(){
    $('link').each(function(){
        var ref = $(this).attr('href');
        if (ref == '/static/toolkit-inverse.css'){
            $(this).removeAttr('href').attr('href', '/static/toolkit-light.css');
            saveCSSinCookie('/static/toolkit-light.css')
        } else if (ref == '/static/toolkit-light.css'){
            $(this).removeAttr('href').attr('href', '/static/toolkit-inverse.css');
            saveCSSinCookie('/static/toolkit-inverse.css')
        }
    });
}

function readCookieCSS(){
    if($.cookie('styleSheet') === null || $.cookie('styleSheet')==undefined) {
        console.log('No stylesheet cookie found')
    }
    else{
        $('link[href="/static/toolkit-inverse.css"]').attr('href',$.cookie('styleSheet'));
        console.log('Reading stylesheet from cookie')
    }
}

function saveCSSinCookie(STYLESHEET_COOKIE) {
    if ($.cookie('styleSheet') === null || $.cookie('styleSheet') == undefined) {
        $.cookie("styleSheet", STYLESHEET_COOKIE, { expires : 365 });//expires after 1 year
    } else {
        $.cookie('styleSheet', STYLESHEET_COOKIE);
    }
}

$(document).ready(function(){
    readCookieCSS();
    $('.nav-link').tooltip({show: {effect:'none', delay:300}});
});


