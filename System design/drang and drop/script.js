function appendToDisplay(value) {
  const display = document.getElementById('display');
  display.value += value;
}

function clearDisplay() {
  const display = document.getElementById('display');
  display.value = '';
}

function calculateResult() {
  const display = document.getElementById('display');
  try {
    const result = eval(display.value);
    if (isNaN(result) || !isFinite(result)) {
      throw new Error('Invalid expression');
    }
    display.value = result;
  } catch (error) {
    display.value = 'Error';
  }
}
