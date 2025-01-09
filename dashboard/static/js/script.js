document.addEventListener('DOMContentLoaded', function() {
  const deviceForm = document.getElementById('deviceForm');
  deviceForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const formData = new FormData(deviceForm);
      fetch('/api/devices', {
          method: 'POST',
          body: formData
      })
      .then(response => response.json())
      .then(data => {
          console.log('Success:', data);
          // Handle success (e.g., update UI)
      })
      .catch((error) => {
          console.error('Error:', error);
      });
  });
});