const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

function randomValueFromArray(array){
  const random = Math.floor(Math.random()*array.length);
  return array[random];
}

const storyText = 'It was 94 fahrenheit outside, so :insertx: went on an adventure. When they got to :inserty:, they were breathless for a few moments, then :insertz:. Bob saw the whole thing, but continued the adventure — :insertx: did not want to go on an adventure.'
const insertx = ['Seashell Sally', 'Cookie Connor', 'Merry Melissa'];
const inserty = ['the crime scene', 'the cemetary', 'the hot dog stand'];
const insertz = ['ran as far and fast as possible', 'vanished into thin air', 'turned into a ghost and floated away'];

randomize.addEventListener('click', result);

function result() {

  let newStory = storyText;
  const xItem = randomValueFromArray(insertx);  
  const yItem = randomValueFromArray(inserty); 
  const zItem = randomValueFromArray(insertz); 

  newStory = newStory.replaceAll(':insertx:',xItem);
  newStory = newStory.replaceAll(':inserty:',yItem);
  newStory = newStory.replaceAll(':insertz:',zItem);

  if(customName.value !== '') {
    const name = customName.value;
    newStory = newStory.replaceAll('Bob', name);

  }

  if(document.getElementById("uk").checked) {
    const weight = `${Math.round(300*0.0714286)} stone`;
    const temperature =  `${Math.round((94-32) * 5 / 9)} centigrade`;

    newStory = newStory.replaceAll('94 fahrenheit', temperature);
    newStory = newStory.replaceAll('300 pounds', weight);

  }

  story.textContent = newStory;
  story.style.visibility = 'visible';
 }