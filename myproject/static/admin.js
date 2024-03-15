let cut = document.querySelectorAll('.btns');
cut.forEach((btn)=>{
    btn.addEventListener('click',removeValue);
})
function removeValue(e){
    let parentValue = e.currentTarget.parentElement.remove();
    console.log(parentValue)
}