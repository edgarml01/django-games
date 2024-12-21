document.addEventListener("DOMContentLoaded", () => {
    const board = document.getElementById("game-board");
    const scoreElement = document.getElementById("score");
    const levelElement = document.getElementById("level");
    const timeElement = document.getElementById("time");
    const startButton = document.getElementById("start-button");
    const container = document.getElementById("game-container");
    const saveScoreUrl = container.getAttribute("data-save-url");

    const boardSize = 20;
    const snake = [{ x: 10, y: 10 }];
    let food = { x: 5, y: 5 };
    let direction = { x: 0, y: 0 };
    let score = 0;
    let level = 1;
    let gameInterval;
    let startTime;

    function initializeGame() {
        resetGame();
        startTime = new Date();
        drawBoard();
        placeFood();
        gameInterval = setInterval(updateGame, 200 - (level - 1) * 20);
        document.addEventListener("keydown", changeDirection);
    }

    function resetGame() {
        clearInterval(gameInterval);
        snake.length = 1;
        snake[0] = { x: 10, y: 10 };
        direction = { x: 0, y: 0 };
        score = 0;
        level = 1;
        updateUI();
    }

    function drawBoard() {
        board.innerHTML = "";
        snake.forEach((segment) => {
            const segmentDiv = document.createElement("div");
            segmentDiv.style.gridRowStart = segment.y;
            segmentDiv.style.gridColumnStart = segment.x;
            segmentDiv.classList.add("snake");
            board.appendChild(segmentDiv);
        });

        const foodDiv = document.createElement("div");
        foodDiv.style.gridRowStart = food.y;
        foodDiv.style.gridColumnStart = food.x;
        foodDiv.classList.add("food");
        board.appendChild(foodDiv);
    }

    function placeFood() {
        do {
            food.x = Math.floor(Math.random() * boardSize) + 1;
            food.y = Math.floor(Math.random() * boardSize) + 1;
        } while (snake.some((segment) => segment.x === food.x && segment.y === food.y));
    }

    function updateGame() {
        if (direction.x === 0 && direction.y === 0) {
            return;
        }

        const head = { x: snake[0].x + direction.x, y: snake[0].y + direction.y };

        if (
            head.x < 1 ||
            head.x > boardSize ||
            head.y < 1 ||
            head.y > boardSize ||
            snake.some((segment) => segment.x === head.x && segment.y === head.y)
        ) {
            endGame();
            return;
        }

        if (head.x === food.x && head.y === food.y) {
            snake.unshift(head);
            score++;
            if (score % 5 === 0) level++;
            updateUI();
            placeFood();
        } else {
            snake.pop();
            snake.unshift(head);
        }

        drawBoard();
    }

    function changeDirection(event) {
        switch (event.key) {
            case "ArrowUp":
            case "w":
                if (direction.y === 0) direction = { x: 0, y: -1 };
                break;
            case "ArrowDown":
            case "s":
                if (direction.y === 0) direction = { x: 0, y: 1 };
                break;
            case "ArrowLeft":
            case "a":
                if (direction.x === 0) direction = { x: -1, y: 0 };
                break;
            case "ArrowRight":
            case "d":
                if (direction.x === 0) direction = { x: 1, y: 0 };
                break;
        }
    }

    function updateUI() {
        scoreElement.textContent = score;
        levelElement.textContent = level;
        const currentTime = Math.floor((new Date() - startTime) / 1000);
        timeElement.textContent = currentTime || 0;
    }

    function endGame() {
        clearInterval(gameInterval);
        alert(`Game Over! Tu puntuación: ${score}, Nivel alcanzado: ${level}`);
        saveGameData(score, level, Math.floor((new Date() - startTime) / 1000));
        resetGame();
    }

    function saveGameData(score, level, time) {
        fetch(saveScoreUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({ puntaje: score, nivel: level, tiempo: time }),
        });
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(";").shift();
    }

    startButton.addEventListener("click", initializeGame);
});
