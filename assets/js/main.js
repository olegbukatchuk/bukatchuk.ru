/* Бургер-меню и год в подвале. Больше на страницах скриптов нет. */
(function () {
  var b = document.getElementById('burger'), n = document.getElementById('nav');
  if (b && n) {
    b.addEventListener('click', function () {
      var open = n.classList.toggle('is-open');
      b.setAttribute('aria-expanded', open);
    });
  }
})();
