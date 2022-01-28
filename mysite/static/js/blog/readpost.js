
var likeCount;
function like(postid) {
  likeCount = document.querySelector(`#likeCount${postid}`)
  fetch(`${window.origin}/blog/like/${postid}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(res => res.json()).then(data=> {
    likeCount.innerHTML = data["like"]
  })
}