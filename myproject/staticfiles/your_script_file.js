// Function to update cart items dynamically on the checkout page
function updateCartItemsOnCheckout() {
    const cartItemsDiv = document.getElementById("cart-items");
    cartItemsDiv.innerHTML = ""; // Clear existing items

    let totalAmount = 0;

    itemList.forEach((item, index) => {
        const itemDiv = document.createElement("div");
        itemDiv.className = "cart-card";

        itemDiv.innerHTML = `
            <div class="cart-details">
                <div class="cart-food-title">
                    ${item.title}
                </div>
                <div class="price-box">
                    <div class="total-price">Rs.<span class="iprice">${item.price}</div>
                </div>
            </div>
            <input type="number" value="${item.quantity}" id="cart-quantity-${index}" disabled>
            <div class="item-remove" data-index="${index}">
                <i class="fa-solid fa-trash"></i>
            </div>
        `;

        cartItemsDiv.appendChild(itemDiv);

        totalAmount += item.price;
    });

    // Update total amount
    document.getElementById("total-amount").textContent = `Rs.${totalAmount}`;
}

// Call the function to initially populate cart items and total on the checkout page
updateCartItemsOnCheckout();
