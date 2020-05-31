$(document).ready(function(){

    // owl-carousel
    $('.owl-carousel').owlCarousel({
        loop:true,
        nav:true,
        items: 1,
        navText: [],
        autoplay: true,
        autoplaySpeed: 1000,
        smartSpaeed: 500
    })

    // wow reveal
    new WOW().init();
});