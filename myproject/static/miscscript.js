//selecting the variable 
const cartIcon = document.querySelector('.cart')
const cartBox = document.querySelector('.cart-box')
const cross = document.querySelector(".cross")

cartIcon.addEventListener('click', () => {
    cartBox.classList.add('cart-active');
});


cross.addEventListener("click", () => {
    cartBox.classList.remove('cart-active');
});


document.addEventListener("DOMContentLoaded", loadFood());
// it will get the website dynamic 
function loadFood() {
    loadContent();
}

function loadContent() {
    //remove items from the cart
    let removeBtn = document.querySelectorAll('.item-remove');
    removeBtn.forEach((btn) => {
        btn.addEventListener('click', buttonRemove);
    });
    //for number didn't get below 1
    let quantity = document.querySelectorAll('#cart-quantity');
    quantity.forEach((input) => {
        input.addEventListener('change', qtyChange);
    });
    //for add items to cart
    let btnsValue = document.querySelectorAll('.btn');
    btnsValue.forEach((btn) => {
        btn.addEventListener('click', addCart);
    });

    updateTotal();
}


var itemList = [];
function qtyChange() {
    if (this.value < 1) {
        this.value = 1;
    }
    loadContent();
}

function buttonRemove(e) {
    let titleElement = e.currentTarget.parentElement.querySelector('.cart-food-title');
    let title = titleElement.innerText;
    title = title.toLowerCase();
    itemList = itemList.filter(el => {
        return el.title !== title;
    });
    console.log(itemList);
    e.currentTarget.parentNode.remove();
    let numbers = document.querySelector('.cart-value');
    numbers.style.display = "block";
    numbers.innerText = Number(numbers.innerText) - 1;
    loadContent();
}


function updateTotal() {
    let cartDetails = document.querySelectorAll('.cart-details');
    let totalValue = 0;
    cartDetails.forEach(product => {
        let price = product.querySelector('.value').innerHTML;
        let qty = product.querySelector('#cart-quantity').value;
        totalValue += (price * qty);
        product.querySelector('.iprice').innerHTML = (price * qty);
    })
    return (totalValue);
}


function addCart() {
    let numbers = document.querySelector('.cart-value');
    let mainClass = this.parentElement;
    let title = mainClass.querySelector('h1').innerText.toLowerCase();
    let price = parseInt(mainClass.querySelector('.price').innerText);
    let newProduct = { title, price };
    if (itemList.find((el) => el.title === newProduct.title)) {
        alert("Product already in the cart. Please check it.");
        return;
    } else {
        itemList.push(newProduct);
        numbers.style.display = "block";
        numbers.innerText = Number(numbers.innerText) + 1;
    }
    let newProductElement = createCartProduct(title, price);
    let element = document.createElement('div');
    element.innerHTML = newProductElement;
    let cartBasket = document.querySelector('.cart-card');
    cartBasket.append(element);
    loadContent();
}


function createCartProduct(title, price) {
    return `
    <div class="cart-card">
            <div class="cart-details">
                <div class="cart-food-title">
                    ${title}
                </div>
                <div class="price-box">
                    <div class="value" style="display:none">${price}</div>
                    <div class="total-price">Rs.<span class="iprice">${price}</div>
                </div>
                <input type="number" value="1" id="cart-quantity">
            </div>
            <div class="item-remove">
                <i class="fa-solid fa-trash"></i>
            </div>
        </div>`;
}


let buyBtn = document.querySelector('.buy-btn');
buyBtn.addEventListener('click', () => {
    if (itemList.length === 0) {
        alert("please add items in cart and place the order");
        return;
    }
    else {
        sessionStorage.setItem("details", JSON.stringify(itemList));
        window.location.href = "checkout.js";
    }
})