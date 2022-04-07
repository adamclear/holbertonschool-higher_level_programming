$('#add_item').click(() => {
  $('.my_list').append('<li>Item</li>');
});
$('#add_item').hover(() => {
  $('#add_item').css('cursor', 'pointer');
});