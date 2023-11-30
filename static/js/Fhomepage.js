document.addEventListener('DOMContentLoaded', function() {
    const searchTextarea = document.getElementById('search-textarea');
    const searchLabel = document.getElementById('search-label');
  
    searchTextarea.addEventListener('input', function() {
      if (searchTextarea.value.trim() !== '') {
        searchLabel.style.display = 'none'; // Hide the search element
      } else {
        searchLabel.style.display = 'block'; // Show the search element
      }
    });
  });
  