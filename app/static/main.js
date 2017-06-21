$(document).ready(function() {
  // get current URL path and assign 'active' class
  const pathname = window.location.pathname;
  $('nav li > a[href="'+pathname+'"]').addClass('active');

  // $.getJSON('http://api.fixer.io/latest?base=USD', function(data) {
  //   console.log(data);
  // });

  // set hidden input value for review deletion
  $('.delete').click(function() {
    id = $(this).data('id');
    $('#deleteReviewModal input.form-control').val(id);
  });

  // if visitor ID does not exist in set visitorID in local storage after adding a visitor
  if (pathname == '/profile') {
    visitorID = $('#visitorid').val()
    localStorage.setItem('visitorID', visitorID);
  }

  function setReviewsURL() {
    visitor_id = localStorage.getItem('visitorID');
    $('.yourreviews a').attr('href', "/yourreviews/"+ visitor_id +"");
  }
  setReviewsURL();

  // if visitor ID exists in local storage
  if (localStorage.getItem('visitorID') !== null) {
    $('.yourreviews').show();
    $('.nav-id').show();
    // show ID in nav bar
    visitorID = localStorage.getItem('visitorID');
    $('#navIDNum').text(visitorID);

    // auto fill visitor ID field then writing a review
    if (pathname == '/review') {
      visitorID = localStorage.getItem('visitorID');
      $('#visitorID').val(visitorID);
    }
  }



})