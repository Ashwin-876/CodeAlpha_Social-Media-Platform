document.addEventListener("DOMContentLoaded", function () {
    loadPosts();
    setupEventListeners();
});

// Base API URL
const API_URL = "http://127.0.0.1:8000/api"; // Adjust based on your backend URL

// Load Posts for the Feed
function loadPosts() {
    fetch(`${API_URL}/posts/`)
        .then(response => response.json())
        .then(posts => {
            const feed = document.getElementById("feed");
     
