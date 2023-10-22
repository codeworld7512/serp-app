function showCopiedPopup() {
    // Create the popup div
    let popup = document.createElement('div');
    popup.textContent = "Copied to clipboard!";
    popup.style.position = 'fixed';
    popup.style.bottom = '20px';
    popup.style.left = '50%';
    popup.style.transform = 'translateX(-50%)';
    popup.style.backgroundColor = '#333';
    popup.style.color = '#fff';
    popup.style.padding = '10px 20px';
    popup.style.borderRadius = '5px';
    popup.style.zIndex = '10000';
    popup.style.opacity = '0.9';
    document.body.appendChild(popup);

    // Remove the popup after 3 seconds
    setTimeout(function() {
        document.body.removeChild(popup);
    }, 3000);
}

// Injecting CSS into the document
let style = document.createElement('style');
style.textContent = `
    /* Hide the link icon by default using opacity */
    h2 .heading-link-icon, 
    h3 .heading-link-icon, 
    h4 .heading-link-icon {
        display: inline-block;
        opacity: 0;
        margin-left: 0px; 
        padding: 0px;
        border: none;
        vertical-align: middle; 
        transition: opacity 0.3s; 
    }

    .heading-link-icon:hover svg {
        stroke: var(--primary-color);
    }

    /* Show the link icon when hovering over its parent heading */
    h2:hover .heading-link-icon, 
    h3:hover .heading-link-icon, 
    h4:hover .heading-link-icon {
        opacity: 1;  // Make the SVG icon fully visible on hover
    }
`;
document.head.appendChild(style);




function slugify(text) {
    return text.toLowerCase().trim()
        .replace(/\s+/g, '-')          
        .replace(/&/g, '-and-')        
        .replace(/[^\w\-]+/g, '')      
        .replace(/\-\-+/g, '-');       
}

// Adding link icons to headings
document.querySelectorAll('h2, h3, h4').forEach(function(heading) {
    let button = document.createElement('button');
    button.type = "button";
    button.className = "btn btn-link";
    button.setAttribute('aria-label', `Copy link to this section: ${heading.textContent.trim()}`);
    button.setAttribute('data-title', `Copy link to this section: ${heading.textContent.trim()}`);
    button.setAttribute('data-id', heading.id);

    let svg = `<svg  fill="none" height="24" viewBox="0 0 24 24" width="24" class="heading-link-icon logo-inverse">
                <path d="m14 7h2c2.7614 0 5 2.23858 5 5 0 2.7614-2.2386 5-5 5h-2m-4-10h-2c-2.76142 0-5 2.23858-5 5 0 2.7614 2.23858 5 5 5h2m-2-5h8" 
                      stroke="#000" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
               </svg>`;

    button.innerHTML = svg;
    heading.appendChild(button); // Append the button inside the heading

    button.addEventListener('click', function() {
        // Generate slug for the heading
        let slug = slugify(heading.textContent);
        heading.id = slug;

        // Update the URL with the anchor
        history.pushState(null, null, `#${slug}`);

        // Copy the URL to the clipboard
        let currentUrl = window.location.href;
        navigator.clipboard.writeText(currentUrl).then(function() {
            showCopiedPopup();  // Show the popup
        }).catch(function(err) {
            console.error('Failed to copy URL: ', err);
        });
    });
});
