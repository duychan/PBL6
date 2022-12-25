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
      rs_detect.value = api_svm["result"]
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
      rs_detect.value = api_knn["result"]
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
        rs_detect.value = api_nb["result"]
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
        rs_detect.value = api_lstm["result"]
        break;
  }
});
