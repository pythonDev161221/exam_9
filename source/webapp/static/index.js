
async function photoChooseClick(event){
    let url=event.target.dataset.chooseUrl;
    console.log(url)
    let response = await fetch(url);
    let responsebody = await response.json()

    let id = responsebody.photo_id;
    let div_photo_choose = document.getElementById(`${id}choose`);
    div_photo_choose.innerText = `choosen: ${responsebody.choose}`

}
