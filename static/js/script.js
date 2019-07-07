function scroll_to(clicked_link) {
	var element_class = clicked_link.attr('href');
	var scroll_to = $(element_class).offset().top;
	if($(window).scrollTop() != scroll_to) {
		$('html, body').stop().animate({scrollTop: scroll_to}, 1000);
	}
}

jQuery(document).ready(function() {
	$('.scroll-link').on('click', function(e) {
		e.preventDefault();
		scroll_to($(this));
	});
});

