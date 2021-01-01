$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar-fixed-top");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});

$(".homeSouth").click(function() {
  var offset = 60;
  if($(window).width() < 992) {
      offset = 54;
  }
  $('html,body').animate({
      scrollTop: $(".welcome").offset().top - offset},'slow');
});