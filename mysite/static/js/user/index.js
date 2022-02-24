window.onload = ()=> {
  setInterval(fetchData, 1000);
  function fetchData() {
    return fetch(`${window.origin}/user/userdata/`).then(res=> res.json()).then(data=>{
      a = data['views']
      console.log(a)
      console.log(typeof a)
    })
  }
  
  function myData() {
    
    const labels = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
    ];

    const data = {
      labels: labels,
      datasets: [{
        label: 'My First dataset',
        backgroundColor: ['red',
          'green',
          'cyan',
          'pink',
          'blue'],
        data: [0,
          10,
          5,
          2,
          20,
          30,
          45],
      }]
    };

    const config = {
      type: 'pie',
      data: data,
      options: {}
    };
    const myChart = new Chart(
      document.getElementById('myChart'),
      config
    );
  }
    function myAct() {
    const labels = [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
    ];

    const data = {
      labels: labels,
      datasets: [{
        label: 'My First dataset',
        backgroundColor: ['red',
          'green',
          'cyan',
          'pink',
          'blue'],
        data: [0,
          10,
          5,
          2,
          20,
          30,
          45],
      }]
    };

    const config = {
      type: 'line',
      data: data,
      options: {}
    };
    const myChart = new Chart(
      document.getElementById('myPost'),
      config
    );
  }
  myAct()
  myData()
}