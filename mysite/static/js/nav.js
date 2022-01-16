let menu = document.getElementById('menu');
let ul = document.getElementById('ul');
let nav = document.getElementById('nav');
console.log(nav);
let ham = () => {
  if (ul.style.right == '-400px') {
    ul.style.right = "0px"
    menu.innerHTML = "&#10799;"

  } else {
    ul.style.right = '-400px'
    menu.innerHTML = '&equiv;'

  }
}
menu.addEventListener('click', ham)
window.onclick = function(event) {
  if (event.target == ul) {
    ul.style.right = '-45vw'
  }
}