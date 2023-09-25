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
    
    cartNumber.textContent = parseInt(cartNumber.textContent) - 1;
    
    parentProduct.style.display = 'none';
}

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

}


    

