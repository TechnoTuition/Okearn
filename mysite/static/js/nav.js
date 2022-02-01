let menu = document.getElementById('menu');
let ul = document.getElementById('ul');
let nav = document.getElementById('nav');
console.log(nav);
let ham = () => {
  if (ul.style.right == '-400px') {
    ul.style.right = "0px"
    menu.innerHTML = `<i class="bi bi-x"></i>`

  } else {
    ul.style.right = '-400px'
    menu.innerHTML = `<i class="bi bi-list"></i>`

  }
}
menu.addEventListener('click', ham)
