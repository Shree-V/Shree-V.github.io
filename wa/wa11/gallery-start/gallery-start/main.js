const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');

/* Declaring the array of image filenames */

const images = ['ProfilePic.png', `Drawing.jpg`, `backgroundpic.jpg`, `MossTak Logo.png`, `Flower.jpg`];
const alts = {
  'ProfilePic.png' : 'Rose on a plain background',
  'Drawing.jpg' : 'Drawing of girl on swing',
  'backgroundpic.jpg' : 'Tree on a plain background',
  'MossTak Logo.png' : 'MossTak Tree Logo',
  'Flower.jpg' : 'Flower Collage'
}

/* Declaring the alternative text for each image file */

/* Looping through images */

for (const image of images) {
const newImage = document.createElement('img');
newImage.setAttribute('src', `images/${image}`);
newImage.setAttribute('alt', alts[image]);
thumbBar.appendChild(newImage);
newImage.addEventListener('click', e => {
    displayedImage.src = e.target.src;
    displayedImage.alt = e.target.alt;
  });
}

/* Wiring up the Darken/Lighten button */

btn.addEventListener('click', () => {
    const btnClass = btn.getAttribute('class');
    if (btnClass === 'dark') {
      btn.setAttribute('class','light');
      btn.textContent = 'Lighten';
      overlay.style.backgroundColor = 'rgba(0,0,0,0.5)';
    } else {
      btn.setAttribute('class','dark');
      btn.textContent = 'Darken';
      overlay.style.backgroundColor = 'rgba(0,0,0,0)';
    }
  });