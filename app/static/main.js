$(document).ready(function() {
  // get current URL path and assign 'active' class
  const pathname = window.location.pathname;
  $('nav li > a[href="'+pathname+'"]').addClass('active');

  $.getJSON('http://api.fixer.io/latest?base=USD', function(data) {
    console.log(data);
  });

  // set hidden input value for review deletion
  $('.delete').click(function() {
    id = $(this).data('id');
    $('#deleteReviewModal input.form-control').val(id);
  });

})