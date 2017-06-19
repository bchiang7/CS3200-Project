$(document).ready(function() {
  // get current URL path and assign 'active' class
  const pathname = window.location.pathname;
  $('nav li > a[href="'+pathname+'"]').addClass('active');


  // $('#filter').on('click', () => {
  //   const selectedContinent = $("#continent :selected").text();
  //   const selectedClimate = $("#climate :selected").text();
  //   const selectedCountry = $("#country :selected").text();
  //   const selectedCategory = $("#category :selected").text();
  //   const selectedOrigin = $("#origin :selected").text();

  //   const filters = [selectedContinent, selectedClimate, selectedCountry, selectedCategory, selectedOrigin];

  //   console.log(filters);

  // });



  $.getJSON('http://api.fixer.io/latest?base=USD', function(data) {
    console.log(data);
  });

})