function get_data() {
    let request = new XMLHttpRequest()
    request.open('POST', '/api/create/')
    const url = document.getElementsByName('url')[0].value
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.send("url=" + url)
}