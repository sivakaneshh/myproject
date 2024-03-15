let removeBtn = document.querySelectorAll('.remove');
removeBtn.forEach((btn)=>{
    btn.addEventListener('click',trash);
});
function trash(e){
    e.currentTarget.parentElement.remove();
}