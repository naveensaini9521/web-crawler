// scripts.js

$(document).ready(function() {
    var currentPage = 1;  // Initial page number
    var query = '';  // Initial query

    // Function to perform search
    function search(query, page) {
        $.ajax({
            url: '/search',
            method: 'GET',
            data: {
                query: query,
                page: page
            },
            dataType: 'json',
            success: function(response) {
                displayResults(response.results);
                renderPagination(response.totalPages, page, query);
            },
            error: function(xhr, status, error) {
                console.error('AJAX Error: ' + status, error);
            }
        });
    }

    // Function to display search results
    function displayResults(results) {
        var resultList = $('#resultsList');
        resultList.empty();
        if (results.length > 0) {
            $.each(results, function(index, item) {
                var listItem = $('<li>').addClass('list-group-item').text(item.title);
                resultList.append(listItem);
            });
        } else {
            resultList.append($('<li>').addClass('list-group-item').text('No results found.'));
        }
    }

    // Function to render pagination links
    function renderPagination(totalPages, currentPage, query) {
        var pagination = $('#pagination ul');
        pagination.empty();
        for (var i = 1; i <= totalPages; i++) {
            var pageLink = $('<li>').addClass('page-item');
            if (i === currentPage) {
                pageLink.addClass('active');
            }
            var link = $('<a>').addClass('page-link').attr('href', '#').text(i);
            link.attr('onclick', 'search("' + query + '", ' + i + '); return false;');
            pageLink.append(link);
            pagination.append(pageLink);
        }
    }

    // Initial search on page load
    search(query, currentPage);

    // Search button click event
    $('#searchButton').click(function() {
        query = $('#searchInput').val();
        if (query.trim() !== '') {
            currentPage = 1;  // Reset to first page when new search is performed
            search(query, currentPage);
        }
    });

    // Pagination link click event (delegated event)
    $(document).on('click', '#pagination ul li a', function(event) {
        event.preventDefault();
        currentPage = parseInt($(this).text());
        search(query, currentPage);
    });
});
// Sample data for autocomplete
const countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
    "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
    "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
    "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada",
    "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
    "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
    "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia",
    "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
    "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos",
    "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia",
    "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
    "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
    "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
    "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan",
    "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
    "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
    "Yemen", "Zambia", "Zimbabwe"
  ];
  
  const autocompleteItems = document.getElementById('autocomplete-items');
  
  // Function to clear autocomplete items
  function clearAutocomplete() {
    while (autocompleteItems.firstChild) {
      autocompleteItems.removeChild(autocompleteItems.firstChild);
    }
  }
  
  // Function to show autocomplete suggestions
  function showAutocompleteSuggestions(input) {
    clearAutocomplete();
    
    const filteredSuggestions = countries.filter(country => 
      country.toLowerCase().startsWith(input.toLowerCase())
    );
    
    filteredSuggestions.forEach(suggestion => {
      const suggestionElement = document.createElement('div');
      suggestionElement.textContent = suggestion;
      suggestionElement.addEventListener('click', function() {
        searchInput.value = suggestion;
        clearAutocomplete();
      });
      autocompleteItems.appendChild(suggestionElement);
    });
  }
  
  // Event listener for input changes
  searchInput.addEventListener('input', function() {
    showAutocompleteSuggestions(this.value);
  });
  
  // Event listener to clear autocomplete on clicking outside
  document.addEventListener('click', function(e) {
    if (!autocompleteItems.contains(e.target) && e.target !== searchInput) {
      clearAutocomplete();
    }
  });
  