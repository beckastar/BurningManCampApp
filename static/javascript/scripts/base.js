$(document).ready(function () {

	$('#campertoggle').click(function(){
		$(".campertable").toggleClass("hidden shown");
		console.log("clicked");	
	});


	$("#meal_shift_help_icon").click(function(){
		$(".table_instructions").toggleClass("hidden shown");
		console.log("clicked");
	});

	function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
	    var cookies = document.cookie.split(';');
	    for (var i = 0; i < cookies.length; i++) {
	        var cookie = jQuery.trim(cookies[i]);
	        // Does this cookie string begin with the name we want?
	        if (cookie.substring(0, name.length + 1) == (name + '=')) {
	            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	            break;
	        }
	    }
	}
	    return cookieValue;
	}

	var csrftoken = getCookie('csrftoken');
	console.log(csrftoken);

	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

});