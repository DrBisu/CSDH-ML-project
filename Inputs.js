document.getElementById("Predict").onclick = function () {

    async function load_model() {
        let m = await tf.loadLayersModel('modelSigmoid.json')
        return m;
    }

    let model = load_model();

    model.then(function (res) {
        var AgePred = document.getElementById("Age").value;
        var SexPred = document.getElementById("Sex").value;
        var HeadachePred = document.getElementById("Headache").value;
        var DementiaPred = document.getElementById("Dementia").value;
        var GCSPred = document.getElementById("GCS").value;
        var MotorPred = document.getElementById("Motor_Weakness").value;
        var MidlinePred = document.getElementById("Midline_Shift").value;
        var CSDHPred = document.getElementById("CSDH_size").value;
        var QoLPred = document.getElementById("QoL").value;
        var AnticoagPred = document.getElementById("Anticoagulation").value;
        var prediction = res.predict(tf.tensor([[parseInt(AgePred),
            parseInt(SexPred), parseInt(HeadachePred), parseInt(DementiaPred),
            parseInt(GCSPred), parseInt(MotorPred), parseInt(MidlinePred),
            parseInt(CSDHPred), parseInt(QoLPred), parseInt(AnticoagPred)]]));



        document.getElementById("prediction").innerHTML = prediction  ;

        var d = document.getElementById("prediction").textContent;

        var newStr1 = d.replace('Tensor','');
        var newStr2 = newStr1.replace('[','');
        var newStr3 = newStr2.replace(']','');
        var newStr4 = newStr3.replace(',','');
        var newStr5 = newStr4.replace(']','');
        var newStr6 = newStr5.replace('[','');

        if (parseFloat( newStr6) > 0.5)
            var decision = 'Accepted'
        else
            var decision = 'Rejected'


        document.getElementById("decision").innerHTML = decision;






    });}


