let authors = [];
let books = [];
let genres = [];
var bookRatings = {};

function initSearch(container, submittedBox = null, isRatingBox = false) {
  const searchBox = container.querySelector(".search-box");
  if (!searchBox) return;
  const inputBox = searchBox.querySelector("input");
  const resultsBox = searchBox.querySelector(".result-box");
  const ratingBox = isRatingBox ? container : null;

  function showResults() {
    resultsBox.style.display = 'block';

    const placeholderTxt = inputBox.placeholder;
    const words = placeholderTxt.trim().split(" ");
    const lastWord = words[words.length - 1];

    fetch('/get_' + lastWord)
      .then(response => response.json())
      .then(data => {
        let result = [];
        const input = inputBox.value;
        if (input.length === 0) {
          result = data;
        } else {
          result = data.filter((keyword) => keyword.toLowerCase().includes(input.toLowerCase()));
        }
        result = result.slice(0, 10);
        displayResults(result, resultsBox, inputBox, submittedBox, searchBox, isRatingBox, ratingBox);
        if (!result.length) {
          resultsBox.innerHTML = '';
        }
      })
  }

  inputBox.onclick = showResults;
  inputBox.onkeyup = showResults;

  document.addEventListener('click', function (event) {
    if (!searchBox.contains(event.target)) {
      resultsBox.style.display = 'none';
    }
  });
}  

function displayResults(result, resultsBox, inputBox, submittedBox, searchBox, isRatingBox, ratingBox) {
  const ul = document.createElement("ul");

  result.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;

    const context = searchBox.dataset.context;
    const targetArray = getArrayByContext(context);
    li.onclick = () => {
      inputBox.value = isRatingBox ? item : ''; // rating-box keeps selection visible, others clear
      resultsBox.innerHTML = '';

      if (submittedBox) {
        if (targetArray && targetArray.length >= 3) return; // limit of three items
        const newItem = document.createElement("div");
        newItem.classList.add("submitted-item");
        newItem.textContent = item;
        submittedBox.appendChild(newItem);

        if (context === 'authors') authors.push(item);
        else if (context === 'books') books.push(item);
        else if (context === 'genres') genres.push(item);
      } 
      else if (isRatingBox && ratingBox) {
        // Label for rated book  
        let rated = ratingBox.querySelector('.rating-selected');
        if (!rated) {
          rated = document.createElement('div');
          rated.className = 'rating-selected';
          ratingBox.appendChild(rated);
        }
        rated.textContent = "Selected Book: " + item;

        if (bookRatings[item]) {
          bookRatings[item] = 0;
        }
      }
    };

    ul.appendChild(li);
  });

  resultsBox.innerHTML = '';
  resultsBox.appendChild(ul);
}

var algorithm = 0;
var btn = document.querySelector('.btn');
function leftClick() {
  btn.style.left = '0%'; // orange bar set on the left half
  algorithm = 0;
  console.log(algorithm);
}
function rightClick() {
  btn.style.left = '50%'; // orange bar set on the right hald
  algorithm = 1;
  console.log(algorithm)
}

function getArrayByContext(context) {
  if (context === 'books') return books;
  if (context === 'authors') return authors;
  if (context === 'genres') return genres;
  return null;
}

// generates the html for "Your Book" section
function createSpan(className, text) {
  const span = document.createElement("span");
  span.className = className;
  span.textContent = text;
  return span;
}

// initialize search rows
document.querySelectorAll(".search-row").forEach(searchRow => {
  const submittedBox = searchRow.querySelector(".submitted-box");
  initSearch(searchRow, submittedBox, false);
});

// initialize rating-box search 
document.querySelectorAll(".rating-box").forEach(ratingBox => {
  initSearch(ratingBox, null, true);

  // rating stars logic 
  const stars = ratingBox.querySelectorAll(".stars i");
  stars.forEach((star, index) => {
    star.addEventListener("click", () => {
      stars.forEach((s, i) => {
        s.classList.toggle("active", index >= i);
      });
      const selectedBook = ratingBox.querySelector('.rating-selected').textContent.replace("Selected Book: ", "");

      if (selectedBook && bookRatings[selectedBook] === undefined) {
        bookRatings[selectedBook] = 0;
      }
      if (bookRatings[selectedBook] !== undefined) {
        bookRatings[selectedBook] = index + 1;
        console.log("Book: " + selectedBook + ", Rating: " + bookRatings[selectedBook]);
      }
      else {
        console.log("Rating did not work");
      }
    });
  });
});


function generate() {
  if (authors.length === 0 && books.length === 0 && genres.length === 0) {
    alert("At least one entry such as a book/author/genre must be selected to generate books");
    return;
  }
  console.log(bookRatings);

  fetch('/get_result_books', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({authors, books, genres})
  })
    .then(response => response.json())
    .then(data => {
      const bookList = document.getElementById("book-list");
      bookList.innerHTML = "";

      data.forEach(book => {
        const[title, author, genre, rating] = book;

        const h3 = document.createElement("h3");
        h3.className = "book-info";
        
        h3.appendChild(createSpan("book-title", title));
        h3.append(", ");
        h3.appendChild(createSpan("book-author", author));
        h3.append(", ");
        h3.appendChild(createSpan("book-genre", genre));
        h3.append(", ");
        h3.appendChild(createSpan("book-rating", rating));
        bookList.appendChild(h3);
      });
    });
}