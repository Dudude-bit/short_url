function get_data() {
    let request = new XMLHttpRequest()
    request.open('POST', '/api/create/')
    const url = document.getElementsByName('url')[0].value
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.addEventListener('readystatechange', function () {
        if ((this.readyState === 4) && (this.status === 201)) {
            let answer = JSON.parse(this.responseText)
            let url = answer.url
            let slug = answer.slug
            document.getElementsByName('url')[0].value = url
            document.getElementsByName('slug')[0].value = slug


        } else if ((request.readyState === 4) && (request.status === 400)) {
            let answer = request.responseText
            console.log(answer)
        }
    })
    request.send("url=" + url)
}