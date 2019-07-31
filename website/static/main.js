document.addEventListener('DOMContentLoaded', () => {
  console.log('content loaded');

  sbtn = document.getElementById('submit-btn');
  sbtn.onclick = (sbtn) => {
    let user_id = document.querySelector("#user_id").value;
    let user_pass = document.getElementById("user_password").value;
    let user_role = document.getElementById("user_role").value;

    let user_status = document.getElementById("user_status").value;
    let data = [];
    data["pass"] = user_pass;
    data["role"] = user_role;
    data["status"] = user_status;
    // data = [data];
    // data = `pass=${user_pass}+user:${user}`
    let json = JSON.stringify(data);
    console.log(user_role);
    console.log(data);
    console.log(json);
    let xhr = new XMLHttpRequest();
    xhr.open('PUT', '/api/v1/user/' + user_id, true);
    xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log('response received');
            // ul.innerHTML = '';
        }
    };
    xhr.send(json);
    console.log(user_pass);
    console.log('request sent');
  };
  // document.getElementById('submit-btn').addEventListener('click', event => {
  //       // event.preventDefault();
  //       console.log("form submit shod!!");
  //       let user_id = document.getElementById('user_id').value;
  //       let user_pass = document.getElementById('user_password').value;
  //       let user_role = document.getElementById('user_role').value;
  //       let user_status = document.getElementById('user_status').value;
  //       let data = `pass=${user_pass}&status=${user_status}&role=${user_role}`;
  //       let xhr = new XMLHttpRequest();
  //       xhr.open('PUT', '/api/v1/user/' + user_id);
  //       xhr.onreadystatechange = () => {
  //           if (xhr.readyState === 4 && xhr.status === 200) {
  //               console.log('response received');
  //               // ul.innerHTML = '';
  //           }
  //       };
  //       xhr.send(data);
  //       console.log('request sent');
  //   });




});
