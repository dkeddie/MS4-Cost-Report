function enableEdit() {
  $('.submit-button').removeClass('d-none')
  $('.enable-edit').addClass('d-none')
}

// Datatables.Net activation
$(document).ready( function () {
  $('#table-project').DataTable( {
    "ordering": false,
    "lengthChange": false,
    "searching": false,
    "bInfo": false,
    "pageLength": 5,
    "pagingType": "simple"
  });
} );