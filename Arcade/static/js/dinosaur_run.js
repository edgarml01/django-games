document.addEventListener("DOMContentLoaded", function () {
    const dino = document.getElementById("dino");
    const cactus = document.getElementById("cactus");
    const scoreElement = document.getElementById("score");
    const timeElement = document.getElementById("time");

    let score = 0;
    let isJumping = false;
    let timePlayed = 0;

    // Función para iniciar el contador de tiempo
    function startTimer() {
        setInterval(() => {
            timePlayed++;
            timeElement.textContent = timePlayed;
        }, 1000); // Incrementar cada segundo
    }

    // Función para que el dinosaurio salte
    function jump() {
        if (isJumping) return;
        isJumping = true;

        let position = 0;
        const jumpInterval = setInterval(() => {
            if (position >= 150) {
                clearInterval(jumpInterval);
                const fallInterval = setInterval(() => {
                    if (position <= 0) {
                        clearInterval(fallInterval);
                        isJumping = false;
                    }
                    position -= 10;
                    dino.style.bottom = `${position}px`;
                }, 20);
            }
            position += 10;
            dino.style.bottom = `${position}px`;
        }, 20);
    }

    // Función para mover el cactus
    function moveCactus() {
        let cactusPosition = 800;

        const moveInterval = setInterval(() => {
            cactusPosition -= 10;
            cactus.style.right = `${800 - cactusPosition}px`;

            // Detectar colisión
            if (cactusPosition < 100 && cactusPosition > 50 && parseInt(dino.style.bottom) < 50) {
                clearInterval(moveInterval);
                alert("¡Juego terminado! Tu puntaje es: " + score + " en " + timePlayed + " segundos.");
                window.location.reload();
            }

            // Reiniciar cactus
            if (cactusPosition < -50) {
                cactusPosition = 800;
                score++;
                scoreElement.textContent = score;
            }
        }, 20);
    }

    // Detectar tecla de salto
    document.addEventListener("keydown", function (event) {
        if (event.code === "Space" || event.code === "ArrowUp" || event.code === "KeyW") {
            jump();
        }
    });

    // Iniciar el juego
    startTimer();
    moveCactus();
});
