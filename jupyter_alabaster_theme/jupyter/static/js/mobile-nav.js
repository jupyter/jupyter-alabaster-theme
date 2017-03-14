$(document).on('ready', function() {
    $('.mobile-nav-section').on('click', function() {
        console.log('pressed');
        $('.mobile-nav-expand-icon').css('transform', 'rotate(45deg)');
    });
});