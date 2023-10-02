const navBurger = document.querySelector(".burger");
const navLinks = document.querySelector(".nav-links");

function navActiveToggler() {
    navLinks.classList.toggle("nav-links__active");
}

navBurger.addEventListener("click", navActiveToggler);   


// delete product from card
function deleteProduct(img)
{
    
    const parentProduct = img.closest('.added-product');
    const cartNumber = document.querySelector('.counter');
    const productList = document.querySelector('.added-products-list');
    
    cartNumber.textContent = parseInt(cartNumber.textContent) - 1;
    
    parentProduct.style.display = 'none';
    localStorage.setItem("Quantity",cartNumber.textContent);
    localStorage.setItem("cartlist",productList.innerHTML);
    location.reload();
}

document.querySelector(".counter").textContent = localStorage.getItem("Quantity");
document.querySelector(".added-products-list").innerHTML = localStorage.getItem("cartlist");

// Adding products in the cart
function getInfo(imgSrc,productPrice)
{
    const cartNumber = document.querySelector('.counter');
    const productList = document.querySelector('.added-products-list');
    let imageSrc = `../../static/img/products/${imgSrc}`


    cartNumber.textContent =  parseInt(cartNumber.textContent) + 1; 
    
    let newProduct = `
        <div class="added-product">
                    <div class="delete-product">
                        <img src="../../static/img/icons/trash-bin.png" onclick="deleteProduct(this)" alt="trash can icon"/>
                    </div>
                    <img src="${imageSrc}"  alt="product icon" />
                    <span>${productPrice}₾</span>
                </div>
    `;

    productList.innerHTML += newProduct;
    localStorage.setItem("cartlist",productList.innerHTML);

    var addHref = document.getElementById("placeorder");
    
    if (cartNumber.textContent !== "0") {
        addHref.href = "/cart";   
    }
  localStorage.setItem("Quantity",cartNumber.textContent);
}

const cartNumber = document.querySelector('.counter');

if (cartNumber.textContent == "") {
    cartNumber.textContent = "0";
    localStorage.setItem("Quantity",cartNumber.textContent);
}

document.querySelector(".counter").textContent = localStorage.getItem("Quantity");
document.querySelector(".added-products-list").innerHTML = localStorage.getItem("cartlist");

var addHref = document.getElementById("placeorder");
if (cartNumber.textContent !== "0") {
    addHref.href = "/cart";   
}
