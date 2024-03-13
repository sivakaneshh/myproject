
const cartIcon = document.querySelector('.cart')
const cartBox = document.querySelector('.cart-box')
const cross = document.querySelector(".cross")

cartIcon.addEventListener('click',()=>{
    cartBox.classList.add('cart-active');
});
cross.addEventListener("click",()=>{
    cartBox.classList.remove('cart-active');
});


document.addEventListener("DOMContentLoaded",loadFood());

function loadFood(){
    loadContent();
}

function loadContent(){
    let removeBtn = document.querySelectorAll('.item-remove');
    removeBtn.forEach((btn)=>{
        btn.addEventListener('click', buttonRemove);
    });

    let quantity = document.querySelectorAll('.cart-quantity');
    quantity.forEach((input)=>{
        input.addEventListener('change', qtychange);
    });
}

function buttonRemove(e){
    console.log("hello");
    e.currentTarget.parentNode.remove();
}

