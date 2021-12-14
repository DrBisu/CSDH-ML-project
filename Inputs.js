var inputs = []
document.getElementById("Predict").onclick = function () {
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

    inputs.push(AgePred);
    inputs.push(SexPred);
    inputs.push(HeadachePred);
    inputs.push(DementiaPred);
    inputs.push(GCSPred);
    inputs.push(MotorPred);
    inputs.push(MidlinePred);
    inputs.push(CSDHPred);
    inputs.push(QoLPred);
    inputs.push(AnticoagPred);
}

console.log(inputs);