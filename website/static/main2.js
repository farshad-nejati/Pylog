document.addEventListener('DOMContentLoaded', () => {


  delete_btns = document.getElementsByClassName('delete');
  for (let delete_btn of delete_btns) {
      delete_btn.onclick = () => {
        let user = delete_btn.value;
        console.log(user);

        let xhr = new XMLHttpRequest();
        xhr.open('DELETE', '/api/v1/user/'+ user);
        xhr.onreadystatechange = () => {
          if (xhr.readyState === 4 && xhr.status === 200) {
            raw = document.getElementById("raw" + user);
            raw.remove();
            conasole.log('delete successful!');
            // let ul = document.getElementById('repos');
            // // ul.innerHTML = '';
            // while (ul.firstChild) {
            //   ul.removeChild(ul.firstChild);
            // }
            // data.items.forEach(item => {
            //   let a = document.createElement('a');
            //   a.appendChild(document.createTextNode(item.full_name));
            //   a.href = item.html_url;
            //   let li = document.createElement('li');
            //   if (item.has_issues) {
            //     li.classList.add('has-issues');
            //   }
            //   li.appendChild(a);
            //   ul.appendChild(li);
            // });
          }
        };
        xhr.send();
        };
    };


});


