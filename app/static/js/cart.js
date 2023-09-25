var amount = document.querySelector(".counter").innerHTML;
var addHref = document.getElementById("cartIcon");

if (amount !== null) {
  addHref.href = "../pages/cart.html";
  document.getElementById("amountNum").innerText = amount;
  let num1 = document.getElementById("amountNum").innerHTML;
  let num2 = document.getElementById("priceNum").innerHTML;
  let calculate = num1 * num2;
  document.getElementById("sum").innerHTML = calculate;
  }

let btn2 = document.getElementById('remove')
var counters = document.querySelector(".counter");


  btn2.addEventListener("click", btn2remove);
  function btn2remove () {
    counters.textContent = "0";
    document.getElementById("amountNum").textContent = "0";
    document.getElementById("priceNum").textContent = "0";
    document.getElementById("sum").textContent = "0";
    document.getElementById('cartImg').remove();
    var span_Text = document.querySelector(".counter").innerHTML;
    localStorage.setItem("Quantity",span_Text)
}

document.querySelector(".counter").innerHTML = localStorage.getItem("Quantity");

