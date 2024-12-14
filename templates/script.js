// Ensure the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    const downloadButtons = document.querySelectorAll('.btn[download]');

    // Optional: Log download button clicks for debugging
    downloadButtons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const url = button.getAttribute('href');
            console.log(`Downloading from: ${url}`);
        });
    });
});
