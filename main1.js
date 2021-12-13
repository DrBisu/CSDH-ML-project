async function load_model() {
    let m = await tf.loadLayersModel('model.json')
    return m;
}

let model = load_model();

model.then(function (res) {
    const inputs = tf.tensor2d([[80, 1, 0, 0, 15, 0, 1, 3, 0, 0]]);
    const prediction = res.predict(inputs);
    prediction.print();
});
