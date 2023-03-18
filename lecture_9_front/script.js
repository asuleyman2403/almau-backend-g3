const BASE_URL = 'http://localhost:8000';


const fetchBlogs = () => {
    const xhr = new XMLHttpRequest();

    xhr.open('GET', `${BASE_URL}/blogs/`);

    xhr.onload = () => {
        console.log(xhr.response);
    }

    xhr.send();
}

fetchBlogs();

const form = document.getElementById('form');

if (form) {
    form.addEventListener('submit', () => {
        
    });
}



