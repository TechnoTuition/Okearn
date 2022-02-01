function getData() {
  url = "/api/user"
  fetch(url).then((res)=>{
    return res.json()
  }).then((data)=>{
    console.log(data)
  })
  
}