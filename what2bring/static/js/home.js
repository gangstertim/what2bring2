function onSubmit() {
  var formData = {};
  var errors = [];
  var fields = ['eventName', 'eventDate', 'eventTime', 
    'eventLocation', 'eventDescription', 'hostName', 
    'hostEmail', 'guestNames', 'guestEmails',
    'dishesToBring', 'acceptCash', 'cashAmount'
  ];

  fields.forEach(function(field) {
    var data = $('#' + field).val();
    var error = validateField[field] && validateField[field](data);
    if (error) errors.push({field: field, error: error});
    if (data) formData[field] = data;
  });

  //if (errors.length) {
  //  console.log(errors);
  //} else {
    console.log(formData);
    $.post('events', formData);
  //}
}

var validateField = {
  hostName: isRequired,
  eventName: isRequired
};

function isRequired(data) {
  return (data === undefined) ? 'This field is required!' : null;
}
