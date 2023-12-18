const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

menu.addEventListener('click', function() {
  menu.classList.toggle('is-active');
  menuLinks.classList.toggle('active');
});

function redirectToOneCom() {
  window.location.href = '/onecom';
}

function redirectToLaPress() {
  window.location.href = '/lapress';
}

