
const plus_sign = document.querySelector('plus-sign-1')
plus_sign.addEventListner("click", rotate45());

function rotate45(){
    plus_sign.classList.add("plus_sign");
}