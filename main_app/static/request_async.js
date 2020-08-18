function get_data() {
    let request = new XMLHttpRequest()
    request.open('POST', '/api/create/')
    const url = document.getElementsByName('url')[0].value
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.addEventListener('readystatechange', function () {
        console.log(request.status)
        console.log(request.readyState)
        console.log(request.responseText)
        if ((request.readyState == 4) && (request.status == 201)) {
            let answer = JSON.parse(request.responseText)
            let url = answer.url
            let slug = answer.slug
            document.getElementsByName('url')[0].value = url
            document.getElementsByName('slug')[0].value = slug


        }
        else if ((request.readyState == 4) && (request.status == 400)){

        }
    })
    request.send("url=" + url)
}