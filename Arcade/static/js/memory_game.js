document.addEventListener("DOMContentLoaded", function () {
    const gridContainer = document.getElementById("memory-grid");
    const startButton = document.getElementById("start-game");
    const levelDisplay = document.getElementById("level");
    const scoreDisplay = document.getElementById("score");
    const turnStatus = document.getElementById("turn-status");

    let gridSize = 3; // Tamaño inicial de la cuadrícula
    let pattern = []; // Secuencia a seguir
    let playerPattern = []; // Entrada del jugador
    let level = 1;
    let score = 0;
    let isPlayerTurn = false;

    // Colores para el patrón
    const patternColors = ["#FF5733", "#33FF57", "#5733FF", "#FFC300", "#33FFF2"]; // Colores para el patrón
    const playerColor = "#044706"; // Color fijo para los clics del jugador

    // Generar cuadrícula
    function generateGrid(size) {
        gridContainer.style.gridTemplateColumns = `repeat(${size}, 1fr)`;
        gridContainer.innerHTML = ""; // Limpiar la cuadrícula
        for (let i = 0; i < size * size; i++) {
            const square = document.createElement("div");
            square.classList.add("grid-square");
            square.dataset.index = i;
            gridContainer.appendChild(square);
        }
    }

    // Mostrar el patrón
    function showPattern() {
        let index = 0;
        isPlayerTurn = false;
        turnStatus.textContent = "Memoriza el patrón...";
        const squares = document.querySelectorAll(".grid-square");

        const interval = setInterval(() => {
            if (index > 0) {
                squares[pattern[index - 1]].classList.remove("active");
                squares[pattern[index - 1]].style.backgroundColor = ""; // Quitar color del cuadro
            }
            if (index < pattern.length) {
                const colorIndex = index % patternColors.length; // Ciclar colores del patrón
                squares[pattern[index]].classList.add("active");
                squares[pattern[index]].style.backgroundColor = patternColors[colorIndex];
                index++;
            } else {
                clearInterval(interval);
                squares[pattern[index - 1]].classList.remove("active");
                squares[pattern[index - 1]].style.backgroundColor = ""; // Quitar color del último cuadro
                isPlayerTurn = true;
                turnStatus.textContent = "Tu turno";
            }
        }, 600 - level * 50); // Velocidad aumenta con el nivel
    }

    // Generar nuevo patrón
    function generatePattern() {
        const squaresCount = gridSize * gridSize;
        pattern.push(Math.floor(Math.random() * squaresCount));
    }

    // Verificar entrada del jugador
    function checkPlayerInput() {
        for (let i = 0; i < playerPattern.length; i++) {
            if (playerPattern[i] !== pattern[i]) {
                alert(`¡Perdiste! Llegaste al nivel ${level} con un puntaje de ${score}.`);
                resetGame();
                return;
            }
        }

        // Si el jugador termina el patrón correctamente
        if (playerPattern.length === pattern.length) {
            level++;
            score += level * 10; // Incrementar puntaje con el nivel
            levelDisplay.textContent = level;
            scoreDisplay.textContent = score;

            // Aumentar tamaño de cuadrícula en niveles clave
            if (level % 3 === 0) {
                gridSize++;
                generateGrid(gridSize);
            }

            playerPattern = [];
            generatePattern();
            setTimeout(showPattern, 1000); // Mostrar el nuevo patrón
        }
    }

    // Resetear el juego
    function resetGame() {
        level = 1;
        score = 0;
        gridSize = 3;
        pattern = [];
        playerPattern = [];
        levelDisplay.textContent = level;
        scoreDisplay.textContent = score;
        generateGrid(gridSize);
        turnStatus.textContent = "Esperando...";
    }

    // Iniciar el juego
    startButton.addEventListener("click", function () {
        resetGame();
        generatePattern();
        showPattern();
    });

    // Manejar clics del jugador
    gridContainer.addEventListener("click", function (e) {
        if (!isPlayerTurn) return;
        const clickedSquare = e.target;
        if (clickedSquare.classList.contains("grid-square")) {
            const index = parseInt(clickedSquare.dataset.index);
            playerPattern.push(index);
            clickedSquare.style.backgroundColor = playerColor; // Aplicar color fijo para el jugador

            setTimeout(() => {
                clickedSquare.style.backgroundColor = ""; // Volver al color original
                checkPlayerInput();
            }, 300);
        }
    });

    // Generar cuadrícula inicial
    generateGrid(gridSize);
});
