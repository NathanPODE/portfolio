const squares = document.querySelectorAll('.skill-square');
const duration = 70;
squares.forEach((square, i) => {
    square.style.animationDelay = `-${(i / squares.length) * duration}s`;
});

squares.forEach(square => {
    square.addEventListener('mouseenter', () => {
        document.body.classList.add('all-paused');
    });

    square.addEventListener('mouseleave', () => {
        document.body.classList.remove('all-paused');
    });
})