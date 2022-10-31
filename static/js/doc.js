$(document).ready(function (e){
	e.preventDefault();
    $("#submit").click(function (e) {
		e.preventDefault();
        $.ajax({
            url: '/convert',
            success: function(result){
                console.log("done, result=%s", result);
            }
        });
    });
});
