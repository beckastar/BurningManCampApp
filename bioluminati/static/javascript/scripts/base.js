$(document).ready(function () {

	// $('.availShifts').click(function(){
	// 	$(".datarow").toggleClass("showTable hideTable");
	// });

	$("#meal_shift_help_icon").click(function(){
		$(".table_instructions").toggleClass("hidden shown");
		console.log("clicked");
	});

	// make dialog box appear 
	$("#vehiclebutton").click(function(e){
		e.preventDefault();
		$('<div></div>').appendTo('#vehicle_message')
			.html('<div><h3> Next, tell us about your sleeping arrangements. </h3></div>')
			.dialog({
				title: "Confirm",
				width: 500, 
				height: 300,
				modal: true,
				resizable: false,
				show: { effect: 'drop', direction: "left" }, 
				hide: {effect:'drop', direction:'left'},
				buttons: {
					Next: function() {
						$.ajax({ 
							window.location.href('http://127.0.0.1:8000/campers')
							$(this).dialog("close");
						}) 
				}

			}
		})
	})
});