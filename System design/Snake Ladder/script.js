const board = document.querySelector('.board');
const player = document.getElementById('player');
const rollBtn = document.getElementById('rollBtn');

const snakesAndLadders = {
    16: 6, 47: 26, 49: 11, 56: 53, 62: 19,
    64: 60, 87: 24, 93: 73, 95: 75, 98: 78
};

const totalCells = 100;

let currentPlayerPosition = 1;

function createBoard() {
    for (let i = 1; i <= totalCells; i++) {
        const cell = document.createElement('div');
        cell.className = 'cell';
        cell.id = i;
        cell.textContent = i;
        board.appendChild(cell);
    }
}

function updatePlayerPosition() {
    const currentCell = document.getElementById(currentPlayerPosition);
    const { top, left } = currentCell.getBoundingClientRect();
    player.style.top = `${top}px`;
    player.style.left = `${left}px`;
}

function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

function movePlayer(steps) {
    currentPlayerPosition += steps;

    if (snakesAndLadders[currentPlayerPosition]) {
        currentPlayerPosition = snakesAndLadders[currentPlayerPosition];
    }

    if (currentPlayerPosition > totalCells) {
        currentPlayerPosition = totalCells - (currentPlayerPosition - totalCells);
    }

    updatePlayerPosition();
}

rollBtn.addEventListener('click', () => {
    const steps = rollDice();
    alert(`Player rolled: ${steps}`);
    movePlayer(steps);
});

createBoard();
updatePlayerPosition();
