$(document).ready(function(){
        $('#urlForm').on('submit', function(event){
            event.preventDefault();
            var url = $('urlInput').val();

            if(url){
               fetchTextData(url).then(textData => {
                   var words = processTextData(textData);
                   $('#wordcloud').jQCloud('destroy'):
                   $('#wordcloud').jQCloud(words, {
                       fontFamily: 'Arial, sans-serif',
                       colors: ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
                       shape: 'rectangular'
               });
            }).catch(error => {
                alert('Error fetching data: ' + error);
            });
        }
        else {
           alert('Please enter a valid URL.');
        }
    });

    function fetchTextData(url) {
         return $.ajax({
            url: url,
            method: 'GET',
            dataType: 'text'
         });
    }

    function processTextData(text) {
         var wordsArray = text.split(/\s+/);
         var wordCounts = {};
         wordsArray.forEach(word => {
             word = word.toLowerCase().replace(/[^\w]/g, '');
             if (word.length > 2) {
                 wordCounts[word] = (wordCounts[word] || 0) + 1;
             }

             var words = [];
             for (var word in wordCounts) {
                  words.push({ text: word, weight: wordCounts[word] });
             }
             return words;
         }
    });