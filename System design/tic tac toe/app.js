const board = document.getElementById('board');
const status = document.getElementById('status');

let currentPlayer = 'X';
let gameBoard = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;

function handleCellClick(e) {
    const cell = e.target;
    const cellIndex = cell.getAttribute('data-cell-index');

    if (gameBoard[cellIndex] !== '' || !gameActive) {
        return;
    }

    gameBoard[cellIndex] = currentPlayer;
    cell.textContent = currentPlayer;
    cell.classList.add(currentPlayer);

    if (checkWinner()) {
        gameActive = false;
        status.textContent = `${currentPlayer} wins!`;
        return;
    }

    if (!gameBoard.includes('')) {
        gameActive = false;
        status.textContent = 'It\'s a draw!';
        return;
    }

    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    status.textContent = `${currentPlayer}'s turn`;
}

function checkWinner() {
    const winningCombinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    return winningCombinations.some(combination => {
        const [a, b, c] = combination;
        if (gameBoard[a] && gameBoard[a] === gameBoard[b] && gameBoard[a] === gameBoard[c]) {
            return true;
        }
        return false;
    });
}

board.addEventListener('click', handleCellClick);
status.textContent = `${currentPlayer}'s turn`;
