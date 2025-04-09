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

    


const sliderY = document.getElementById('slider-y');

const valueY = document.getElementById('value-y');


async function moveWithSlider(direction) {
    const speed = parseInt(sliderY.value); // récupère la vitesse actuelle
    valueY.textContent = speed; // met à jour l'affichage (au cas où)
    const data = { axis: 'move', value: direction, speed: speed };
    await sendData('/send', data);
}

// Ajout des écouteurs sur chaque bouton
document.getElementById('btn-up').addEventListener('click', () => moveWithSlider('avant'));
document.getElementById('btn-down').addEventListener('click', () => moveWithSlider('arriere'));
document.getElementById('btn-left').addEventListener('click', () => moveWithSlider('gauche'));
document.getElementById('btn-right').addEventListener('click', () => moveWithSlider('droite'));
document.getElementById('btn-stop').addEventListener('click', async () => {
    await sendData('/send', { axis: 'move', value: 'stop' });
});

sliderY.addEventListener('input', async (e) => {
    //Vérification
    valueY.textContent = sliderY.value;
    
     // On envoie un objet, pas juste la valeur
});

async function fetchDistances() {
    try {
        const response = await fetch('/distances');
        const data = await response.json();
        document.getElementById('left').textContent = `Gauche: ${data.Gauche} cm`;
        document.getElementById('right').textContent = `Droite: ${data.Droite} cm`;
        document.getElementById('back').textContent = `Arrière: ${data.Arrière} cm`;
    } catch (err) {
        console.error("Erreur de récupération :", err);
    }
}


// Rafraîchit toutes les 1 sec
setInterval(fetchDistances, 1000);



});



