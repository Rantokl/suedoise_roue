document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('messageForm');
    const input = document.getElementById('messageInput');
    const responseText = document.getElementById('responseText');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();  // Empêche le rechargement de la page

        const message = input.value.trim();
        if (!message) return;

        try {
            const response = await fetch('/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            const result = await response.json();
            console.log("Réponse du serveur :", result);

            responseText.innerHTML = `Message reçu : <strong>${result.message}</strong>`;
            responseText.style.display = 'block';
            input.value = '';
        } catch (error) {
            console.error("Erreur lors de l'envoi du message :", error);
        }
    });
});
