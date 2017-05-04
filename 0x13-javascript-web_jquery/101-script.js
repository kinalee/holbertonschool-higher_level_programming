// adds, removes and clears LI elements from a list when the user clicks
window.onload = function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append($('<LI></LI>').text('Item'));
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove()
  });
  $('DIV#clear_list').click(function () {
    $('LI').remove();
  });
};
