// user like fetch request
var likeCount;
function like(postid) {
  likeCount = document.querySelector(`#likeCount${postid}`)
  fetch(`${window.origin}/blog/like/${postid}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(res => res.json()).then(data=> {
    if (data['liked'] == true) {
      let i = document.querySelector("#like")
      i.className = "fas fa-thumbs-up"
    } else {
      let i = document.querySelector("#like")
      i.className = "far fa-thumbs-up"
    }
    likeCount.innerHTML = data["like"]
  })
}

// user fallow fetch
function fallow(user_id) {
  console.log("fallow")
  var fallowCount = document.querySelector(`#fallowCount${user_id}`)
  fetch(`${window.origin}/blog/fallow/${user_id}/`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((res)=>res.json()).then((data)=> {
      console.log(data)
      fallowCount.innerHTML = data['fallower']
    })

}