$(document).ready(() => {
  jQuery.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', (result) => {
    $('#hello').text(result.hello);
  });
});
