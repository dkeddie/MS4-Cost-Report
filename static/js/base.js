function enableEdit() {
  $('.submit-button').removeClass('d-none')
  $('.enable-edit').addClass('d-none')
}

// Datatables.Net activation
$(document).ready( function () {
  $('#table-project').DataTable( {
    // "columns": [
    //   { "width": "65%" },
    //   { "width": "35%" },
    // ],
    "ordering": false,
    "lengthChange": false,
    "searching": false,
    "bInfo": false,
    "pageLength": 6,
    "pagingType": "simple",
    // "scrollX": true
  });
  $('#table-users').DataTable( {
    "ordering": true,
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
  $('#table-attachments').DataTable( {
    "columns": [
      { "width": "85%" },
      { "width": "10%" },
      { "width": "5%" },
    ],
    "lengthChange": false,
    "pageLength": 9,
    "pagingType": "simple",
    "searching": false,
    "order": [[ 0, "asc" ]],
  });
} );

// Make the row 'clickable' to open the Change to view/edit details
// https://electrictoolbox.com/jquey-make-entire-table-row-clickable/
$(document).ready(function () {
  $('table-change>tr').click(function () {
    var href = $(this).find('a').attr('href');
    if (href) {
      window.location = href;
    }
  });
});

