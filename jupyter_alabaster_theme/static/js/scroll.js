$(window).on("scroll", function () {
    if ($(this).scrollTop() > 200) {
        $(".navbar").addClass("transparent");
        // $(".navbar").stop().animate({opacity: 0});
    }
    else {
        $(".navbar").removeClass("transparent");
        // $(".navbar").stop().animate({opacity: 1});
    }
});
$(window).on("scroll", function () {
    if ($(this).scrollTop() > 0) {
        $(".navbar").addClass("navbar-scroll");
        // $(".navbar").stop().animate({opacity: 0});
    }
    else {
        $(".navbar").removeClass("navbar-scroll");
        // $(".navbar").stop().animate({opacity: 1});
    }
});

var scroll_to_target = function (target, complete) {
    var target = $(target);
    if (target.length) {
        $('html, body').animate({scrollTop: target.offset().top - 120}, 1, complete);
    }
}

// Because we have a fixed position nav bar, when a user clicks on a target with a #hash
// we have to scroll the page a bit so the target is visible.
$(window).on("load", function () {
    // Handle the case where we are loading a page with a #id target in the URL
    var hash = window.location.hash;
    if (hash) {
        scroll_to_target(hash);
    }

    // Handle the case when the user clicks on a #id target on the current page
    $('a[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
            var target = $(this.hash);
            var hash = this.hash;
            target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
            scroll_to_target(target, function () {
                location.hash = hash;
            });
            if (target.length) { return false; }
        }
    });
});



