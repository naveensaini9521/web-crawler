const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');

// Mock data for autocomplete (replace with real data fetching)
const suggestions = [
    "example search 1",
    "example search 2",
    "example search 3",
    "example search 4",
    "example search 5"
];

searchInput.addEventListener('input', function() {
    const input = this.value.toLowerCase();
    const autocompleteContainer = document.createElement('div');
    autocompleteContainer.setAttribute('class', 'autocomplete-items');

    suggestions.filter(function(suggestion) {
        return suggestion.toLowerCase().includes(input);
    }).forEach(function(suggestion) {
        const autocompleteItem = document.createElement('div');
        autocompleteItem.innerHTML = suggestion;
        autocompleteItem.addEventListener('click', function() {
            searchInput.value = suggestion;
            autocompleteContainer.remove();
        });
        autocompleteContainer.appendChild(autocompleteItem);
    });

    if (input.length > 0) {
        this.parentNode.appendChild(autocompleteContainer);
    } else {
        autocompleteContainer.remove();
    }
});

// Event listener for search button click
searchButton.addEventListener('click', function() {
    const query = searchInput.value.trim();
    if (query !== '') {
        const encodedQuery = encodeURIComponent(query);
        window.location.href = `/results?q=${encodedQuery}`;
    }
});
