document.addEventListener("DOMContentLoaded", function() {
    // Adiciona classe ao body para ativar as animações do CSS com segurança
    document.body.classList.add('js-enabled');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    const elements = document.querySelectorAll('.fade-in');
    elements.forEach((el) => observer.observe(el));
});