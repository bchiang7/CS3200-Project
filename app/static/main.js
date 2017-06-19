$(document).ready(function() {
  // get current URL path and assign 'active' class
  const pathname = window.location.pathname;
  $('nav li > a[href="'+pathname+'"]').addClass('active');

  const selectedContinent = $("#continent :selected").text();
  const selectedClimate = $("#climate :selected").text();
  const selectedCountry = $("#country :selected").text();
  const selectedCategory = $("#category :selected").text();
  const selectedOrigin = $("#origin :selected").text();

  $('#filter').click( () => {

    const filters = [
      selectedContinent,
      selectedClimate,
      selectedCountry,
      selectedCategory,
      selectedOrigin
    ]

    console.log(filters);

  });


})