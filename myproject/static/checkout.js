document.addEventListener("DOMContentLoaded", function() {
    let orderList = JSON.parse(sessionStorage.getItem('details'));
    console.log(orderList);
    var totalPrice = 0;
    if (orderList) {
        for (let i = 0; i < orderList.length; i++) {
            let title = orderList[i].title;
            let price = parseFloat(orderList[i].price); // Ensure price is parsed as a float
            totalPrice += price;
            let num = i + 1;
            let newElement = addFile(num, title, price);
            let el = document.createElement('div');
            el.innerHTML = newElement;
            let listBasket = document.querySelector('.details');
            listBasket.append(el);
        }
    }
    console.log(totalPrice);
    let totalAmt = document.querySelector('.total-amt');
    if (totalAmt) {
        totalAmt.innerText = "Rs. " + totalPrice.toFixed(2); // Ensure total price is displayed with 2 decimal places
    }
});

function addFile(num, title, price) {
    return `
        <div class="detail-value">
            <span>
                <p class="serial-no">${num}</p>
                <h1>${title}</h1>
            </span>
            <div class="price">Rs. ${price.toFixed(2)}</div> <!-- Ensure price is displayed with 2 decimal places -->
        </div>`;
}
