document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.slide');
    const circles = document.querySelectorAll('.circle');
    let index = 0;

    const changeSlide = (newIndex) => {
        moveBy = [0, -100, -200]
        index = newIndex;
        slides.forEach((slide, i) => {
            slide.style.transform = `translateX(${moveBy[index]}%)`;
        });
        circles.forEach((circle, i) => {
            if (i === index) {
                circle.classList.add('active');
            } else {
                circle.classList.remove('active');
            }
        });
    };

    circles.forEach((circle, i) => {
        circle.addEventListener('click', () => {
            changeSlide(i);
        });
    });

    setInterval(() => {
        index = (index + 1) % slides.length;
        changeSlide(index);
    }, 3000);

    // Initialize first slide
    changeSlide(0);
});
