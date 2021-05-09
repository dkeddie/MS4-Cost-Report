
// Makes rows on 'List of changes' clickable to open edit change
$('#table-changes tbody tr').click(function () {
  var change_id = $(this).children('.change_id_select').text();
  window.location.href = `/dashboard/edit_change/${change_id}/`;
});

// Sends data from the attachment to the modal to operate
$('#table-attachments button').click(function() {
  var x = $(this).attr('data-url');
  var y = $(this).parent().prev().prev().text();
  $('h5.attachment-name>em').text(y);
  $('#deleteAttachmentModal a').attr('href', x);
});


$(window).on('load', function() {
  // Limits editing if User Perimission is View only
  var permission = $('#user_permission').val();
  if (permission === 'View') {
    $('#edit-change-form input').prop('readonly', true);
    $('#edit-change-form select[name="change_status"]').prop('disabled', true);
  }

  // Remove decimal points from Change Cost
  var x = $('#id_change_cost').val().split(".", 1)[0];
  $('#id_change_cost').val(x);
});
