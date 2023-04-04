function sendRequest() {
    // Получаем значения из полей ввода
    var nsShares = document.getElementById("ns-shares").value;
    var height = document.getElementById("height").value;
  
    // Формируем URL-адрес для GET-запроса
    var url = "http://localhost:26659/namespaced_shares/" + nsShares + "/height/" + height;
  
    // Отправляем GET-запрос на сервер
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status == 200) {
        // Отображаем результат в отдельном окне
        window.open().document.write(xhr.responseText);
      }
    };
    xhr.send();
  }
  