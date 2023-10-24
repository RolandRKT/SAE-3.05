document.addEventListener('DOMContentLoaded', function() {
    const animatedImage1 = document.getElementById('animation-button1');
    const imgContent = document.getElementById('animation-button');
    animatedImage1.style.transform = 'translateX(-8vw) scaleX(-1)';
    imgContent.classList.add('hidden');
    setTimeout(function(){
        imgContent.classList.remove('hidden');
        setTimeout(function(){
        imgContent.classList.add('transition-logo');
    }, 100);
    }, 1000);
  });