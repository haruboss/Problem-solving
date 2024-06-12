function appendToDisplay(value) {
    document.getElementById('display').value += value;
  }
  
  function clearDisplay() {
    document.getElementById('display').value = '0';
  }
  
  function calculateResult() {
    const displayValue = document.getElementById('display').value;
    try {
      const result = eval(displayValue);
      document.getElementById('display').value = result;
    } catch (error) {
      document.getElementById('display').value = 'Error';
    }
  }
  