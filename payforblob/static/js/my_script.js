const submitButton = document.getElementById('submit-button');
const loadingSpinner = document.getElementById('loading-spinner');

submitButton.addEventListener('click', () => {
  loadingSpinner.style.display = 'block';
});
