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

function loadFood() {
    loadContent();
}

function loadContent() {
    let removeBtn = document.querySelectorAll('.item-remove');
    removeBtn.forEach((btn) => {
        btn.addEventListener('click', buttonRemove);
    });

    let quantity = document.querySelectorAll('#cart-quantity');
    quantity.forEach((input) => {
        input.addEventListener('change', function() {
            if(this.value < 1){
                this.value = 1;
            }
        });
    });


    let btnsValue = document.querySelectorAll('.btn');
    btnsValue.forEach((btn) => {
        btn.addEventListener('click', addCart);
    });
}
var itemList = [];
function buttonRemove(e) {

    let index = parseInt(e.currentTarget.dataset.index); // Get the index of the item to be removed
    itemList.splice(index, 1); // Remove the item from the itemList array
    console.log(itemList); // Log the updated itemList
    e.currentTarget.parentNode.remove(); // Remove the item's HTML element from the cart
    let numbers = document.querySelector('.cart-value');
    numbers.style.display = "block";
    numbers.innerText = Number(numbers.innerText) - 1; // Update the cart item count
    loadContent(); // Update the cart content (if needed)
}
// function rItem(array, property, value){
//         return array.filter(function(item){
//             return item[property] !== value;
//         });
//     }
    


function addCart() {
    let numbers = document.querySelector('.cart-value');
    let mainClass = this.parentElement;
    let title = mainClass.querySelector('h1').innerText;
    let price = mainClass.querySelector('.price').innerText;
    let newProduct = { title, price }; // Create a new item object
    if (itemList.find((el) => el.title === newProduct.title)) {
        alert("Product already in the cart. Please check it.");
        return;
    } else {
        itemList.push(newProduct); // Add the new item to itemList
        numbers.style.display = "block";
        numbers.innerText = Number(numbers.innerText) + 1; // Update the cart item count
    }
    let newProductElement = createCartProduct(title, price); // Create HTML for the new item
    let element = document.createElement('div');
    element.innerHTML = newProductElement;
    let cartBasket = document.querySelector('.cart-card');
    cartBasket.append(element); // Append the new item's HTML to the cart
    loadContent(); // Update the cart content (if needed)
    console.log(itemList); // Log the updated itemList
}
function createCartProduct(title, price) {
    return `
    <div class="cart-card">
            <div class="cart-details">
                <div class="cart-food-title">
                    ${title}
                </div>
                <div class="price-box">
                    <div class="total-price">Rs.<span class="iprice">${price}</div>
                </div>
                <input type="number" value="1" id="cart-quantity">
            </div>
            <div class="item-remove">
                <i class="fa-solid fa-trash"></i>
            </div>
        </div>`;
}
