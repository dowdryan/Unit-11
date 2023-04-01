console.log("Time to Party!!!")
let count = 0
let gifSpace = $('#gifSpace')

async function getGif(searchTerm) {
    const res = await axios.get(`http://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym`)
    count >= 49 ? count = 0 : count++ 
    const response = res.data.data[count].images.original.url
    return appendGif(response)
}

function appendGif(response) {
    gifSpace.append(`<img src=${response}></img>`)
}

$('#userInput').on('submit', (event) => {
    event.preventDefault()
    const searchTerm = $('.searchTerm').val()
    getGif(searchTerm)
})

$('#removeGif').on('click', () => {
    gifSpace.empty()
})
