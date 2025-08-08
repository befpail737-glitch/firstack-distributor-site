document.addEventListener('DOMContentLoaded', () => {
    const tabContainer = document.querySelector('.product-tabs');
    if (!tabContainer) return;

    const tabLinks = tabContainer.querySelectorAll('.tab-link');
    const tabContents = tabContainer.querySelectorAll('.tab-content');

    tabLinks.forEach(link => {
        link.addEventListener('click', () => {
            const tabId = link.getAttribute('data-tab');

            // Update active state on links
            tabLinks.forEach(item => item.classList.remove('active'));
            link.classList.add('active');

            // Show the correct content
            tabContents.forEach(content => {
                if (content.id === tabId) {
                    content.classList.add('active');
                } else {
                    content.classList.remove('active');
                }
            });
        });
    });
});