
// Remove User button -> sends info to Modal to delete user
$('#table-users button').click(function() {
  var x = $(this).attr('data-url');
  var y = $(this).attr('data-user');
  $('#remove-userModal a').attr('href', x);
  $('#remove-userModal h5 strong').text(y);
});

// Enable edit of Project Details from read-only
function enableEdit() {
  $('input[readonly]').prop('readonly', false);
  $('.enable-edit').addClass('d-none');
  $('.submit-button').removeClass('d-none');
}