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
  $('#table-changes').DataTable( {
    "columns": [
      { "width": "69%" },
      { "width": "20%" },
      { "width": "10%" },
      { "width": "0%" }
    ],
    "lengthChange": false,
    "pageLength": 9,
    "pagingType": "simple",
    "order": [[ 3, "asc" ]],
  });
} );

// Make the row 'clickable' to open the Change to view/edit details
// https://electrictoolbox.com/jquey-make-entire-table-row-clickable/
$(document).ready(function () {
  $('tr').click(function () {
    var href = $(this).find('a').attr('href');
    if (href) {
      window.location = href;
    }
  });
});

