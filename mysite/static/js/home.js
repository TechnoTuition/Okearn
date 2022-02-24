function getData() {
  url = "/api/v1/users/"
  fetch(url).then((res)=>{
    return res.json()
  }).then((data)=>{
    console.log(data)
  })
  
}