$('.increment').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue + 1);
   var itemId = $(this).data('item_id');

    isNaN(currentValue) || currentValue >= 99 ? 
        $(closestInput).val(99) : 
        $(closestInput).val(currentValue + 1);
});

$('.decrement').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue - 1);
   var itemId = $(this).data('item_id');

    isNaN(currentValue) || currentValue <= 0 ? 
       $(closestInput).val(0) : 
       $(closestInput).val(currentValue - 1);
});