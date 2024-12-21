document.addEventListener("DOMContentLoaded", function () {
    const character = document.getElementById("character"); // Personaje
    const container = document.querySelector(".game-container"); // Contenedor del juego
    const map = document.querySelector(".map"); // Contenedor del mapa

    let posX = 225; // Posición inicial horizontal del personaje
    let posY = 225; // Posición inicial vertical del personaje
    const step = 10; // Distancia por pulsación

    const obstacleCount = 20; // Número de obstáculos a generar
    const obstacles = []; // Array para almacenar obstáculos

    // Genera obstáculos en posiciones aleatorias
    function generateObstacles() {
        for (let i = 0; i < obstacleCount; i++) {
            const obstacle = document.createElement("div");
            obstacle.classList.add("obstacle");

            const randomX = Math.floor(Math.random() * (map.clientWidth - 50)); // Posición aleatoria X
            const randomY = Math.floor(Math.random() * (map.clientHeight - 50)); // Posición aleatoria Y

            obstacle.style.left = `${randomX}px`;
            obstacle.style.top = `${randomY}px`;

            map.appendChild(obstacle);
            obstacles.push(obstacle); // Guarda el obstáculo en el array
        }
    }

    // Verifica si el personaje choca con algún obstáculo
    function checkCollision() {
        obstacles.forEach((obstacle) => {
            const rect1 = character.getBoundingClientRect();
            const rect2 = obstacle.getBoundingClientRect();

            if (
                rect1.left < rect2.right &&
                rect1.right > rect2.left &&
                rect1.top < rect2.bottom &&
                rect1.bottom > rect2.top
            ) {
                alert("¡Colisión detectada!"); // Acciones en caso de colisión
            }
        });
    }

    // Llama a la función para generar obstáculos
    generateObstacles();

    // Manejo del teclado para mover el personaje
    document.addEventListener("keydown", function (event) {
        switch (event.key) {
            case "ArrowUp": // Flecha arriba
            case "w":
            case "W":
                if (posY > 0) posY -= step;
                break;
            case "ArrowDown": // Flecha abajo
            case "s":
            case "S":
                if (posY < map.clientHeight - character.clientHeight) posY += step;
                break;
            case "ArrowLeft": // Flecha izquierda
            case "a":
            case "A":
                if (posX > 0) posX -= step;
                break;
            case "ArrowRight": // Flecha derecha
            case "d":
            case "D":
                if (posX < map.clientWidth - character.clientWidth) posX += step;
                break;
        }

        // Actualiza la posición del personaje
        character.style.top = posY + "px";
        character.style.left = posX + "px";

        // Desplaza el contenedor horizontalmente cuando el personaje se mueve
        container.scrollLeft = posX - container.clientWidth / 2;

        // Desplaza el contenedor verticalmente cuando el personaje se mueve
        container.scrollTop = posY - container.clientHeight / 2;

        // Verifica colisiones
        checkCollision();
    });
});
