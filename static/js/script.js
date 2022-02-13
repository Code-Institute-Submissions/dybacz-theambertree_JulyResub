$(document).ready(function() {
    $("a.nav-link").each(function() {
        if (this.href == window.location.href) {
            $(this).addClass("active");
        } else if ($(document).prop('title') != 'The Amber Tree | Restaurant & Bar'){
            $(this).removeClass("active")
        }
    });


    $(window).on('hashchange', function(){
        $("a.nav-link").each(function() {
            if (this.href == window.location.href) {
                $(this).addClass("active");
            } else {
                $(this).removeClass("active")
            }
        });
    });
});