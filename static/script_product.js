let currentImageIndex = 0;


function changeImageSlideRight(numImage) {

    let images = []

    if(numImage == 1) {
        images = ['../static/product-1-frontview.png', '../static/product-1-sideview.png', '../static/product-1-topview.png'];
    }

    if(numImage == 2) {
        images = ['../static/product-2-frontview.png', '../static/product-2-sideview.png', '../static/product-2-topview.png'];
    }

    if(numImage == 3) {
        images = ['../static/product-3-frontview.png', '../static/product-3-sideview.png', '../static/product-3-topview.png'];
    }

    const currentImage = document.getElementById('current-img');
    currentImage.classList.add('hiddenR');

    setTimeout(() => {
        if(currentImageIndex == 2) {
            currentImageIndex = 0;
        } else {
            currentImageIndex = currentImageIndex + 1;
        }
        currentImage.src = images[currentImageIndex];
        currentImage.classList.remove('hiddenR')
    }, 300);
}

function changeImageSlideLeft(numImage) {

    let images = []

    if(numImage == 1) {
        images = ['../static/product-1-frontview.png', '../static/product-1-sideview.png', '../static/product-1-topview.png'];
    }

    if(numImage == 2) {
        images = ['../static/product-2-frontview.png', '../static/product-2-sideview.png', '../static/product-2-topview.png'];
    }

    if(numImage == 3) {
        images = ['../static/product-3-frontview.png', '../static/product-3-sideview.png', '../static/product-3-topview.png'];
    }

    const currentImage = document.getElementById('current-img');

    currentImage.classList.add('hiddenL');

    setTimeout(() => {
        if(currentImageIndex == 0) {
            currentImageIndex = 2
        } else {
            currentImageIndex = currentImageIndex - 1;
        }
        currentImage.src = images[currentImageIndex];
        currentImage.classList.remove('hiddenL')
    }, 300);
}