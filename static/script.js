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


let intervalId = null;

    function startSending(direction) {
        const sendCommand = () => {
            const speed = sliderY.value;
            valueY.textContent = speed;
            const data = { axis: 'move', value: direction, speed: speed };
            sendData('/send', data);
        };

        sendCommand(); // envoie immédiat
        intervalId = setInterval(sendCommand, 200); // continue tant qu'on appuie
    }

    function stopSending() {
        if (intervalId) {
            clearInterval(intervalId);
            intervalId = null;
            
        }
    }

    // Ajoute les listeners sur chaque bouton
    function setupHoldButton(buttonId, direction) {
        const btn = document.getElementById(buttonId);
        btn.addEventListener('mousedown', () => startSending(direction));
        btn.addEventListener('mouseup', stopSending);
        btn.addEventListener('mouseleave', stopSending);

        // Pour mobile (touch)
        btn.addEventListener('touchstart', (e) => {
            e.preventDefault(); // empêche le scroll
            startSending(direction);
        }, { passive: false });
        btn.addEventListener('touchend', stopSending);
    }

    setupHoldButton('btn-up', 'avant');
    setupHoldButton('btn-down', 'arriere');
    setupHoldButton('btn-left', 'gauche');
    setupHoldButton('btn-right', 'droite');

    // Bouton STOP (juste un clic)
    document.getElementById('btn-stop').addEventListener('click', async () => {
        stopSending();
        await sendData('/send', { axis: 'move', value: 'stop',speed:'0' });
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



