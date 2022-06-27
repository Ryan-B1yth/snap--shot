$('#increment').click( function(e) {
    e.preventDefault()
    var value = parseInt($('#quantity').val())
    $('#quantity').val(value + 1)
})

$('#decrement').click( function(e) {
    e.preventDefault()
    var value = parseInt($('#quantity').val())
    
    isNaN(value) || value <= 0 ? 
        $('#quantity').val(0) : 
        $('#quantity').val(value - 1)
})