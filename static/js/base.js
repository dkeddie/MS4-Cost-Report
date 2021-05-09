
// Message container - to show and automatically hide
$(document).ready(function () {
  $('.toast').toast('show');
  setTimeout(() => {
    $('.toast').hide();
  }, 5000);
});


// Button to enable Form editing on 'Home' page and elsewhere
function enableEdit() {
  $('.submit-button').removeClass('d-none');
  $('.enable-edit').addClass('d-none');
}


// Datatables.Net activation and formatting
$(document).ready(function () {
  // Home View - Projects available to user
  $('#table-project').DataTable({
    "ordering": false,
    "lengthChange": false,
    "searching": false,
    "bInfo": false,
    "pageLength": 6,
    "pagingType": "simple",
  });
  // Admin View - Users who can access the project
  $('#table-users').DataTable({
    "ordering": true,
    "lengthChange": false,
    "searching": false,
    "bInfo": false,
    "pageLength": 5,
    "pagingType": "simple"
  });
  // Dashboard View - Changes on the Project
  $('#table-changes').DataTable({
    "columns": [
      { "width": null },
      { "width": "20%" },
      { "width": "10%" },
      { "width": "0%" }
    ],
    "lengthChange": false,
    "pageLength": 9,
    "pagingType": "simple",
    "order": [[3, "asc"]],
  });
  // Edit View - Attachments associated with a Change
  $('#table-attachments').DataTable({
    "columns": [
      { "width": "85%" },
      { "width": "10%" },
      { "width": "5%" },
    ],
    "lengthChange": false,
    "pageLength": 9,
    "pagingType": "simple",
    "searching": false,
    "order": [[0, "asc"]],
  });
});


// Bootrap - enable tooltips to show
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})