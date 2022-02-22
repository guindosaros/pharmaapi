(function($) { 
	"use strict";

/* JavaScript Document */
jQuery(document).ready(function() {
    'use strict';

	/*  Blog post Carousel function by = owl.carousel.js */
	jQuery('.list-carousel').owlCarousel({
		loop:true,
		autoplay:true,
		margin:15,
		nav:true,
		dots: false,
		navText: ['<i class="fa fa-arrow-left"></i>', '<i class="fa fa-arrow-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			
			480:{
				items:2
			},			
			
			767:{
				items:3
			},
			1000:{
				items:3
			}
		}
	})	
	
	/*  Testimonials Carousel Carousel function by = owl.carousel.js */
	jQuery('.testimonials-carousel').owlCarousel({
		loop:true,
		autoplay:true,
		margin:15,
		center: true,
		nav:true,
		dots: false,
		navText: ['<i class="la la-arrow-left"></i>', '<i class="la la-arrow-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			
			480:{
				items:1
			},			
			
			767:{
				items:2
			},
			991:{
				items:2
			},
			1200:{
				items:3
			}
		}
	})	
	
	/*  Testimonials Carousel Carousel function by = owl.carousel.js */
	jQuery('.item4').owlCarousel({
		loop:true,
		autoplay:true,
		margin:15,
		nav:true,
		dots: false,
		navText: ['<i class="la la-arrow-left"></i>', '<i class="la la-arrow-right"></i>'],
		responsive:{
			0:{
				items:1
			},
			
			480:{
				items:2
			},			
			
			767:{
				items:2
			},
			991:{
				items:3
			},
			1200:{
				items:4
			}
		}
	})	
	
});
/* Document .ready END */	
	
})(jQuery);		
