import * as tf from '@tensorflow/tfjs';

async function load() {
  const model = await tf.loadLayersModel('model.json');
  return model;
};

load();

function predict(model) {
  const input = tf.tensor([90, 1, 0, 0, 15, 0, 0, 1, 0, 0])
  output = model.predict(input)
  const outputData = output.dataSync();
  document.getElementById("answer").value = Number(outputData[0] > 0.5);
}

//  const userInput = document.getElementById('userInput').value
//  const inputTensor = tf.tensor([parseInt(userInput)]);  // then convert to tensor

  // now lets make the prediction, we use .then because the model is a promise
  // (this is confusing as a Python user, but useful so check it out if interested)
//  model.then(model => {
//    let result = model.predict(inputTensor);  // make prediction like in Python
result = result.round().dataSync()[0];  // round prediction and get value
alert(result ? "True" : "False");  // creates pop-up, if result == 1 shows 'odd', otherwise 'even'
//  });
//};

// const model = load();  // load the model now to prevent any delay when user clicks 'Predict'
