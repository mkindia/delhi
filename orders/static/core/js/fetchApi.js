const csrftoken = getCookie('csrftoken');

        function postoption(data)
        {
         let option = {
            method: 'POST',
            credentials: 'same-origin',
            headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': csrftoken,
            },
                body: JSON.stringify(data) //JavaScript object of data to POST
            } 

            return option ;
        }

        function putoption(data)
        {
         let option = { 
            method: 'PUT',
            credentials: 'same-origin',
            headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
            'X-CSRFToken': csrftoken,
            },
                body: JSON.stringify(data) //JavaScript object of data to POST
            } 

            return option ;
        
        }
   
   
   
   
   function getCookie(name) { 
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }return cookieValue;}