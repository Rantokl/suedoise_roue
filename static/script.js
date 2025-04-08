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

    

const sliderX = document.getElementById('slider-x');
const sliderY = document.getElementById('slider-y');
const valueX = document.getElementById('value-x');
const valueY = document.getElementById('value-y');


async function move(direction) {
    let data = {};

    switch (direction) {
        case 'up':
            data = { axis: 'move', value: 'avant' };
            break;
        case 'down':
            data = { axis: 'move', value: 'arriere' };
            break;
        case 'left':
            data = { axis: 'move', value: 'gauche' };
            break;
        case 'right':
            data = { axis: 'move', value: 'droite' };
            break;
        case 'stop':
            data = { axis: 'move', value: 'stop' };
            break;
        default:
            return;
    }

    await sendData('/direction', data);
}

// sliderY.addEventListener('input', async (e) => {
//     //Vérification
//     valueY.textContent = sliderY.value;
//     const data = { axis: 'y', value: sliderY.value };
//     await sendData('/send', data);  // On envoie un objet, pas juste la valeur
// });

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

async function fetchSpeed() {
    try {
        valueY.textContent = sliderY.value;
        const data = { axis: 'y', value: sliderY.value };
        await sendData('/send', data); 
    }
    catch (err) {
        console.error("Erreur de récupération :", err);
    }
}
setInterval(fetchSpeed, 1000);

});



