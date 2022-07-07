$(document).ready(function() {
    $("a.nav-link").each(function() {
        if (this.href == window.location.href) {
            $(this).addClass("active");
        } 
    });

    if ($(".booking-link").hasClass("active") === true){
        getDates()
    } else {
        sideNavCheck();
    };

    document.addEventListener("scroll", sideNavCheck, { passive: true });
    
 
    function sideNavCheck(){

        let windowHeight = window.innerHeight
        let scrollDemo = document.documentElement
        let x = scrollDemo.scrollTop

        let pathName = window.location.pathname  

        if (pathName == '/') {
            if (x < windowHeight/2) {
                $(".about-link").addClass("active")
                $(".menu-link").removeClass("active")
                $(".drinks-link").removeClass("active")
                $(".contact-link").removeClass("active")
            }
            if (x > windowHeight/2 && x < (3/2)*windowHeight) {
                $(".menu-link").addClass("active")
                $(".about-link").removeClass("active")
                $(".drinks-link").removeClass("active")
                $(".contact-link").removeClass("active")
    
            }
            if (x > (3/2)*windowHeight && x < (5/2)*windowHeight){
                $(".drinks-link").addClass("active")
                $(".about-link").removeClass("active")
                $(".menu-link").removeClass("active")
                $(".contact-link").removeClass("active")
            }
            if (x >= (5/2)*windowHeight){
                $(".contact-link").addClass("active")
                $(".about-link").removeClass("active")
                $(".menu-link").removeClass("active")
                $(".drinks-link").removeClass("active")
            }
        }   
    }
   

    function getDates() {
    let dateControl = document.querySelector('input[type="date"]');
    let today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0'); 
    let mmPlusone = String(today.getMonth() + 2).padStart(2, '0');
    let yyyy = today.getFullYear();
    today = yyyy + '-' + mm + '-' + dd
    todayPlusMonth = yyyy + '-' + mmPlusone + '-' + dd
    dateControl.value = today;
    dateControl.min = today;
    dateControl.max = todayPlusMonth;
    }
});