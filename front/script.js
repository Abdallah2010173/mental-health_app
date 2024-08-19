let cart = [];
let cartTotal = 0;

function addToCart(productName, productPrice) {
    cart.push({ name: productName, price: productPrice });
    cartTotal += productPrice;
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cartItems');
    const cartTotalElement = document.getElementById('cartTotal');

    // Clear previous cart items
    cartItems.innerHTML = '';

    // Add current cart items
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - SAR ${item.price.toFixed(2)}`;
        cartItems.appendChild(li);
    });

    // Update total
    cartTotalElement.textContent = `Total: SAR ${cartTotal.toFixed(2)}`;
}

// Form submission handler (example)
document.getElementById('contactForm')?.addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Thank you for your message!');
});
