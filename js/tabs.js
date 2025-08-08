document.addEventListener('DOMContentLoaded', () => {
    
    // --- Mobile Navigation Toggle ---
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (mobileNavToggle) {
        mobileNavToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            mobileNavToggle.classList.toggle('is-active');
        });
    }

    // --- Main Contact Form Simulation ---
    const contactForm = document.querySelector('#contact-form');
    if(contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Thank you for your message! This is a demo. In a real website, this would be sent to an administrator.');
            contactForm.reset();
        });
    }

    // --- Admin Login Form Simulation ---
    const adminLoginForm = document.querySelector('#admin-login-form');
    if (adminLoginForm) {
        const messageEl = document.querySelector('#login-message');

        adminLoginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const username = adminLoginForm.username.value;
            const password = adminLoginForm.password.value;

            messageEl.textContent = '';
            messageEl.className = 'message';

            if (username === 'admin' && password === '123456') {
                messageEl.textContent = 'Login Successful! Redirecting...';
                messageEl.classList.add('success');
                // In a real application, you would redirect to the admin dashboard.
                // For this demo, we'll just show the message.
                // window.location.href = '/admin/dashboard.html';
                alert('Login successful! You would now be redirected to the admin dashboard.');
            } else {
                messageEl.textContent = 'Invalid username or password.';
                messageEl.classList.add('error');
            }
        });
    }

});