/**
 * Script principal pour la gestion du menu déroulant mobile
 * et des interactions utilisateur
 */

document.addEventListener('DOMContentLoaded', function() {
    // Sélection des éléments du DOM
    const menuBouton = document.getElementById('menu-déroulant');
    const menuListe = document.getElementById('navigation-liste');
    
    // Vérifier si on est sur un appareil mobile
    const isMobile = window.innerWidth <= 480;
    
    // Fonction pour basculer le menu
    function toggleMenu() {
        menuBouton.classList.toggle('active');
        menuListe.classList.toggle('active');
    }
    
    // Ajouter l'événement de clic sur le bouton du menu
    if (menuBouton && menuListe) {
        menuBouton.addEventListener('click', toggleMenu);
        
        // Fermer le menu lorsqu'un lien est cliqué (sur mobile)
        const liensMenu = menuListe.querySelectorAll('a');
        liensMenu.forEach(lien => {
            lien.addEventListener('click', function() {
                if (isMobile) {
                    toggleMenu();
                }
            });
        });
    }
    
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
    
    // Fonction pour gérer le redimensionnement de la fenêtre
    function handleResize() {
        // Si on passe en mode bureau, s'assurer que le menu est visible
        if (window.innerWidth > 480) {
            menuListe.style.display = 'flex';
        } else if (!menuBouton.classList.contains('active')) {
            menuListe.style.display = 'none';
        }
    }
    
    // Écouter l'événement de redimensionnement
    window.addEventListener('resize', handleResize);
});
