document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const productsContainer = document.getElementById('products-container');
    const productDetailsContainer = document.createElement('div'); // Создаем контейнер для информации о продукте
    productDetailsContainer.className = 'product-details'; // Добавляем класс для стилей

    searchInput.addEventListener('input', function() {
        const searchTerm = searchInput.value.trim().toLowerCase();
        filterProducts(searchTerm);
    });

    fetch('http://localhost:8000/all_products')
        .then(response => response.json())
        .then(data => displayProducts(data))
        .catch(error => console.error('Error fetching products:', error));

    function displayProducts(products) {
        productsContainer.innerHTML = '';

        Object.entries(products).forEach(([productName, productDetails]) => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';
            productCard.innerHTML = `
                <h3>${productName}</h3>
                <p>Вага порції: ${productDetails['Вага порції']} g</p>
                <p>Калорійність: ${productDetails['Калорійність']} kcal</p>
                <div class="product-details">
                    <p>Жири: ${productDetails['Жири']} g</p>
                    <p>Білки: ${productDetails['Білки']} g</p>
                    <p>Вуглеводи: ${productDetails['Вуглеводи']} g</p>
                    <p>Цукор: ${productDetails['Цукор']} g</p>
                    <p>Сіль: ${productDetails['Сіль']} g</p>
                    <p>Загальна інформація: ${productDetails['Загальна інформація']}</p>
                </div>
            `;
            productCard.addEventListener('click', function() {
                // Получаем имя продукта из текста заголовка
                const productName = productCard.querySelector('h3').textContent.trim();
                // Формируем URL для запроса на сервер
                const productURL = `http://localhost:8000/products/${encodeURIComponent(productName)}`;
                // Отправляем запрос на сервер для получения информации о продукте
                fetch(productURL)
                    .then(response => response.json())
                    .then(productData => {
                        // Показываем информацию о продукте на странице
                        displayProductDetails(productData);
                    })
                    .catch(error => console.error('Error fetching product details:', error));
            });
            productsContainer.appendChild(productCard);
        });
    }

    function filterProducts(searchTerm) {
        const productCards = document.querySelectorAll('.product-card');

        productCards.forEach(card => {
            const productName = card.querySelector('h3').textContent.trim().toLowerCase();
            if (productName.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    function displayProductDetails(productDetails) {
        // Очищаем контейнер с информацией о продукте перед добавлением новой информации
        productDetailsContainer.innerHTML = '';

        Object.entries(productDetails).forEach(([key, value]) => {
            const detailParagraph = document.createElement('p');
            detailParagraph.textContent = `${key}: ${value}`;
            productDetailsContainer.appendChild(detailParagraph);
        });

        // Добавляем контейнер с информацией о продукте на страницу
        productsContainer.appendChild(productDetailsContainer);
    }
});
