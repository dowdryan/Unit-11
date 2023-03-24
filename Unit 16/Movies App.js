$(function() {
    $("#form").on("submit", function(event) {
        event.preventDefault()
        let title = $("#title").val();
        let rating = $("#rating").val();
        $('#ul').append(`<li>${title}: ${rating}/10</li>`)
        $('#delete').css("visibility", "visible");
    })

    $('#delete').on('click', function() {
        $('#ul').empty()
        $('#delete').css("visibility", "hidden");
    })
})
