var CUSTOMERFIELDS = [
  '#id_first_name',
  '#id_last_name',
  '#id_email',
  '#id_street_address',
  '#id_postcode',
  '#id_city',
  '#id_phone',
  '#id_discount'
];

function showHide () {
  var selectedCustomer = $('#id_customer').val();
  if (selectedCustomer === '') {
      $(CUSTOMERFIELDS.join(', ')).parent().parent().show();
  } else {
      $(CUSTOMERFIELDS.join(', ')).parent().parent().hide();
  }
}

$('#id_customer').on('change', showHide);
showHide();