const sqaures = document.querySelectorAll('.skill-square');
const duration = 50;
sqaures.forEach((sq, i) => {
    sq.style.animationDelay = '-${(i/squares.length) * duration}s';
});