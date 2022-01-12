function getData() {
  URL = '/api/user'
  fetch(URL).then((response) => {
    return response.json()
  }).then((data) => {
    document.querySelector("h3").innerHTML = data[0].id
  })
}
getData()