// $(document).ready(function () {

$(function() {
	$('#item_form').submit(
		function(event) {
			event.preventDefault();

			$.ajax({
				url: $(this).attr('action'),
				type: 'post',
				data: $(this).serialize(),
				success: function(data) {
					$('#status').text('Successfully updated' + data.title).show().fadeOut(5000);
					console.log(data);
				},
				error: function (xd4, statusText, errorText) {
                    $('#status').text('Uh oh. Something didn\'t go right.');
                    console.log("error was " + statusText + " and error text was " + errorText);
                },
        });
	});

	$("#increment").click(
		function(event) {
			event.preventDefault();
			form = $(this).parents("form");
			form.find("#id_quantity").val(Number(form.find("#id_quantity").val()) + 1);
			form.submit();
	});

	$("#decrement").click(
		function(event) {
			event.preventDefault();
			form = $(this).parents("form");
			form.find("#id_quantity").val(Number(form.find("#id_quantity").val()) - 1);
			form.submit();
	});
			
			
});
