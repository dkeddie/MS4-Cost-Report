
// Enable edit button - change fields from read-only to edit
function enableEdit() {
  $('input[readonly]').prop('readonly', false);
  $('.enable-edit').addClass('d-none');
  $('.submit-button').removeClass('d-none');
}