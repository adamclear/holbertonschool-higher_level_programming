$('#toggle_header').click(() => {
  $('header').toggleClass('red green');
});
$('#toggle_header').hover(() => {
  $('#toggle_header').css('cursor', 'pointer');
});