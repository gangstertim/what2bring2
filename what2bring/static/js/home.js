$('#submit').click(function() {
  var $form = $('#event-creation-form');

  // Move event name into form field
  var eventName = $('#eventName').val();
  $('#_eventName').val(eventName);

  //TODO: do some validation

  $form.submit();
});