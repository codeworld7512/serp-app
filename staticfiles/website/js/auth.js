async function getCurrentUser() {
    const token = localStorage.getItem('auth_token');

    if (!token) {
        return null;
    }

    const response = await fetch(window.AUTH_API_URL + '/users/me', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
        }
    });

    if (response.ok) {
        // If the response was successful, return the user data
        const userData = await response.json();
        localStorage.setItem('user', JSON.stringify(userData));
        return userData;
    } else {
        // If the response was not successful, remove the token and return null
        localStorage.removeItem('auth_token');
        localStorage.removeItem('user');
        return null;
    }
}

async function logout() {
    const token = localStorage.getItem('auth_token');

    if (!token) {
        return null;
    }

    localStorage.removeItem('auth_token');
    localStorage.removeItem('user');
    return null;
}


document.addEventListener('DOMContentLoaded', function () {
    getCurrentUser().then(userData => {
        if (userData) {
            // The user is logged in
            const loggedOutLinks = document.querySelectorAll('#logged-out');
            const loggedInLinks = document.querySelectorAll('#logged-in');
            loggedOutLinks.forEach(link => link.hidden = true);
            loggedInLinks.forEach(link => link.hidden = false);

            if (userData.profile_photo != null) {
                imgElems = document.querySelectorAll('#profile-nav-avatar');
                imgElems.forEach(imgElem => {
                    imgElem.src = userData.profile_photo;
                });
            }
            if (userData.name != null) {
                name_ = document.querySelector('#profile-nav-name');
                name_.innerHTML = userData.name;
            } else {
                name_ = document.querySelector('#profile-nav-name');
                name_.innerHTML = userData.username;
            }
            email = document.querySelector('#profile-nav-email');
            email.innerHTML = userData.email;

            // Add event listener to logout button
            const logoutButton = document.querySelector('#logout');
            logoutButton.addEventListener('click', (event) => {
                event.preventDefault();

                logout();
                // Refresh the page
                window.location.reload();
            });
        } else {
            // The user is not logged in
            const loggedOutLinks = document.querySelectorAll('#logged-out');
            const loggedInLinks = document.querySelectorAll('#logged-in');
            loggedOutLinks.forEach(link => link.hidden = false);
            loggedInLinks.forEach(link => link.hidden = true);
        }
    });
});