document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu functionality
    const btn = document.querySelector('.mobile-menu-button');
    const menu = document.querySelector('.mobile-menu');

    btn.addEventListener('click', () => {
        menu.classList.toggle('hidden');
    });
}); 