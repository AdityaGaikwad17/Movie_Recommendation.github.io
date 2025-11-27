// Global movie list (will be filled when JSON loads)
let movies = [];

// Load movie database from JSON file
fetch('movies.json')
  .then(res => res.json())
  .then(data => {
      movies = data;                 // store globally
      displayResults(movies);        // show all movies initially
  })
  .catch(err => console.error("Error loading movies.json:", err));


// Attach search event listener
document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    searchMovies();
});


// ---------------- SEARCH MOVIE FUNCTION ----------------
function searchMovies() {
    if (!movies.length) return; // avoid errors if JSON not loaded

    const genre = document.getElementById('genre').value;
    const minRating = parseFloat(document.getElementById('minRating').value) || 0;
    const year = parseInt(document.getElementById('year').value) || 0;

    const filteredMovies = movies.filter(movie => {
        const genreMatch = !genre || movie.genre === genre;
        const ratingMatch = movie.rating >= minRating;
        const yearMatch = !year || movie.year === year;

        return genreMatch && ratingMatch && yearMatch;
    });

    displayResults(filteredMovies);
}


// ---------------- SURPRISE ME (RANDOM MOVIE) ----------------
function getRandomMovie() {
    if (!movies.length) return;

    const randomMovie = movies[Math.floor(Math.random() * movies.length)];
    displayResults([randomMovie]);
}


// ---------------- DISPLAY RESULTS ----------------
function displayResults(moviesToDisplay) {
    const resultsDiv = document.getElementById('results');

    if (!moviesToDisplay || moviesToDisplay.length === 0) {
        resultsDiv.innerHTML = `
            <div class="no-results">
                😕 No movies found. Try different filters!
            </div>
        `;
        return;
    }

    resultsDiv.innerHTML = moviesToDisplay.map(movie => `
        <div class="movie-card">
            <div class="movie-header">
                <h3 class="movie-title">${movie.title}</h3>
                <span class="movie-rating">⭐ ${movie.rating}</span>
            </div>
            <div class="movie-meta">
                <span class="genre-badge">${movie.genre}</span>
                <span>📅 ${movie.year}</span>
            </div>
            <p class="movie-description">${movie.description}</p>
        </div>
    `).join('');
}


// ---------------- RESET FUNCTION ----------------
function resetForm() {
    document.getElementById('searchForm').reset();
    displayResults(movies);
}
