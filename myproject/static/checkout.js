let orderList = JSON.parse(sessionStorage.getItem('details'));
console.log(orderList);
var totalPrice = 0
for (i=0;i<orderList.length;i++){
    let title = orderList[i].title;
    let price = orderList[i].price;
    totalPrice +=price;
    let num = i+1;
    let newElement = addFile(num,title,price);
    let el = document.createElement('div');
    el.innerHTML = newElement;
    let listBasket = document.querySelector('.details');
    listBasket.append(el);
}
console.log(totalPrice);
let totalAmt = document.querySelector('.total-amt');
totalAmt.innerText ="Rs."+totalPrice;

function addFile(num,title,price){
    return`
    <div class="detail-value">
                <span>
                    <p class="serial-no">${num}</p>
                    <h1>${title}</h1>
                </span>

                <div class="price">Rs.${price}</div>
            </div> `;
}