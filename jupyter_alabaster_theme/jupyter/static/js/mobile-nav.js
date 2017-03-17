$(function() {
    $('.mobile-nav-section, .mobile-nav-current-dropdown').on('click', function() {
        var openToggle = $(this).find('.mobile-nav-expand-icon');
        if (openToggle.hasClass('close-icon')) {
          openToggle.removeClass('close-icon');
        }
        else {
          openToggle.addClass('close-icon');
        }
    });
});
