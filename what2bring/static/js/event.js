function onAddGuestClick() {
  $('#add-guest').hide();
  $('#rsvp-well').show();
}

$('#bring-button').click(function(e) {
  e.preventDefault();
  $('#dishes-container').show();
});

$('#submit').click(function() {

  var $form = $('#guest-creation-form');
  var selectedDishes = [];

  var dishes = $('#dishes-container .dish');
  for (var i = 0; i < dishes.length; i++) {
    //TODO: Not sure what the right way to verify this value is... this doesn't work
    if (dishes[i].value === 'on') {
      selectedDishes.push(dishes[i].dataset.dish);
    }
  }

  // Move dishes into form field
  $('#_dishes').val(selectedDishes.join(','));
  debugger;

  $form.submit();
});
