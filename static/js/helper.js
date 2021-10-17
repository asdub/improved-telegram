// Not currently in use
const csrftoken = Cookies.get('csrftoken');
console.log(csrftoken)

    function submitForm() {
        document.getElementById('update-form').submit()
    }

    function submitFormRemove(){
        document.getElementById('id_qty').value = 0;
        document.getElementById('update-form').submit();
    }

    let form = document.getElementById('update-form');

    form.addEventListener('submit', function(event) { 
        event.preventDefault()
        
        let data = new FormData();
        data.append('id_qty', document.getElementById('id_qty').value)  
        data.append('csrfmiddlewaretoken', csrftoken)
       
        axios.post('bag/update_order', data)
        .then(res => {
            console.log(csrftoken)
            location.reload()
        })
        .catch(errors => console.log(errors))

    })