document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('messageForm');
    const input = document.getElementById('messageInput');
    const responseText = document.getElementById('responseText');
    async function sendData(url, data) {
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: data })
            });
    
            const result = await response.json();
            console.log("Réponse du serveur :", result);
            return result; 
        } catch (error) {
            console.error("Erreur lors de l'envoi des données :", error);
        }
    }

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const message = input.value.trim();
        if (!message) return;

        await sendData('/send',message)
    });

const sliderX = document.getElementById('slider-x');
const sliderY = document.getElementById('slider-y');
const valueX = document.getElementById('value-x');
const valueY = document.getElementById('value-y');

sliderX.addEventListener('input', async (e) => {
    valueX.textContent = sliderX.value;
    // tu peux envoyer la valeur ici si besoin
    const data = { axis: 'x', value: sliderX.value };
    await sendData('/send', data);
});

sliderY.addEventListener('input', async (e) => {
    //Vérification
    valueY.textContent = sliderY.value;
    const data = { axis: 'y', value: sliderY.value };
    await sendData('/send', data);  // On envoie un objet, pas juste la valeur
});
});



