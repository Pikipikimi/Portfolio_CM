/**
 * Script principal pour la gestion du menu déroulant mobile
 * et des interactions utilisateur
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // Vérifier si on est sur un appareil mobile
    const isMobile = window.innerWidth <= 480;
    
    // Mettre à jour la classe active sur la navigation
    const currentPage = window.location.pathname.split('/').pop() || 'TEST - Index.html';
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        const linkHref = link.getAttribute('href');
        // Vérifier si le lien correspond à la page actuelle
        if (linkHref === currentPage || 
            (currentPage === '' && linkHref === 'TEST - Index.html') ||
            (currentPage === 'index.html' && linkHref === 'TEST - Index.html')) {
            link.classList.add('active');
        }
    });
    
    // Ajouter un effet de défilement fluide pour les ancres
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 20,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Écouter l'événement de redimensionnement
    window.addEventListener('resize', handleResize);
});
