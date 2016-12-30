function onSubmit() {
  var formData = {};
  var errors = [];
  var fields = ['inputEventName', 'inputDate', 'inputTime', 
    'inputLocation', 'inputDescription', 'inputName', 
    'inputUserEmail', 'inputGuests', 'inputGuestEmails',
    'inputToBring', 'inputCash', 'inputCashAmount'
  ];

  fields.forEach(function(field) {
    var data = $(field).val();
    var error = validateField[field] && validateField[field](data);
    if (error) errors.push({field: field, error: error});
    formData[field] = data;
  });

  //if (errors.length) {
  //  console.log(errors);
  //} else {
    $.post("events", formData);
  //}
}

var validateField = {
  inputName: isRequired,
  inputEventName: isRequired
};

function isRequired(data) {
  return (data === undefined) ? 'This field is required!' : null;
}
