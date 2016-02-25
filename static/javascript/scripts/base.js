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

	$(function () {
	  $("#profilebutton").click(function(e){
	    e.preventDefault();
	    var obj = null;
	    $('<div></div>').appendTo('#profile_message')
	    .html('<div><h3> Next, tell us about how you\'re getting here. </h3></div>')
	    .dialog({
	      title: "Confirm",
	      width: 500,
	      height: 300,
	      modal: true,
	      resizable: false,
	      show: {effect: 'drop', direction: "left"},
	      hide: {effect: 'drop', direction: 'left'},
	      buttons: [{
	        text: 'Next',
	        click: function () {
	          var data = "";
	          obj = $(this);
	          $.ajax({
	            method: "POST", 
	          	beforeSend: function(xhr, settings) {
					if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			            xhr.setRequestHeader("X-CSRFToken", csrftoken);
			        }
			    },
	            data: data,
	            dataType: 'html',
	          }).done(function(data, textStatus, jqXHR) {
	            window.location.href = '/vehicle/'; 
	            obj.dialog("close");
	          }).fail(function(jqXHR, textStatus) {
	            obj.dialog("close");
	          })
	        }
	      }]
	    });
	  });
	});

		$(function () {
	  $("#vehiclebutton").click(function(e){
	    e.preventDefault();
	    var obj = null;
	    $('<div></div>').appendTo('#vehicle_message')
	    .html('<div><h3> Next, tell us about your sleeping arrangements. </h3></div>')
	    .dialog({
	      title: "Confirm",
	      width: 500,
	      height: 300,
	      modal: true,
	      resizable: false,
	      show: {effect: 'drop', direction: "left"},
	      hide: {effect: 'drop', direction: 'left'},
	      buttons: [{
	        text: 'Next',
	        click: function () {
	          var data = "";
	          obj = $(this);
	          $.ajax({
	            method: "POST", 
	          	beforeSend: function(xhr, settings) {
					if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			            xhr.setRequestHeader("X-CSRFToken", csrftoken);
			        }
			    },
	            data: data,
	            dataType: 'html',
	          }).done(function(data, textStatus, jqXHR) {
	            window.location.href = '/campers/'; 
	            obj.dialog("close");
	          }).fail(function(jqXHR, textStatus) {
	            obj.dialog("close");
	          })
	        }
	      }]
	    });
	  });
	});

		$(function () {
	  $("#shelterbutton").click(function(e){
	    e.preventDefault();
	    var obj = null;
	    $('<div></div>').appendTo('#shelter_message')
	    .html('<div><h3> Next, pick your meal shifts. </h3></div>')
	    .dialog({
	      title: "Confirm",
	      width: 500,
	      height: 300,
	      modal: true,
	      resizable: false,
	      show: {effect: 'drop', direction: "left"},
	      hide: {effect: 'drop', direction: 'left'},
	      buttons: [{
	        text: 'Next',
	        click: function () {
	          var data = "";
	          obj = $(this);
	          $.ajax({
	            method: "POST", 
	          	beforeSend: function(xhr, settings) {
					if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			            xhr.setRequestHeader("X-CSRFToken", csrftoken);
			        }
			    },
	            data: data,
	            dataType: 'html',
	          }).done(function(data, textStatus, jqXHR) {
	            window.location.href = '/meal_schedule/'; 
	            obj.dialog("close");
	          }).fail(function(jqXHR, textStatus) {
	            obj.dialog("close");
	          })
	        }
	      }]
	    });
	  });
	});




});