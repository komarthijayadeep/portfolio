/* Custom Cursor and Interactivity */
document.addEventListener('DOMContentLoaded', () => {
    const cursor = document.createElement('div');
    cursor.classList.add('cursor');
    document.body.appendChild(cursor);

    const cursorFollower = document.createElement('div');
    cursorFollower.classList.add('cursor-follower');
    document.body.appendChild(cursorFollower);

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
        
        // Slight delay for follower
        setTimeout(() => {
            cursorFollower.style.left = e.clientX + 'px';
            cursorFollower.style.top = e.clientY + 'px';
        }, 50);
    });

    document.addEventListener('mousedown', () => {
        cursor.classList.add('active');
        cursorFollower.classList.add('active');
    });

    document.addEventListener('mouseup', () => {
        cursor.classList.remove('active');
        cursorFollower.classList.remove('active');
    });

    // Hover effects for links and buttons
    const interactiveElements = document.querySelectorAll('a, button, input, textarea, .project-card');
    
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.classList.add('hover');
            cursorFollower.classList.add('hover');
        });
        
        el.addEventListener('mouseleave', () => {
            cursor.classList.remove('hover');
            cursorFollower.classList.remove('hover');
        });
    });
});
