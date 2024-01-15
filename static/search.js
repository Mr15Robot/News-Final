document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('search-form').addEventListener('submit', function (event) {
        event.preventDefault();

        var searchTerm = document.getElementById('search-input').value;
        // Redirect to a search endpoint or perform any desired action with the searchTerm
        // You may want to use window.location.href = '/search?query=' + encodeURIComponent(searchTerm);
        // Replace '/search' with the actual route you want to handle the search
    });
});