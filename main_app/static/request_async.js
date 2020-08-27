function get_data() {
    let urlInput = document.getElementsByName('url')[0]
    let button = document.getElementsByTagName('button')[0]
    let request = new XMLHttpRequest()
    request.open('POST', '/api/create/')
    const url = document.getElementsByName('url')[0].value
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.addEventListener('readystatechange', function () {
        if ((this.readyState === 4) && (this.status === 201)) {
            let answer = JSON.parse(this.responseText)
            let slug = '127.0.0.1:8000/' + answer['slug']
            let addAnotherLink = document.createElement('button')
            addAnotherLink.innerHTML = 'Add another link'
            addAnotherLink.style.width = '50%'
            addAnotherLink.addEventListener('click', anotherLink)
            urlInput.value = slug
            button.innerHTML = 'Copy'
            button.style.width = '50%'
            button.parentNode.insertBefore(addAnotherLink, button.nextSibling)

            button.setAttribute('onclick', 'copy()')
        } else if ((request.readyState === 4) && (request.status === 400)) {
            let answer = request.responseText
            console.log(answer)
        }
    })
    console.log(document.cookie)
    request.send("url=" + url)
}


function copy() {
    let urlInput = document.getElementsByName('url')[0]
    urlInput.select()
    document.execCommand('copy')
    alert('Copied!')
}

function anotherLink(){
    this.parentNode.removeChild(this)
    let button = document.getElementsByTagName('button')[0]
    button.innerHTML = 'Shorten'
    button.setAttribute('onclick', 'get_data()')
    button.style.width = '100%'
    let urlInput = document.getElementsByName('url')[0]
    urlInput.value = ''

}


