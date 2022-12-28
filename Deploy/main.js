const btn = document.querySelector(".button");
const selectItems = document.querySelector(".custom-select")
const rs_detect = document.querySelector(".rs-detect");
selectItems.addEventListener("change", ()=>{
  rs_detect.value = ""
})
btn.addEventListener("click", async () => {
  const text = document.querySelector(".textarea")
  if(text.value.split(" ").length < 30){
    rs_detect.value = "Quá ít dữ liệu vui lòng nhập nhiều hơn"
    return
  }
  const bodyInput = { "content": text.value};
  switch (selectItems.value) {
    case "SVM":
      let api_svm = await fetch("http://127.0.0.1:8000/predict_svm", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(bodyInput),
      });
      api_svm = await api_svm.json();
      let predicted_svm = api_svm["result"]
      let confidence_svm = api_svm["confidence"] 
      if(predicted_svm == "fake"){
        predicted_svm = "Giả"
      }
      else{
        predicted_svm = "Thật"
      }
      rs_detect.value = `Mô hình dự đoán đây là tin ${predicted_svm} với độ tin cậy là: ${confidence_svm}%`
      break;

    case "KNN":
      let api_knn = await fetch("http://127.0.0.1:8000/predict_knn", {
        method: "POST",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(bodyInput),
      });
      api_knn = await api_knn.json();
      let predicted_knn = api_knn["result"]
      let confidence_knn = api_knn["confidence"] 
      console.log(predicted_knn)
      if(predicted_knn == "fake"){
        predicted_knn = "Giả"
      }
      else{
        predicted_knn = "Thật"
      }
      rs_detect.value = `Mô hình dự đoán đây là tin ${predicted_knn} với độ tin cậy là: ${confidence_knn}%`
      break;

      case "NB":
        let api_nb = await fetch("http://127.0.0.1:8000/predict_nb", {
          method: "POST",
          headers: {
            "Content-type": "application/json",
          },
          body: JSON.stringify(bodyInput),
        });
        api_nb = await api_nb.json();
        let predicted_nb = api_nb["result"]
        let confidence_nb = api_nb["confidence"] 
        if(predicted_nb == "fake"){
          predicted_nb = "Giả"
        }
        else{
          predicted_nb = "Thật"
        }
        rs_detect.value = `Mô hình dự đoán đây là tin ${predicted_nb} với độ tin cậy là: ${confidence_nb}%`
        break;
        
      
      case "LSTM":
        let api_lstm = await fetch("http://127.0.0.1:8000/predict_lstm", {
          method: "POST",
          headers: {
            "Content-type": "application/json",
          },
          body: JSON.stringify(bodyInput),
        });
        api_lstm = await api_lstm.json();
        let predicted_lstm = api_lstm["result"]
        let confidence_lstm = api_lstm["confidence"] 
        if(predicted_lstm == "fake"){
          predicted_lstm = "Giả"
        }
        else{
          predicted_lstm = "Thật"
        }
        rs_detect.value = `Mô hình dự đoán đây là tin ${predicted_lstm} với độ tin cậy là: ${confidence_lstm}%`
        break;
    }
  }
);
