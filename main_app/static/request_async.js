function get_data() {
    let urlInput = document.getElementsByName('url')[0]
    let button = document.getElementsByTagName('button')[0]
    console.log(button)
    let request = new XMLHttpRequest()
    urlInput.removeEventListener('click', changeAttr)
    request.open('POST', '/api/create/')
    const url = document.getElementsByName('url')[0].value
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.addEventListener('readystatechange', function () {
        if ((this.readyState === 4) && (this.status === 201)) {
            let answer = JSON.parse(this.responseText)
            let slug = answer['slug']
            urlInput.addEventListener('click', changeAttr
            )
            urlInput.value = slug
            button.innerHTML = 'Copy'
            button.setAttribute('onclick', 'copy()')
        } else if ((request.readyState === 4) && (request.status === 400)) {
            let answer = request.responseText
            console.log(answer)
        }
    })
    request.send("url=" + url)
}


function copy() {
    let urlInput = document.getElementsByName('url')[0]
    urlInput.select()
    document.execCommand('copy')
}

function changeAttr() {
    this.removeEventListener('click', changeAttr)
    let button = document.getElementsByTagName('button')[0]
    button.innerHTML = 'Shorten'
    button.setAttribute('onclick', 'get_data()')
}


